from django.shortcuts import get_object_or_404, render

from datetime import datetime

from .models import Article

def index(request):
    liste_articles = Article.objects.filter(
        visibility=True,
        pub_date__gt=datetime.now()
    ).order_by('-pub_date')

    return render(request, 'articles/index.html', {'liste_articles': liste_articles})

def detail(request, article_id):
    article = get_object_or_404(
        Article, 
        pk=article_id, 
        visibility=True, 
        pub_date__gt=datetime.now()
    )

    return  render(request, 'articles/detail.html', {'article': article})
