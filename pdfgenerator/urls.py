from django.contrib import admin
from django.urls import path
from pdf import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('done', views.submit, name="submit")
]
