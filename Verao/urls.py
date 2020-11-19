from django.urls import path
from Verao import views


urlpatterns = [

    path('Verão/', views.Verão_View,name='verão'),
    path('post/<int:pk>/Verão/', views.Verão_View,name='Verão_new'),
    # path('', views.BlogListView.as_view(),name='Primavera'),  
    # path('post/new/', views.BlogCreateView.as_view(), name='primavera_home'),
    # path('post/<int:pk>/detail/', views.BlogDetailView.as_view(),name='primavera_detail'),
    # path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(),name='post_edit'),
    # path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
 
]

