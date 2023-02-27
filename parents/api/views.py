from parents.models import Parents, Children, GrandParent, Siblings
from rest_framework.generics import CreateAPIView, ListAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from parents.api.serializers import ParentsSerializer, ChildrenSerializer, GrandParentsSerializer,SiblingsSerializer

# Function Based View
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response

def GrandParentsListView(request):
    grandparent = GrandParent.objects.all()
    serializer = GrandParentsSerializer(grandparent, many = True)
    return JsonResponse(serializer.data)
 
  




class GrandParentsCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GrandParentsSerializer
    queryset = GrandParent.objects.all()

class GrandParentsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GrandParentsSerializer
    queryset = GrandParent.objects.all()

class GrandParentsUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GrandParentsSerializer
    queryset = GrandParent.objects.all()

class GrandParentsDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GrandParentsSerializer
    queryset = GrandParent.objects.all()

class ParentsCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ParentsSerializer
    queryset = Parents.objects.all()

class ParentsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ParentsSerializer
    queryset = Parents.objects.all()

class ParentsUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ParentsSerializer
    queryset = Parents.objects.all()

class ParentsDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ParentsSerializer
    queryset = Parents.objects.all()

class ChildrenCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChildrenSerializer
    queryset = Children.objects.all()


class ChildrenListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ChildrenSerializer
    queryset = Children.objects.all()


class ChildrenUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChildrenSerializer
    queryset = Children.objects.all()


class ChildrenDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChildrenSerializer
    queryset = Children.objects.all()

class SiblingsCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SiblingsSerializer
    queryset = Siblings.objects.all()

class SiblingsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SiblingsSerializer
    queryset = Siblings.objects.all()

class SiblingsUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SiblingsSerializer
    queryset = Siblings.objects.all()

class SiblingsDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SiblingsSerializer
    queryset = Siblings.objects.all()