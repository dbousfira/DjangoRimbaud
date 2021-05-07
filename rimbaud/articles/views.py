from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from datetime import datetime

from .models import Article


def index(request):
    latest_article_list = Article.objects.filter(
        visibility=True,
        pub_date__gt=datetime.now()
    ).order_by('-pub_date')

    if request.is_ajax():
        url_parameter = request.GET.get("q")

        latest_article_list = Article.objects.all().filter(
            pk__startswith=url_parameter,
            visibility=True,
            pub_date__gt=datetime.now()
        )
        html = loader.render_to_string(
            template_name="articles/_articles_results.html",
            context={"latest_article_list": latest_article_list}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'articles/index.html', {'latest_article_list': latest_article_list})


def detail(request, article_id):
    article = get_object_or_404(
        Article,
        pk=article_id,
        visibility=True,
        pub_date__gt=datetime.now()
    )
    return render(request, 'articles/detail.html', {'article': article})