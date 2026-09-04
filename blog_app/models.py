from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify
from django.apps import apps


class Category(models.Model):
    title = models.CharField(max_length=100,)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.ManyToManyField(Category, related_name="articles")
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)
    objects = models.Manager()
    custom_manager = ArticleManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()


    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


    class Meta:
        ordering = ['-created',]


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:50]


class Message(models.Model):
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class AboutLinks(models.Model):
    github = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)



class Footer(models.Model):
    telegram = models.CharField(max_length=30)
    instagram = models.CharField(max_length=50)
    github = models.CharField(max_length=50)