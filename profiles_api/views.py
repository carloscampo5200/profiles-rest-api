from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings 
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
	""" Test API View """ 
	serializer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		""" Returns a list of APIView features """

		an_apiview = [
			'Uses HTTP methods as function (Get, Post, Patch, Put, Delete)',
			'Is similar to a traditional Django View',
			'Gives you the most control over your application logic',
			'Is mapped manually to URLs',
		]

		""" Message return. Converts dictionary or list to JSON and responds to the message sent to the API"""  
		return Response({'message':'Hello!', 'an_apiview': an_apiview })


	def post(self, request):
		""" Create a hello message with our name """
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'

			return Response({'message': message})

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk=None):
		""" Handle updating an object - Replaces an object with the new object"""
		return Response({'method': 'PUT'})


	def patch(self, request, pk=None):
		""" Handle a partial update of an object / only the fields provided in the request """
		return Response({'method': 'PATCH'})

	def delete(self, request, pk=None):
		""" Delete an object in database"""
		return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
	""" Test API ViewSet """
	serializer_class = serializers.HelloSerializer

	def list(self, request):
		""" Return a hello message """
		a_viewset = [
			'Uses actions (list, create, retrieve, update, partial_update',
			'Automatically maps to URLs using Routers',
			'Provides more functionality with less code',
		]
		
		return Response({'message': 'Hello!', 'viewset': a_viewset})


	def create(self, request):
		""" Create a new Hello Message """
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def retrieve(self, request, pk=None):
		""" Handle getting an object by its ID """ 
		return Response({'http_method': 'GET'})


	def update(self, request, pk=None):
		""" Handle updating an object """
		return Response({'http_method': 'PUT'})


	def partial_update(self, request, pk=None):
		""" Handle updating part of an object """
		return Response({'http_method': 'PATCH'})


	def destroy(self, request, pk=None):
		""" Handle removing an object """
		return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
	""" Handle creating and updating profiles """
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	# Authentication variable is created as a touple
	authentication_classes = (TokenAuthentication, )
	permission_classes = (permissions.UpdateOwnProfile, )

	# Search functionality
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
	""" Handle creating user authentication tokens """
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# This part requires listening to the explanation . 62 y 63 Create Profile Feed sitem erializer
class UserProfileFeedViewSet(viewsets.ModelViewSet):
	""" Handles creating, reading and updating profile feed items """
	authentication_classes = (TokenAuthentication,)
	serializer_class = serializers.ProfileFeedItemSerializer
	queryset = models.ProfileFeedItem.objects.all()
	## Authenticates so that only Authenticated Users can get or modigy the Feedview Lists
	## Note / if you want non authenticated users to be able to GET *read* the Feedview list, 
	## simply change IsAuthenticated to IsAuthenticatedOrReadOnly (Change import above) 
	permission_classes = (
		permissions.UpdateOwnStatus, 
		IsAuthenticated	
	)

	def perform_create(self, serializer):
		""" Sets the user profile to the logged in user """
		serializer.save(user_profile=self.request.user)















