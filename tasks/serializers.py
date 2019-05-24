from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'content', 'user', 'status', 'completion_date', 'created_at', 'updated_at',)
        model = Task
