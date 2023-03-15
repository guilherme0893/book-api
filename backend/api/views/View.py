from rest_framework.response import Response
from rest_framework import status, generics


class ViewView(generics.GenericAPIView):
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, serializer, model):
      self.serializer_class = serializer
      self.queryset = model.objects.all()
        

    def get(self, request):
        views = self.queryset.objects.all().values_list().order_by('id')
        return Response(views)

    def post(self, request):
        view = self.serializer_class(data=request.data)
        if view.is_valid():
            view.save()
            return Response({"status": "success", "view": view.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": view.errors}, status=status.HTTP_400_BAD_REQUEST)
