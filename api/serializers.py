from django.contrib.auth.models import User
from rest_framework import serializers

from todolist.models import TodoList, Todo


class UserSerializer(serializers.ModelSerializer):

    todolists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TodoList.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'date_joined', 'todolists')


class TodoListSerializer(serializers.ModelSerializer):

    create_user = serializers.ReadOnlyField(source='create_user.username')

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'create_date', 'create_user', 'todos')


class TodoSerializer(serializers.ModelSerializer):

    create_user = serializers.ReadOnlyField(source='create_user.username')

    class Meta:
        model = Todo
        fields = (
            'id', 'todolist', 'description', 'create_date',
            'create_user', 'is_finished', 'deadline'
        )
