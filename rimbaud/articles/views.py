from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render


from .models import Article

def index(request):
    liste_articles = Article.objects.filter(visibility=True).order_by('-pub_date')

    return render(request, 'articles/index.html', {'liste_articles': liste_articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id, visibility=True)

    return  render(request, 'articles/detail.html', {'article': article})
