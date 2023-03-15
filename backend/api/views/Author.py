from rest_framework.response import Response
from rest_framework import status, generics
from api.models import AuthorModel
from api.serializers.Author import AuthorSerializer
from datetime import datetime


class AuthorView(generics.GenericAPIView):
    serializer_class = AuthorSerializer
    queryset = AuthorModel.objects.all()

    def get(self, request):
        authors = AuthorModel.objects.all().values_list().order_by('id')
        return Response(authors)

    def post(self, request):
        author = self.serializer_class(data=request.data)
        if author.is_valid():
            author.save()
            return Response({"status": "success", "author": author.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": author.errors}, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetailView(generics.GenericAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

    def get_author(self, pk):
        try:
            return AuthorModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        author = self.get_author(pk=pk)
        if author == None:
            return Response({"status": "fail", "message": f"Author with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(author)
        return Response({"status": "success", "author": serializer.data})

    def patch(self, request, pk):
        author = self.get_author(pk)
        if author == None:
            return Response({"status": "fail", "message": f"Author with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            author, data=request.data, partial=True)
        if serializer.is_valid():
            # serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "author": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_author(pk)
        if author == None:
            return Response({"status": "fail", "message": f"Author with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
