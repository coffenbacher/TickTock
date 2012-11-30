# Create your views here.
from django.shortcuts import render_to_response
from models import *

def index(request):
    posts = BlogPost.objects.all()
    return render_to_response('blog/index.html' , {'posts': posts})
