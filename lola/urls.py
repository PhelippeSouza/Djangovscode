"""lola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from blogloh import views
from Primavera import viewsprimavera
from Verao import viewsverao
from outono import viewsoutono
from inverno import viewsinverno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('Primavera/', include('Primavera.urls')),
    path('outono/', include('outono.urls')),
    path('inverno/', include('inverno.urls')),
    
    


    path('Verao/', include('Verao.urls')),
    path('', include('blogloh.urls')),

    
    path('post_edit.html', views.BlogUpdateView.as_view(),name='post_edit'),
   
    path('devocionais.html', views.Devocional_View, name = 'Devocional'),

    

    path('primaveraview.html', viewsprimavera.BlogCreateView.as_view(), name = 'primavera_new'),
    path('primaveradetail.html', viewsprimavera.BlogDetailView.as_view(),name='primavera_detail'),
    path('primaverahome.html', viewsprimavera.BlogListView.as_view(), name = 'primavera_home'),
   

    path('verãoview.html', viewsverao.BlogCreateView.as_view(), name = 'Nova Postagem'),
    path('veraodetail.html', viewsverao.BlogDetailView,name='verao_detail'),
    path('verãohome.html', viewsverao.BlogListView.as_view(),name='invernonohome'),
   
  
    path('outonodetail.html', viewsoutono.BlogDetailView.as_view(), name = 'Nova Postagem'),
    path('outonohome.html', viewsoutono.BlogListView.as_view(), name = 'Nova Postagem'),
    path('outononew.html', viewsoutono.BlogCreateView.as_view(), name = 'Nova Postagem'),


    path('invernohome.html', viewsinverno.BlogListView.as_view(),name='invernonohome'),
    path('invernonew.html', viewsinverno.BlogCreateView.as_view(), name = 'Nova Postagem'),
    path('invernodetail.html', viewsinverno.BlogDetailView.as_view(), name = 'Nova Postagem'),
    path('inverno_delete.html', viewsinverno.BlogDeleteView.as_view(), name = 'Deletar'),





]

# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
