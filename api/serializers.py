from rest_framework import serializers
from movies.models import Gore
import base64
from django.core.files.base import ContentFile

class GoreSerializer(serializers.ModelSerializer):
    Picture = serializers.CharField(required=True, allow_blank=False)

    class Meta:
        model = Gore
        fields = '__all__'

    def validate_picture(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen no válida")
        return None
