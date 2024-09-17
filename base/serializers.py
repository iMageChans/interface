import re
from rest_framework import serializers

class KeypairSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    path = serializers.CharField(required=True, allow_blank=True)

    def validate_path(self, value):
        if value == "":
            return value

        if not re.match(r'^/\d+$', value):
            raise serializers.ValidationError("The path must be empty or in the format '/1', '/2', etc.")
        return value