
from rest_framework import permissions

class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
    	if request.user.has_perm('auth.view_user'):
    		return True
    	else:
	    	return False