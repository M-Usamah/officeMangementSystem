from rest_framework import serializers
from .models import EmployDetails  # Import your model

class EmployDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployDetails  # Specify the model associated with the serializer
        fields = '__all__'  # You can specify specific fields if needed
