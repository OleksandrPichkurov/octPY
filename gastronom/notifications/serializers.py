from django.contrib.auth.models import User
from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'sent', 'source', 'recipient', 'message', 'timestamp', 'send_method']


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class NotificationNestedSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'notifications']
