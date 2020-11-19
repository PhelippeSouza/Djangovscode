
from django.urls import path

from blogloh import views
from inverno import viewsinverno



urlpatterns = [
    path('', viewsinverno.BlogListView.as_view(),name='home'),  
    path('post/teste/', viewsinverno.hello, name='hello'),
    path('post/new/', viewsinverno.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/detail/', viewsinverno.BlogDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/edit/', viewsinverno.BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/', viewsinverno.BlogDeleteView.as_view(), name='post_delete'),
    path('post_detail.html', viewsinverno.Detail_View,name='Detail'),
   

]