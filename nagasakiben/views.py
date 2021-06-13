from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Dictionary, Post
from .forms import DictionaryForm, FeedbackForm, PostForm, CommentForm 
from django.views.generic.base import TemplateView
from django_pandas.io import read_frame
from django.http import HttpResponse
from django.views.generic import View


def dictionary_list(request):
    dictionaries = Dictionary.objects.filter(published_date__lte=timezone.now()).order_by('pronunciation')
    return render(request, 'nagasakiben/dictionary_list.html', {'dictionaries': dictionaries})

def dictionary_detail(request, pronunciation):
    dictionary = get_object_or_404(Dictionary, pronunciation=pronunciation)
    return render(request, 'nagasakiben/dictionary_detail.html', {'dictionary': dictionary})

def dictionary_new(request):
    if request.method == "POST":
        dictionaryform = DictionaryForm(request.POST)
        if dictionaryform.is_valid():
            dictionary = dictionaryform.save(commit=False)
            dictionary.published_date = timezone.now()
            dictionary.save()
            return redirect('dictionary_detail', pronunciation=dictionary.pronunciation)
    else:
        dictionaryform = DictionaryForm()
    return render(request, 'nagasakiben/dictionary_edit.html', {'dictionaryform': dictionaryform})

def dictionary_edit(request, pronunciation):
    dictionary = get_object_or_404(Dictionary, pronunciation=pronunciation)
    if request.method == "POST":
        dictionaryform = DictionaryForm(request.POST, instance=dictionary)
        if dictionaryform.is_valid():
            dictionary = dictionaryform.save(commit=False)
            dictionary.published_date = timezone.now()
            dictionary.save()
            return redirect('dictionary_detail', pronunciation=dictionary.pronunciation)
    else:
        dictionaryform = DictionaryForm(instance=dictionary)
    return render(request, 'nagasakiben/dictionary_edit.html', {'dictionaryform': dictionaryform})

def dictionary_feedback(request, pronunciation):
    dictionary = get_object_or_404(Dictionary, pronunciation=pronunciation)
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.dictionary = dictionary
            feedback.save()
            return redirect('dictionary_detail', pronunciation=dictionary.pronunciation)
    else:
        feedback_form = FeedbackForm()
    return render(request, 'nagasakiben/dictionary_feedback.html', {'feedback_form': feedback_form})

# def dictionary_export_csv():
#     data = Dictionary.objects.all()
#     df = read_frame(data, fieldnames=['word', 'pronunciation', 'meaning', 'usage'])
    
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=nagasakiben.csv'
#     df.to_csv(path_or_buf=response, index=False, encoding='utf-8')

#     return response

class dictionary_export_csv(View):
    def get(self, request, *args, **kwargs):
        dictionary = Dictionary.objects.all()
        df = read_frame(dictionary, fieldnames=[ 'word', 'pronunciation', 'meaning', 'usage' ])

        response = HttpResponse(content_type='text/csv; charset=utf8')
        response['Content-Disposition'] = 'attachment; filename=nagasakiben.csv'
        df.to_csv(path_or_buf=response, encoding='utf_8_sig', index=None)

        return response

class dictionary_export_csv_shiftjis(View):
    def get(self, request, *args, **kwargs):
        dictionary = Dictionary.objects.all()
        df = read_frame(dictionary, fieldnames=[ 'word', 'pronunciation', 'meaning', 'usage' ])

        response = HttpResponse(content_type='text/csv; charset=shift-jis')
        response['Content-Disposition'] = 'attachment; filename=nagasakiben.csv'
        df.to_csv(path_or_buf=response, encoding='shift_jis', index=None)

        return response


def dictionary_export(request):
    dictionaries = Dictionary.objects.all()
    return render(request, 'nagasakiben/dictionary_export.html', {'dictionaries': dictionaries})

def about(request):
    return render(request, 'nagasakiben/about.html', {})  

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searchresults = Dictionary.objects.filter(word__contains=searched)
        return render(request, 'nagasakiben/search.html', {'searched':searched, 'searchresults':searchresults})
    else:
        return render(request, 'nagasakiben/search.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'nagasakiben/post_list.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'nagasakiben/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        postform = PostForm()
    return render(request, 'nagasakiben/post_edit.html', {'postform': postform})


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        postform = PostForm(request.POST, instance=post)
        if postform.is_valid():
            post = post.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        postform = PostForm(instance=post)
    return render(request, 'nagasakiben/post_edit.html', {'postform': postform})


def post_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'nagasakiben/post_comment.html', {'comment_form': comment_form})

