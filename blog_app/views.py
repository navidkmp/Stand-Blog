from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.views.generic import DetailView
from blog_app.models import Article, Category, Comment, Message, AboutLinks
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm


def article_detail(request, slug):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, slug=slug)
        if request.method == 'POST':
            parent_id = request.POST.get('parent_id')
            body = request.POST.get('body')
            Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
        return render(request, "blog_app/article_detail.html", {"article": article})
    else:
        return redirect('account:login')

def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog_app/articles_list.html", {"articles": objects_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog_app/articles_list.html", {"category": category, "articles": articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog_app/articles_list.html", {"articles": objects_list})


def contactus(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    return render(request, "blog_app/contactus.html", {'form': form})

def aboutus(request):
    about = AboutLinks.objects.first()
    return render(request, "blog_app/about.html", {'about': about})