from django.urls import path
from . import views
from nagasakiben.views import dictionary_export_csv, dictionary_export_csv_shiftjis

urlpatterns = [
    path('', views.dictionary_list, name='dictionary_list'),
    path('dictionary/about/', views.about, name='about'),
    path('dictionary/search/', views.search, name='search'),
    path('dictionary/new/', views.dictionary_new, name='dictionary_new'),
    path('dictionary/export/csv', dictionary_export_csv.as_view(), name="dictionary_export_csv"),
    path('dictionary/export/shiftjis', dictionary_export_csv_shiftjis.as_view(), name="dictionary_export_csv_shiftjis"),
    path('dictionary/export/', views.dictionary_export, name='dictionary_export'),
    path('dictionary/<slug:pronunciation>/edit/', views.dictionary_edit, name='dictionary_edit'),
    path('dictionary/<slug:pronunciation>/feedback/', views.dictionary_feedback, name='dictionary_feedback'),
    path('dictionary/<slug:pronunciation>/', views.dictionary_detail, name='dictionary_detail'),
    path('blog/post_list/', views.post_list, name='post_list'),
    path('blog/new/', views.post_new, name='post_new'),
    path('blog/<slug:slug>/comment/', views.post_comment, name='post_comment'),
    path('blog/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]