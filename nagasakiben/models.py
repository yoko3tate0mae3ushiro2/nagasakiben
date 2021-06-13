from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Dictionary(models.Model):
    written_by = models.CharField(max_length=50, verbose_name="投稿者")
    word = models.CharField(max_length=50, verbose_name="単語")
    pronunciation = models.SlugField(null=False, unique=True, verbose_name="アルファベット読み") 
    #https://docs.djangoproject.com/en/3.2/ref/models/fields/#slugfield
    meaning = models.TextField(verbose_name="意味")
    usage = models.TextField(verbose_name="用例")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="作成日")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="登録日")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.word

class Feedback(models.Model):
    dictionary = models.ForeignKey('nagasakiben.Dictionary', on_delete=models.CASCADE, related_name='feedbacks', verbose_name="コメント")
    written_by = models.CharField(max_length=50, verbose_name="コメントした人")
    feedback_content = models.TextField(verbose_name="コメント内容")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="コメント日時")
    approved_feedback = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.feedback_content

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="著者")
    title = models.CharField(max_length=100, verbose_name="記事タイトル")
    slug = models.SlugField(null=False, unique=True, verbose_name="記事スラッグ") 
    #https://docs.djangoproject.com/en/3.2/ref/models/fields/#slugfield
    content = RichTextField(blank=True, null=True, verbose_name="記事内容")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="作成日")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="投稿日")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('nagasakiben.Post', on_delete=models.CASCADE, related_name='comments', verbose_name="コメント")
    written_by = models.CharField(max_length=200, verbose_name="コメントした人")
    content = models.TextField(verbose_name="コメント内容")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="コメント日時")
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content
