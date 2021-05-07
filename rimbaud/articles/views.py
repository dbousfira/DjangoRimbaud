from django.http import HttpResponse

from .models import Article

# def index(request):
#     liste_articles = Article.objects.order_by('pub_date')
#     output = ', '.join([q.title for q in liste_articles])
#     return HttpResponse(output)

def detail(request, article_id):
    return HttpResponse("Détail de l'article %s" % article_id)
