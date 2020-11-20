from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from .modelsinverno import Post
from .formsinverno import Postform
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .modelsinverno import Category
# Create your views here.

   


# def Home_view(request, *args, **kwargs):
# 	return render(request, 'invernohome.html')

# def Inverno_New(request, *args, **kwargs):
#     return render(request, "invernonew.html")


# def Detail_View(request, *args, **kwargs):
# 	return render(request, 'post_inverno.html')



class BlogListView(ListView):
    model = Post
    template_name = 'invernohome.html'

    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_inverno.html'
    
class BlogCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'invernonew.html'
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
    template_name = 'inverno_edit.html'
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
    template_name = 'inverno_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(BlogDeleteView,self).delete(request, *args, **kwargs)