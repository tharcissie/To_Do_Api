from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializer import ToDoSerializer
from .models import ToDo
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from django.http import Http404
from rest_framework.views import APIView

# Create your views here.

# @csrf_exempt
# def todo_list(request):

#     if request.method == 'GET':
#         list = ToDo.objects.all()
#         serializer = ToDoSerializer(list, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ToDoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ToDoList(APIView):
    """
    List all todos, or create a new ones.
    """
    def get(self, request, format=None):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @csrf_exempt
# def todo_detail(request, pk):


#     try:
#         item = ToDo.objects.get(pk=pk)
    
#     except ToDo.DoesNotExist:

#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ToDoSerializer(item)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ToDoSerializer(item, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         item.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class ToDoDetail(APIView):
    """
    Retrieve, update or delete a todo instance.
    """
    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = ToDoSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = ToDoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)