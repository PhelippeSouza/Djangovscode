from django.urls import path
from Primavera import viewsprimavera


urlpatterns = [

    path('Primavera/', viewsprimavera.NovaPrimavera_View,name='primavera_nova'),
    path('post/<int:pk>/Primavera/', viewsprimavera.Primavera_View,name='primavera_new'),
    path('', viewsprimavera.BlogListView.as_view(),name='Primavera'),  
    path('post/new/', viewsprimavera.BlogCreateView.as_view(), name='primavera_home'),
    path('post/<int:pk>/detail/', viewsprimavera.BlogDetailView.as_view(),name='primavera_detail'),
    path('post/<int:pk>/edit/', viewsprimavera.BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/', viewsprimavera.BlogDeleteView.as_view(), name='post_delete'),
 
]






