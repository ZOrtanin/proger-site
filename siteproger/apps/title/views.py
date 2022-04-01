from django.shortcuts import render
# from .models import Article, Comment
from django.http import Http404, HttpResponse

from django.urls import reverse

def index(request):
	# latest_articles_list = Article.objects.order_by('-pub_date')[:5]
	# return render(request,'articles/list.html', {'latest_articles_list':latest_articles_list})
	return render(request,'title/resume.html', {})