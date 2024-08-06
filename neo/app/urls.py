from django.urls import path
from rest_framework.views import APIView
from django.contrib.auth import views as auth_views
from .views import *  
from . import views

urlpatterns = [


    #toutes les apis fonctionnes avec angular for exemple http://127.0.0.1:8000/app/*****
    path('create_author', AuthorCreateView.as_view(), name='create_author'),
    path('AuthorListView', AuthorListView.as_view(), name='AuthorListView'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
#/***************************************

    path('BookCreateView', BookCreateView.as_view(), name='BookCreateView'),
    path('BookListView', BookListView.as_view(), name='BookListView'),
    path('BookDetailView/<int:pk>/', BookDetailView.as_view(), name='BookDetailView-detail'),
    path('BookDetailView2/<str:isbn>/', BookDetailView2.as_view(), name='BookDetailView-detail'),
#/***************************************

    path('GenreCreateView', GenreCreateView.as_view(), name='GenreCreateView'),
    path('GenreListView', GenreListView.as_view(), name='GenreListView'),
    path('GenreDetailView/<int:pk>/', GenreDetailView.as_view(), name='GenreDetailView-detail'),
#/***************************************

    path('BookInstanceCreateView', BookInstanceCreateView.as_view(), name='BookInstanceCreateView'),
    path('BookInstanceListView', BookInstanceListView.as_view(), name='BookInstanceListView'),
    path('BookInstanceDetailView/<int:pk>/', BookInstanceDetailView.as_view(), name='BookInstanceDetailView-detail'),
#/***************************************



#si en veut voire avec les interfaces

    path('liste4',Book2_all_view.as_view(),name="index"),
    path('liste1',auth2_all_view.as_view,name="liste"),
    path('liste2',genre2_all_view.as_view,name="liste"),
    path('liste3',inst2_all_view.as_view,name="liste"),
    path('create_author', AuthorCreateView2.as_view(), name='create_author'),
    path('', AuthorListView2.as_view(), name='AuthorListView'),
    path('authors/<int:pk>/', AuthorDetailView2.as_view(), name='author-detail'),
#/***************************************

    path('BookCreateView', BookCreateView2.as_view(), name='BookCreateView'),
    path('BookDetailView/<int:pk>/', BookDetailView2.as_view(), name='BookDetailView-detail'),
    path('BookDetailView2/<str:isbn>/', BookDetailView22.as_view(), name='BookDetailView-detail'),
#/***************************************

    path('GenreCreateView', GenreCreateView2.as_view(), name='GenreCreateView'),
    path('', GenreListView2.as_view(), name='GenreListView'),
    path('GenreDetailView/<int:pk>/', GenreDetailView2.as_view(), name='GenreDetailView-detail'),
#/***************************************

    path('BookInstanceCreateView', BookInstanceCreateView2.as_view(), name='BookInstanceCreateView'),
    path('', BookInstanceListView2.as_view(), name='BookInstanceListView'),
    path('BookInstanceDetailView/<int:pk>/', BookInstanceDetailView2.as_view(), name='BookInstanceDetailView-detail'),
#/***************************************



]
