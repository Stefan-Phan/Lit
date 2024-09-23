from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import Menu, Booking
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MenuItemView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class SingleMenuItemView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        item = get_object_or_404(Menu, pk=id)
        serializer = MenuSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        item = get_object_or_404(Menu, pk=id)
        serializer = MenuSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = get_object_or_404(Menu, pk=id)
        item.delete()
        return Response(status=status.HTTP_200_OK)


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})
