from django.http import JsonResponse
from magazine.models import Article


def get_all(request):
    result = [
        {'id': i.id, 'title': i.title}
        for i in Article.objects.all()
    ]
    return JsonResponse({'items': result})
