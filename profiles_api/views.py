from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
	""" Test API View """ 

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


