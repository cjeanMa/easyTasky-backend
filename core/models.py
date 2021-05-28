from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.


class User (AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Nombre de Usuario", max_length=200, unique=True)
    email = models.CharField("Email", max_length=200, unique=True)
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    celphone = models.CharField(max_length = 15)
    is_active = models.BooleanField("Esta Activo?", blank=True, default=True)
    is_staff = models.BooleanField("Permiso Administrador?", blank=True, default=True)
    date_joined = models.DateTimeField("Fecha Registro", auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class TaskCategory(models.Model):
    title_task_category = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


    class Meta:
        verbose_name = "Categoria tarea"
        verbose_name_plural = "Categorias de Tareas"

    def __str__(self):
        return self.title_task_category

class EventCategory(models.Model):
    title_event_category = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Categoria evento"
        verbose_name_plural = "Categoria de eventos"

    def __str__(self):
        return self.title_event_category

class TaskState(models.Model):
    value = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Estado Tarea"
        verbose_name_plural = "Estado Tareas"

    def __str__(self):
        return self.value

class EventState(models.Model):
    value = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Estado Evento"
        verbose_name_plural = "Estado Eventos"

    def __str__(self):
        return self.value

class Task(models.Model):
    title_task = models.CharField(max_length=200)
    description_task = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now = True, auto_now_add=False, blank=True, null=True)
    deleted_at = models.DateField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    image = models.FileField(upload_to="img/tasks/", blank = True, null=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_user")
    taskCategory = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, blank=True, null=True, related_name="task_category")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.title_task

class Event(models.Model):
    title_event = models.CharField(max_length=200)
    description_event = models.CharField(max_length=500)
    place_event = models.CharField(max_length=100, blank=True, null=True)
    date_event = models.DateField(auto_now = False, auto_now_add = False, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now = True, auto_now_add=False, blank=True, null=True)
    deleted_at = models.DateField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    image = models.FileField(upload_to="img/events/", blank = True, null= True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    eventCategory = models.ForeignKey(EventCategory, on_delete=models.CASCADE, blank=True, null=True, related_name="event_category")


    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.title_event
