from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos.views import TodoViewSet
from django.shortcuts import render  # 使用 render

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')


def home_view(request):
    return render(request, 'home.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    # ✅ 使用正式模板
    path('', home_view, name='home'),
]