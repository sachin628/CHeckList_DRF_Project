from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CheckListSerializer, CheckListItemSerializer
from .models import CheckList,CheckListItem
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwner

# Create your views here.


# for retrieve the all data from the checklist...
class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer
    permission_classes =[IsAuthenticated,IsOwner]
    def get(self, request, format=None):
        data =  CheckList.objects.filter(user=request.user) # for get instances from db'model' and request.user used for get the validate user
        serializer= self.serializer_class(data, many=True) #for instance the serialize object
        serialized_data = serializer.data
        return Response(serialized_data)
    
    # Create CheckList
    def post(self, request, format=None):
        #code for creation
        serializer = self.serializer_class(data=request.data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# for retrieve single object from the checklist
class CheckListAPIView(APIView):
    serializer_class =CheckListSerializer
    permission_classes =[IsAuthenticated,IsOwner]
    def get_object(self, pk):
        try:
            obj =CheckList.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except CheckList.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    # For edit the object of CheckList
    def put(self, request,pk, format=None):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance, data=request.data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    #For delete the checklist object
    def delete(self, request,pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Create APi for CheckListItem...............................................................

class CheckListItemCreateAPIView(APIView):
    serializer_class = CheckListItemSerializer
    permission_classes =[IsAuthenticated,]
    
    #for create the checklistItem
    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckListItemAPIView(APIView):
    serializer_class = CheckListItemSerializer
    permission_classes =[IsAuthenticated,]
    def get_object(self, pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    
    # For edit the object of CheckListItem
    def put(self, request,pk, format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item, data=request.data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    #For delete the checklist object
    def delete(self, request,pk, format=None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Using the Generic APIView..................................

# from rest_framework.generics import (
#     CreateAPIView,
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )


# class CheckListsAPIView(ListCreateAPIView):
#     """
#     Listing, Creation
#     """
#     serializer_class = CheckListSerializer
#     permission_classes = [IsAuthenticated, IsOwner]

#     def get_queryset(self):
#         queryset = CheckList.objects.filter(user=self.request.user)
#         return queryset

# 
# class CheckListAPIView(RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, Update, Destroy
#     """
#     serializer_class = CheckListSerializer
#     permission_classes = [IsAuthenticated, IsOwner]

#     def get_queryset(self):
#         queryset = CheckList.objects.filter(user=self.request.user)
#         return queryset

# class CheckListItemCreateAPIView(CreateAPIView):
#     """
#     Creation
#     """
#     serializer_class = CheckListItemSerializer
#     permission_classes = [IsAuthenticated, IsOwner]

# class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, Update, Delete
#     """
#     serializer_class = CheckListItemSerializer
#     permission_classes = [IsAuthenticated, IsOwner]

#     def get_queryset(self):
#         queryset = CheckListItem.objects.filter(user=self.request.user)
#         return queryset