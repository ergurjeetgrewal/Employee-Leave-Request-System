from rest_framework import serializers
from app.models import Employeeleave

class EmployeeleaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeeleave
        fields = '__all__'