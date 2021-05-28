from django.urls import path, include
from .views import (
    ApiListTasksView,
    ApiUserView,
    ApiListUsersView,
    ApiTasksByUserView,
    ApiTaskView,
    ApiLoginView,
    ApiEventsByUserView,
    ApiListEventsView,
    ApiListTaskCategoryView,
    ApiListEventCategoryView,
    ApiEventView,
)
from rest_framework import routers
"""Metodo por ViewSet"""
"""
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
"""
"""path('', include(router.urls)),"""
"""Metodo por APIVIEW"""
"""path('tasks_api/', TaskAPIView.as_view(), name = "api_tasks"),"""
urlpatterns = [
    path('categoryTasks/', ApiListTaskCategoryView),
    path('categoryEvents/', ApiListEventCategoryView),
    path('tasks/', ApiListTasksView),
    path('tasks/<int:idTask>', ApiTaskView),
    path('events/', ApiListEventsView),
    path('events/<int:idEvent>', ApiEventView),
    path('user/tasks/<int:idUser>', ApiTasksByUserView),
    path('user/events/<int:idUser>', ApiEventsByUserView),
    path('users/', ApiListUsersView),
    path('user/<int:idUser>', ApiUserView),

    #Logeo
    path('login/', ApiLoginView),
]
