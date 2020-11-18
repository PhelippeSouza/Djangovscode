from django.urls import path
from Primavera import viewsprimavera

urlpatterns = [

    path('Primavera/', viewsprimavera.NovaPrimavera_View,name='primavera_nova'),
    path('post/<int:pk>/Primavera/', viewsprimavera.NovaPrimavera_View,name='primavera_nova'),
  

]




