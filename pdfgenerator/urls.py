from django.contrib import admin
from django.urls import path
from pdf import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('add/', views.adding, name="add"),
    path('<int:id>/', views.cv, name="cv"),
    path('list/', views.list, name="list"),
]
