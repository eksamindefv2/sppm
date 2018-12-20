from django.contrib.auth.backends import ModelBackend
from django_python3_ldap import ldap
from Pentadbir.models import Peranan, Profil


class SPPMLDAPBackend(ModelBackend):

    """
    An authentication backend that delegates to an LDAP
    server.
    User models authenticated with LDAP are created on
    the fly, and syncronised with the LDAP credentials.
    """

    supports_inactive_user = False

    def authenticate(self, *args, **kwargs):

            # for arg in args:
            # 	print(arg)

            # for kwarg in kwargs:
            # 	print(kwarg)

            # print(ldap.authenticate(*args, **kwargs))
            # print(self.ldap_attributes)
            # print(self.ldap_attributes)
            username = ldap.authenticate(*args, **kwargs)
            # username = ldap.authenticate(*args, **kwargs)
            # username = ldap.authenticate(*args, **kwargs)
            # username = ldap.authenticate(*args, **kwargs)
            print('type='+str(type(username)))
            p = Profil(user=username)
            print('Nokpten='+str(p.nokpten))

            username2 = ldap.authenticate(*args, **kwargs)
            # type(username)
            # print(username)
            # print('username kat backend='+ username)
            # if username == "usersysadmineksa":
            if username == username2:
            	print("sama")
            	return ldap.authenticate(*args, **kwargs)

            else:
            	print("tak sama")
            	return None

    	
    	# # self.user
    	# for arg in args:
    	# 	print(arg)
    	# for kwarg in kwargs:
    	# 	print(kwarg)
        
    	# for arg in args:
    	# 	print(arg)

        # return ldap.authenticate(*args, **kwargs)