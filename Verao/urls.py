from django.urls import path
from Verao import viewsverao


urlpatterns = [

    path('', viewsverao.BlogListView.as_view(),name='home'),  
   # path('post/teste/', views.hello, name='hello'),
    path('post/new/', viewsverao.BlogCreateView.as_view(), name='verao_new'),
    path('verao/<int:pk>/detail/', viewsverao.BlogDetailView.as_view(),name='verao_detail'),
    path('verao/<int:pk>/edit/', viewsverao.BlogUpdateView.as_view(),name='verao_edit'),
    path('verao/<int:pk>/delete/', viewsverao.BlogDeleteView.as_view(), name='verao_delete'),
    
]

