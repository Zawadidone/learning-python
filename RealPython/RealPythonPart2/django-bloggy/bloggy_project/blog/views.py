# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render, get_object_or_404, redirect

# import models
from blog.models import Post
from blog.forms import PostForm


# helper functions


def get_popular_posts():
    popular_posts = Post.objects.filter()  # filter by views => 5
    return popular_posts


# Create your views here.


def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    popular_posts = get_popular_posts()
    t = loader.get_template('index.html')
    c = {
        'latest_posts': latest_posts,
        'popular_posts': popular_posts,
    }
    return HttpResponse(t.render(c))


def post(request, title):
    single_post = get_object_or_404(Post, title=title)
    single_post.views += 1  # increment the number of views
    single_post.save()  # and save it
    t = loader.get_template('post.html')
    c = {'single_post': single_post}
    return HttpResponse(t.render(c))


def delete_post(request, title):
    Post.objects.filter(title=title).delete()
    return redirect('index')


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # is the form valid
            form.save(commit=True)  # yes? save to database
            return post(None, form.cleaned_data['title'])
        else:
            print(form.errors)  # no? display errors to end user
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})
