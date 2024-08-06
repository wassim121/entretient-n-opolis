from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import *


#teste with postman




class AuthorCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AuthorListView(APIView):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AuthorDetailView(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****************************

class BookCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        Books = Book.objects.all()
        serializer = BookSerializer(Books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookDetailView2(APIView):
   
    def get(self, request, isbn, *args, **kwargs):
        books = Book.objects.filter(isbn=isbn)
        if not books.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(books.first()) 
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        Book = self.get_object(pk)
        if Book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(Book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def get(self, request, genre, *args, **kwargs):
        Book = Book.objects.filter(isbn=genre)
        if Book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(Book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        Book = self.get_object(pk)
        if Book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(Book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        Book = self.get_object(pk)
        if Book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****************************

class GenreCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GenreListView(APIView):
    def get(self, request, *args, **kwargs):
        Genres = Genre.objects.all()
        serializer = GenreSerializer(Genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GenreDetailView(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        Genre = self.get_object(pk)
        if Genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(Genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        Genre = self.get_object(pk)
        if Genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(Genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        Genre = self.get_object(pk)
        if Genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****************************

class BookInstanceCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookInstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookInstanceListView(APIView):
    def get(self, request, *args, **kwargs):
        BookInstances = BookInstance.objects.all()
        serializer = BookInstanceSerializer(BookInstances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookInstanceDetailView(APIView):
    def get_object(self, pk):
        try:
            return BookInstance.objects.get(pk=pk)
        except BookInstance.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        BookInstance = self.get_object(pk)
        if BookInstance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInstanceSerializer(BookInstance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        BookInstance = self.get_object(pk)
        if BookInstance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInstanceSerializer(BookInstance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        BookInstance = self.get_object(pk)
        if BookInstance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        BookInstance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#  views 
def index(request):
	return render(request, "index.html", )


def liste(request):
	return render(request, "liste.html", )









class AuthorCreateView2(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            print("ok")
            serializer.save()
            
            return render(request, 'index.html')
        return render(request, 'index.html')



class AuthorListView2(APIView):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        return render(request, 'index.html', {'authors': authors})


class AuthorDetailView2(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        author = self.get_object(pk)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****************************

class BookCreateView2(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return render(request, 'index.html')




class Book2_all_view(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        Authors = Author.objects.all()
        Genres = Genre.objects.all()
        BookInstances = BookInstance.objects.all()
        return render(request, 'liste2.html',   {'books': books})

class auth2_all_view(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        Authors = Author.objects.all()
        Genres = Genre.objects.all()
        BookInstances = BookInstance.objects.all()
        return render(request, 'liste3.html',    {'Authors': Authors})

class genre2_all_view(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        Authors = Author.objects.all()
        Genres = Genre.objects.all()
        BookInstances = BookInstance.objects.all()
        return render(request, 'liste1.html',  {'Genres': Genres})

class inst2_all_view(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        Authors = Author.objects.all()
        Genres = Genre.objects.all()
        BookInstances = BookInstance.objects.all()
        return render(request, 'liste4.html',  {'BookInstances': BookInstances})

class BookDetailView22(APIView):
   
    def get(self, request, isbn, *args, **kwargs):
        books = Book.objects.filter(isbn=isbn)
        if not books.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(books.first()) 
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailView2(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        Book = self.get_object(pk)
        if Book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(Book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def get(self, request, genre, *args, **kwargs):
        Book = Book.objects.filter(isbn=genre)
        if Book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(Book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        Book = self.get_object(pk)
        if Book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(Book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        Book = self.get_object(pk)
        if Book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****************************

class GenreCreateView2(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return render(request, 'index.html')




class GenreListView2(APIView):
    def get(self, request, *args, **kwargs):
        Genres = Genre.objects.all()
        return render(request, 'index.html', {'Genres': Genres})


class GenreDetailView2(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        Genre = self.get_object(pk)
        if Genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(Genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        Genre = self.get_object(pk)
        if Genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(Genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        Genre = self.get_object(pk)
        if Genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****************************

class BookInstanceCreateView2(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookInstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return render(request, 'index.html')






class BookInstanceListView2(APIView):
    def get(self, request, *args, **kwargs):
        BookInstances = BookInstance.objects.all()
        return render(request, 'index.html', {'BookInstances': BookInstances})


class BookInstanceDetailView2(APIView):
    def get_object(self, pk):
        try:
            return BookInstance.objects.get(pk=pk)
        except BookInstance.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        BookInstance = self.get_object(pk)
        if BookInstance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInstanceSerializer(BookInstance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        BookInstance = self.get_object(pk)
        if BookInstance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInstanceSerializer(BookInstance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        BookInstance = self.get_object(pk)
        if BookInstance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        BookInstance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

