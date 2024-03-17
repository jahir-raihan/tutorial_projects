from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from rest_framework import status

from .serializers import BookSerializer



class ExampleAPIView(APIView):

    """
    Example api view for demonstrating optimization
    """

    def get(self, request):

        """
        Get all books along with authors
        """

        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True).data

        return Response({"books": serialized_books}, status=status.HTTP_200_OK)