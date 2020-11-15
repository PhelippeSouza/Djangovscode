from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
	Titulo = models.CharField(max_length= 230)
	conteudo = RichTextField()




	


    


