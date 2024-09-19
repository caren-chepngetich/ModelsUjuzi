from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status  
from rest_framework.generics import get_object_or_404
from kicd.models import Kicd
from .serializers import KicdSerializer
from modules.models import Module
from .serializers import ModuleSerializer
from  marking_scheme.models import MarkingScheme
from .serializers import MarkingSchemeSerializer


class KicdListView(APIView):
    def get(self, request):
        kicds = Kicd.objects.all()  
        first_name = request.query_params.get("first_name")
        if first_name:
            kicds = kicds.filter(first_name=first_name) 
        serializer = KicdSerializer(kicds, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = KicdSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KicdDetailView(APIView):
    def get(self, request, id):
        kicd = get_object_or_404(Kicd, id=id)
        serializer = KicdSerializer(kicd)  
        return Response(serializer.data)

    def put(self, request, id):
        kicd = get_object_or_404(Kicd, id=id) 
        serializer = KicdSerializer(kicd, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        kicd = get_object_or_404(Kicd, id=id)  
        kicd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ModuleListView(APIView):
    def get(self, request):
        modules = Module.objects.all()  
        serializer = ModuleSerializer(modules, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = ModuleSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModuleDetailView(APIView):
    def get(self, request, id):
        module = get_object_or_404(Module, id=id)  
        serializer = ModuleSerializer(module) 
        return Response(serializer.data)

    def put(self, request, id):
        module = get_object_or_404(Module, id=id)  
        serializer = ModuleSerializer(module, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkingSchemeListView(APIView):
    def get(self, request):
        marking_schemes = MarkingScheme.objects.all()  
        serializer = MarkingSchemeSerializer(marking_schemes, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = MarkingSchemeSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkingSchemeDetailView(APIView):
    def get(self, request, id):
        marking_scheme = get_object_or_404(MarkingScheme, id=id)  
        serializer = MarkingSchemeSerializer(marking_scheme) 
        return Response(serializer.data)

    def put(self, request, id):
        marking_scheme = get_object_or_404(MarkingScheme, id=id)  
        serializer = MarkingSchemeSerializer(marking_scheme, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
