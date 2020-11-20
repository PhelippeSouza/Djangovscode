from django.urls import path
from outono import viewsoutono



   
urlpatterns = [
    path('', viewsoutono.BlogListView.as_view(),name='home'),  
    path('post/new/', viewsoutono.BlogCreateView.as_view(), name='post_new'),
    path('outono/<int:pk>/detail/', viewsoutono.BlogDetailView.as_view(),name='outono_detail'),
    path('post/<int:pk>/edit/', viewsoutono.BlogUpdateView.as_view(),name='post_edit'),
    path('outono/<int:pk>/delete/', viewsoutono.BlogDeleteView.as_view(), name='outono_delete'),
  

]