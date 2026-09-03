from blog_app.models import Article, Category, Footer

def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')
    categories = Category.objects.all()
    return {'recent_articles': recent_articles, 'categories': categories}

def footer_links(request):
    footer = Footer.objects.first()
    return {'footer': footer}