from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
	"""Allow user to edit their own profile"""

	def has_object_permission(self, request, view, obj):
		"""Check if user is trying to edit their own profile """


		## Check if request is safe (Read is a safe method, doesn't edit)
		if request.method in permissions.SAFE_METHODS:
			return True
		## If it is not safe, then check user id 
		return obj.id == request.user.id
