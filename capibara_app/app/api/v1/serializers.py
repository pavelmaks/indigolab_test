from api.models import Capibara
from rest_framework import serializers


class CapibaraSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['capibara_phrases'] = list(set(validated_data['capibara_phrases']))
        return Capibara.objects.create(**validated_data)

    class Meta:
        model = Capibara
        fields = '__all__'
