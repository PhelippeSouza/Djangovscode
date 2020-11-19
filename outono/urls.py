from django.urls import path
from outono import viewsoutono



   
urlpatterns = [
    path('', viewsoutono.BlogListView.as_view(),name='home'),  
   # path('post/teste/', views.hello, name='hello'),
    path('post/new/', viewsoutono.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/detail/', viewsoutono.BlogDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/edit/', viewsoutono.BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/', viewsoutono.BlogDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/', viewsoutono.BlogDetailView.as_view(),name='post_detail'),
    #path('post_detail.html', viewsoutono.Detail_View,name='Detail'),
   

]