from rest_framework import serializers
from .models import Employee

class EmployeeSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    salary = serializers.FloatField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.salary = validated_data.get('salary',instance.salary)
        instance.save()
        return instance
