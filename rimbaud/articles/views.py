from django.http import HttpResponse
from django.http.response import JsonResponse
from django.template import loader

from django.shortcuts import get_object_or_404, render

from .models import Article


def index(request):
    latest_article_list = Article.objects.filter(visibility=True).order_by('-pub_date')
    template = loader.get_template('articles/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }

    if request.is_ajax():
        url_parameter = request.GET.get("q")

        latest_article_list = Article.objects.all().filter(pk__startswith=url_parameter)

        html = loader.render_to_string(
            template_name="articles/_articles_results.html",
            context={"latest_article_list": latest_article_list}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return HttpResponse(template.render(context, request))


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})


def results(request, article_id):
    response = "You're looking at the results of article %s."
    return HttpResponse(response % article_id)
