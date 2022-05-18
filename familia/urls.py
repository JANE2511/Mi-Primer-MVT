from django.urls import path
from familia import views
#localhost:8000/familia/agregar


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar")
]
