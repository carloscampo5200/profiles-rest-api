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


class UpdateOwnStatus(permissions.BasePermission):
	""" Allow users to update their own status """
	
	def has_object_permission(self, request, view, obj):
		""" Check the user is trying to update their own status """
		if request.method in permissions.SAFE_METHODS:
			return True

		#If the user is the same of the id of the object, it is allowed, if not it is blocked 
		return obj.user_profile.id == request.user.id 