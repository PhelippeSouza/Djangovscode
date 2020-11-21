from django.urls import path
from Primavera import viewsprimavera


urlpatterns = [

    path('', viewsprimavera.BlogListView.as_view(),name='home'),  
   # path('post/teste/', views.hello, name='hello'),
    path('post/new/', viewsprimavera.BlogCreateView.as_view(), name='primavera_new'),
    path('primavera/<int:pk>/detail/', viewsprimavera.BlogDetailView.as_view(),name='primavera_detail'),
    path('primavera/<int:pk>/edit/', viewsprimavera.BlogUpdateView.as_view(),name='primavera_edit'),
    path('primavera/<int:pk>/delete/', viewsprimavera.BlogDeleteView.as_view(), name='primavera_delete'),
    
]




