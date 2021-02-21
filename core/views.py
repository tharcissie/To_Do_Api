from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializer import ToDoSerializer
from .models import ToDo

# Create your views here.

@csrf_exempt
def todo_list(request):

    if request.method == 'GET':
        list = ToDo.objects.all()
        serializer = ToDoSerializer(list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            retun JsonResponse(serializer.data, status=201)
        retun JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo_detail(request, pk):

     try:
         item = ToDo.objects.get(pk=pk)
    
    except ToDo.DoesNotExist:
        retun HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ToDoSerializer(item)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ToDoSerializer(item, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)
