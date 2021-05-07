from django.http import HttpResponse

from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.article for a in latest_article_list])

    return HttpResponse(output)


def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)


def results(request, article_id):
    response = "You're looking at the results of article %s."
    return HttpResponse(response % article_id)


def vote(request, article_id):
    return HttpResponse("You're voting on article %s." % article_id)
