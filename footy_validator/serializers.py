from rest_framework import serializers


class PlayerSearchResultSerializer(serializers.Serializer):
    player_picture_url = serializers.SerializerMethodField()
    player_url = serializers.SerializerMethodField()

    def get_player_picture_url(self, obj):
        return obj.player_picture

    def get_player_url(self, obj):
        return obj.player_url
