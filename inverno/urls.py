
from django.urls import path

from blogloh import views
from inverno import viewsinverno



urlpatterns = [
    path('', viewsinverno.BlogListView.as_view(),name='invernohome'),  
    #path('post/teste/', viewsinverno.hello, name='hello'),
    path('inverno/<int:pk>/edit/', viewsinverno.BlogUpdateView.as_view(),name='inverno_edit'),
    path('inverno/<int:pk>/delete/', viewsinverno.BlogDeleteView.as_view(), name='inverno_delete'),
    path('post/new/', viewsinverno.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/inverno/', viewsinverno.BlogDetailView.as_view(),name='post_inverno'),


]