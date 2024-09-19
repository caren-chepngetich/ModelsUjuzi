from rest_framework import serializers
from kicd.models import Kicd 
from modules.models import Module
from marking_scheme.models import MarkingScheme


class KicdSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Kicd  
        fields = "__all__"

class ModuleSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Module  
        fields = "__all__"

class MarkingSchemeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MarkingScheme 
        fields = "__all__"
