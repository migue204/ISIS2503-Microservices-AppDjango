from django.urls import path
from measurements import views

urlpatterns = [
    path("measurements/", views.measurements),
    path("measurements", views.measurements),
    path("measurements/create/", views.create_measurement),
    path("createmeasurements/", views.create_measurement),
    path("createmeasurements", views.create_measurement),
]
