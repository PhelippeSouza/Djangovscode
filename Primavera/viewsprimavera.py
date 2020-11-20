from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from .modelsprimavera import Post
from .primaveraforms import Postform
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .modelsprimavera import Post, Category
# Create your views here.


    
def Primavera_view(request, *args, **kwargs):
	return render(request, 'primavera_new.html')



class BlogListView(ListView):
    model = Post
    template_name = 'primavera_home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'primaveradetail.html'
    
    

class BlogCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'primavera_new.html'
    form_class = Postform
    success_message = "%(field)s - criado com sucesso"

    Category = (
        ('Primavera','Verão'),
        ('Outono','Inverno'),
    )

  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Post
    form_class = Postform
    template_name = 'primavera_edit.html'
    fields = ('titulo','conteudo')
    success_message = "%(field)s - alterado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'primavera_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(BlogDeleteView,self).delete(request, *args, **kwargs)