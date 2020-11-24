from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from .models import Post
from .forms import Postform
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category

# Create your views here.

@login_required
def hello(request):
    return HttpResponse('Olá Mundo')

    
def Home_view(request, *args, **kwargs):
	return render(request, 'home.html')

def Login_View(request, *args, **kwargs):

	return render(request, 'login.html')

def New_View(request, *args, **kwargs):
	
    return render(request, 'post_new.html')

def Detail_View(request, *args, **kwargs):
	return render(request, 'post_detail.html')
  
def Edit_View(request, *args,**kwargs):
	return render(request,'post_edit.html')


# def Devocional_View(request, *args, **kwargs):
# 	return render(request, "devocionais.html")

def Verão_View(request, *args, **kwargs):
	return render(request, "verão.html")


def Outono_View(request, *args, **kwargs):
	return render(request, "outono.html")

def Inverno_View(request, *args, **kwargs):
	return render(request, "inverno.html")


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    

class BlogCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'post_new.html'
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
    template_name = 'post_edit.html'
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
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(BlogDeleteView,self).delete(request, *args, **kwargs)