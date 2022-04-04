from django.shortcuts import render
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
        # POST 요청으로 온 데이터 확인
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )    
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles':articles})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})

def category(request, category_spec):
    a = []
    if category_spec == 'none':
        category_name = '미분류'
    for article in Article.objects.all():
        if article.category == category_spec:
            a.append(article)
    return render(request, 'category.html', {'articles':a})