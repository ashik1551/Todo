from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from .serializers import *
from rest_framework import status,authentication,permissions

class Registration(APIView):

    def post(self,request,*args,**kwargs):
        serializer=User_reg_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class Todoviewset(ViewSet):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Taskmodel.objects.filter(user=request.user)
        serializer=Task_serializer(qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        try:
            qs=Taskmodel.objects.get(id=id)
        except:
            return Response({"message":"id not exist"},status=status.HTTP_404_NOT_FOUND)

        if qs.user==request.user:
            serializer=Task_serializer(qs)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def create(self,request,*args,**kwargs):
        serializer=Task_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        try:
            data=Taskmodel.objects.get(id=id)
        except:
            return Response({"message":"id not exist"},status=status.HTTP_404_NOT_FOUND)

        if data.user==request.user:
            data.delete()
            return Response({"message":"Todo object removed"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
            # raise serializers.ValidationError("not allowed")
            
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        try:
            qs=Taskmodel.objects.get(id=id)
        except:
            return Response({"message":"id not exist"},status=status.HTTP_404_NOT_FOUND)
        
        if qs.user==request.user:
            serializer=Task_serializer(data=request.data,instance=qs)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"id not exist"},status=status.HTTP_404_NOT_FOUND)

class Todomodelviewset(ModelViewSet):
    queryset=Taskmodel.objects.all()
    serializer_class=Task_serializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Taskmodel.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        try:
            qs=Taskmodel.objects.get(id=kwargs.get('pk'))
        except:
            return Response({"message":"id not exists"},status=status.HTTP_404_NOT_FOUND)
        
        if qs.user==request.user:
            self.perform_destroy(qs)
            return Response({"message":"Todo object deleted"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message":"not allowed"},status=status.HTTP_406_NOT_ACCEPTABLE)
        