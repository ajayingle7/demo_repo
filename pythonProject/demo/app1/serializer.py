from rest_framework import serializers
from .models import Employee



class EmployeeSerialzier(serializers.Serializer):
    eid = serializers.IntegerField()
    ename = serializers.CharField(max_length=50)
    esal = serializers.FloatField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.eid = validated_data.get("eid",instance.eid)
        instance.ename = validated_data.get("eid",instance.ename)
        instance.esal  =validated_data.get("esal",instance.esal)
        instance.save()
        return instance

