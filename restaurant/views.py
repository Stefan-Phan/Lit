from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import Menu, Booking
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404
# Create your views here.


class MenuItemView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class SingleMenuItemView(APIView):
    def get(self, request, id):
        item = get_list_or_404(Menu, pk=id)
        serializer = MenuSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        item = get_list_or_404(Menu, pk=id)
        serializer = MenuSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = get_list_or_404(Menu, pk=id)
        item.delete()
        return Response(status=status.HTTP_200_OK)
