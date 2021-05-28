# Create your views here.
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import (UserSerializer,
                          TaskSerializer,
                          UserBasicSerializer,
                          EventSerializer,
                          CategoryTaskSerializer,
                          CategoryEventSerializer
                          )

@api_view(['GET'])
def ApiListTaskCategoryView(request):

    if request.method == "GET":
        categoriesTask = TaskCategory.objects.all()
        serializer_categories = CategoryTaskSerializer(categoriesTask, many=True)
        return Response(serializer_categories.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def ApiListEventCategoryView(request):

    if request.method == "GET":
        categoriesEvent = EventCategory.objects.all()
        serializer_categories = CategoryEventSerializer(categoriesEvent, many=True)
        return Response(serializer_categories.data, status = status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def ApiListTasksView(request):

    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer_tasks = TaskSerializer(tasks, many = True)
        return Response(serializer_tasks.data)

    elif request.method == 'POST':
        task_serializer = TaskSerializer(data = request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data)
        else:
            return Response(task_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def ApiListEventsView(request):

    if request.method == 'GET':
        events = Event.objects.all()
        events_serializer = EventSerializer(events, many = True)
        return Response(events_serializer.data)

    elif request.method == 'POST':
        event_serializer = EventSerializer(data =request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data)
        else:
            return Response(event_serializer.errors)


@api_view(['GET', 'POST', 'PUT'])
def ApiListUsersView(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def ApiUserView(request, idUser):

    user = User.objects.filter(pk = idUser).first()

    if  user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.update()
                return Response(user_serializer.data)
            return Response(user_serializer.errors)

        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status = status.HTTP_200_OK)

    return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def ApiTaskView(request, idTask):

    task = Task.objects.filter(pk = idTask).first()

    if task:
        if request.method == 'GET':
            task_serializer = TaskSerializer(task)
            return Response(task_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            task_serializer = TaskSerializer(task, data = request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response(task_serializer.data, status = status.HTTP_200_OK)
            return Response(task_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            task.delete()
            return Response({"message":"Tarea eliminada correctamente"}, status = status.HTTP_200_OK)
    return Response({"message":"Tarea no encontrada"}, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def ApiEventView(request, idEvent):

    event = Event.objects.filter(pk = idEvent).first()

    if event:
        if request.method == 'GET':
            event_serializer = EventSerializer(event)
            return Response(event_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            event_serializer = EventSerializer(event, data = request.data)
            if event_serializer.is_valid():
                event_serializer.save()
                return Response(event_serializer.data, status = status.HTTP_200_OK)
            return Response(event_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            event.delete()
            return Response({"message":"Evento eliminada correctamente"}, status = status.HTTP_200_OK)
    return Response({"message":"Evento no encontrado"}, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def ApiTasksByUserView(request, idUser):
    if request.method == 'GET':
        tasks = Task.objects.filter(id_user = idUser).order_by('created_at')
        print(tasks)
        tasks_serializer = TaskSerializer(tasks, many = True)
        return Response(tasks_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def ApiEventsByUserView(request, idUser):
    if request.method == 'GET':
        events = Event.objects.filter(id_user=idUser).order_by('date_event')
        events_serializer = EventSerializer(events, many=True)
        return Response(events_serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def ApiLoginView(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username= username).first()
        user_serializer = UserBasicSerializer(user)
        if user:
            if user.check_password(password):
                return Response({"data": user_serializer.data, "success":True}, status = status.HTTP_200_OK)
            return Response({'message': 'Contrasenha incorrecta', 'success': False}, status = status.HTTP_200_OK)
        return Response({'message': 'Error de autenticacion, revisa tu usuario o password', 'success': False}, status = status.HTTP_200_OK)



