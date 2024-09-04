from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskModelSerializers
from rest_framework import status
from .models import TaskModel
# Create your views here.

class TaskView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try: 
            user_id = request.user.id
            data = request.data
            data['user'] = user_id
            serializer = TaskModelSerializers(data)
            serializer.is_valid(raise_exception=True)
            return Response({
                "status":status.HTTP_201_CREATED,
                "message":"Task created"
            })
        except Exception as e:
            return Response({
                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message":serializer.errors()
            })
        

        
    def get(self, request):
        user_id = request.user.id
        task_obj = TaskModel.objects.get(user_id = user_id)
        serializer = TaskModelSerializers(task_obj)

        return Response({
            "status":status.HTTP_200_OK,
            "data":serializer.data
        })
    
    def patch(self, request):
        serializer = TaskModelSerializers(id = request.data.task_id, data=request.DATA, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response({
            "status":status.HTTP_202_ACCEPTED,
            "message":"Data Updated"
        })
    
    def delete(self, request):
        task_id = request.data.task_id
        try:
            TaskModel.objects.delete(id = task_id)
            return Response({
                "status":status.HTTP_200_OK,
                "message":"Object deleted"
            })

        except Exception as e:
            return Response({
                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message":str(e)
            })


        

    



