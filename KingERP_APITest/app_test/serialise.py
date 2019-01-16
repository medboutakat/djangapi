from rest_framework import serializers
from .models import test
class TestSerializer(serializers.HyperlinkedModelSerializer):        
    class Meta:
            model = test
            fields= ('url','name1','name2','name3','file')