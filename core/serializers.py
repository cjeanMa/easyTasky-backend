from .models import User, Task, Event, TaskCategory, EventCategory
from rest_framework import serializers, viewsets

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CategoryTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        exclude = ['description']

class CategoryEventSerializer(serializers.ModelSerializer):
    class Meta :
        model = EventCategory
        exclude = ['description']

class UserBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'surname']


class TaskSerializer(serializers.ModelSerializer):

    #id_user = serializers.StringRelatedField(read_only=True)
    #taskCategory = CategoryTaskSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        #exclude = ['title_task']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title_task': instance.title_task,
            'description_task': instance.description_task,
            #'taskCategory': instance.taskCategory.title_task_category if instance.taskCategory.title_task_category != "" else "",
            'taskCategory': instance.taskCategory.id if instance.taskCategory.id != "" else "",
            'created_at': instance.created_at,
            'id_user': instance.id_user.id
        }

class TaskBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):

    #eventCategory = CategoryEventSerializer(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"





