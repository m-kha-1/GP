from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse


from django.shortcuts import get_object_or_404

from .models import PRODUCTION,Task,Producer
from .serializers import ProdSerializer,TaskSerializer,ProducerSerializer







@api_view(['POST'])
def addProd(request):
    serializer=ProdSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response (serializer.data)
  


@api_view(['GET'])
def prod(request):
    productions=PRODUCTION.objects.all()
    serializer=ProdSerializer(productions,many=True)
    
    return Response (serializer.data)


@api_view(['GET'])
def prodId(request,prod_id):
   production =PRODUCTION.objects.get(id=prod_id)
   serializer=ProdSerializer(production,many=False)
   
   return Response (serializer.data)

@api_view(['GET'])
def get_producer(request):
    producer=Producer.objects.all()
    serializer=ProducerSerializer(producer,many=True)
    
    return Response (serializer.data)
        

@api_view(['PUT'])
def updateId(request,prod_id):
   production =PRODUCTION.objects.get(id=prod_id)
   serializer=ProdSerializer(production,data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response (serializer.data)
   
   return Response(serializer.errors, status=400)



@api_view(['DELETE'])
def delId(request,prod_id):
    
   production =PRODUCTION.objects.get(id=prod_id)
   
   production.delete() 
   return HttpResponse ("production deleted successfully")



@api_view(['GET'])
def get_PRODUCTION_id(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    production_id = task.PRODUCTIONId.id if task.PRODUCTIONId else None
    return Response({'production_id': production_id})

@api_view(['GET'])
def get_task_ids_by_production(request, production_id):
    production = get_object_or_404(PRODUCTION, pk=production_id)
    # task_ids = production.PRODUCTIONTasks.values_list('id', flat=True)
    # return Response({'task_ids': list(task_ids)})
    tasks = production.PRODUCTIONTasks.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({'tasks': serializer.data})









