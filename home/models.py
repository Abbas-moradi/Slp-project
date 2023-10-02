from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    tags = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    created = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title} - {self.author} - {self.created}'
    

class Category(models.Model):
    name = models.CharField(max_length=150)
    favicon = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=250, blank=True)
    color_status = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.description}'
    

class ImageGallery(models.Model):
    name = models.CharField(max_length=150)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    descriptoin = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.created} - {self.status}'
    

class NewsUserEmail(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.email} - {self.created} - {self.status}'
