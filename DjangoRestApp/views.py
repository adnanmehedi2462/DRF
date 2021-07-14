from django.shortcuts import render,redirect,get_object_or_404
from DjangoRestApp.models import artical
from DjangoRestApp.serializers import articalSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class articallist(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artical.html'

    def get(self, request, format=None):
        arti = artical.objects.all()
        serializer = articalSerializer(arti, many=True)
        return Response({'artical':arti})

    def post(self, request, format=None):
        serializer = articalSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'serializer':serializer})
        serializer.save()
            
        return redirect('articallist')




class crud(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artical.html'
    def get_object(self, pk):
        try:
            return artical.objects.get(pk=pk)
        except artical.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artical = self.get_object(pk)
        serializer = articalSerializer(artical)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        artical = self.get_object(pk)
        serializer = articalSerializer(artical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        artical = self.get_object(pk)
        artical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET', 'POST'])

# @csrf_exempt
# def articallist(request):
# 	if request.method == 'GET':
# 		arti=artical.objects.all()
# 		serializer=articalSerializer(arti,many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':

# 		serializer=articalSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data,status=201)
# 		return Response(serializer.errors,status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# def crud(request, pk):
#     """
#     Retrieve, update or delete a code artical.
#     """
#     try:
#         Artical = artical.objects.get(pk=pk)
#     except artical.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = articalSerializer(Artical)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = articalSerializer(Artical, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         Artical.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







 