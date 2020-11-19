from django.urls import path
from Primavera import viewsprimavera



   
urlpatterns = [
    path('', viewsprimavera.BlogListView.as_view(),name='home'),  
   # path('post/teste/', views.hello, name='hello'),
    path('post/new/', viewsprimavera.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/detail/', viewsprimavera.BlogDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/edit/', viewsprimavera.BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/', viewsprimavera.BlogDeleteView.as_view(), name='post_delete'),
    #path('post_detail.html', viewsprimavera.Detail_View,name='Detail'),
   

]






