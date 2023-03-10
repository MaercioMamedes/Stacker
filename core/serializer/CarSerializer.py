from rest_framework import serializers
from core.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def validate(self, attrs):
        return attrs
