from django.db import models


class UserQuastion(models.Model):
    issue = models.CharField(max_length=250)
    child_name = models.CharField(max_length=150)
    child_age = models.PositiveSmallIntegerField()
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.issue}-{self.child_name}-{self.phone}'


class Hint(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='hint/')
    tags = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    created = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title} - {self.author} - {self.created}'


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
    

class SmallDescription(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}-{self.created}-{self.status}'
    

class SiteHeader(models.Model):
    img = models.ImageField(upload_to='header/')
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title} - {self.created} - {self.status}'