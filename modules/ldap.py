from django_python3_ldap.utils import format_search_filters, sync_user_relations
from django.contrib.auth.models import Group, User
from Pentadbir.models import Peranan, Profil

# Filter ldap which type of ldap object can access the system
# Memastikan hanya person object shj boleh key in
def custom_format_search_filters(ldap_fields):
    # Add in simple filters.
    ldap_fields["objectclass"] = "person"
    # Call the base format callable.
    search_filters = format_search_filters(ldap_fields)
    # Advanced: apply custom LDAP filter logic.
    return search_filters

# Sync user apabila berjaya authenticate
def custom_sync_user_relations(user, ldap_attributes):

    # Cipta rekod profil bagi AD user yang berjaya di'authenticate'
    # Namun begitu, AD user ini hendaklah disenaraikan dalam table Peranan untuk masuk
    try:
        # Semak sama ada profil user telah wujud atau tidak. Jika tidak, pergi ke except
        profilusr = Profil.objects.get(nokpten=ldap_attributes['extensionattribute6'][0])

    # Cipta rekod profil dengan no ic / tentera yang ada pada AD user tersebut
    except (Profil.DoesNotExist):
        profilusr = Profil(nokpten=ldap_attributes['extensionattribute6'][0],user=user)
        profilusr.save()
        # pass