from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=200, unique=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "authors"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.name
        
class BookModel(models.Model):
    title = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "books"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title
        
        

