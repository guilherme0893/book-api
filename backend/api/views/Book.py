from api.models import BookModel
from api.serializers.Book import BookSerializer
from api.serializers.Book import BookSerializer
from rest_framework.response import Response
from rest_framework import status, generics


class BookView(generics.GenericAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()

    def get(self, request):
        books = BookModel.objects.all().values_list().order_by('id')
        return Response(books)

    def post(self, request):
        author = self.serializer_class(data=request.data)
        if author.is_valid():
            author.save()
            return Response({"status": "success", "book": author.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": author.errors}, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(generics.GenericAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def get_book(self, pk):
        try:
            return BookModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        author = self.get_book(pk=pk)
        if author == None:
            return Response({"status": "fail", "message": f"Book with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(author)
        return Response({"status": "success", "author": serializer.data})

    def patch(self, request, pk):
        book = self.get_book(pk)
        if book == None:
            return Response({"status": "fail", "message": f"Book with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            book, data=request.data, partial=True)
        if serializer.is_valid():
            # serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "book": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_book(pk)
        if book == None:
            return Response({"status": "fail", "message": f"Book with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

