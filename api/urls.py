from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('todolists', views.TodoListViewSet)
router.register('todos', views.TodoViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
