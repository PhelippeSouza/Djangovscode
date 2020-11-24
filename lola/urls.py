
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
   
   


    

    path('primaveraview.html', viewsprimavera.BlogCreateView.as_view(), name = 'primavera_new'),
    path('primaveradetail.html', viewsprimavera.BlogDetailView.as_view(),name='primavera_detail'),
    path('primaverahome.html', viewsprimavera.BlogListView.as_view(), name = 'primavera_home'),
    path('devocionais.html', viewsprimavera.Devocional_View, name = 'Devocional'),
    path('disciplina.html', viewsprimavera.Disciplina_View, name = 'Disciplina'),
    path('identidade.html', viewsprimavera.Identidade_View, name = 'Identidade'),
    path('proposito.html', viewsprimavera.Proposito_View, name = 'Propósito'),
    path('livros.html', viewsprimavera.Livros_View, name = 'Livros'),





   

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
