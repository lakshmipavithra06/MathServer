
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('calculate_BMI/', views.calculate_BMI, name = "BMI"),
    path('', views.calculate_BMI, name="BMIroot")
]

