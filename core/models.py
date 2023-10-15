from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    favicon = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=250, blank=True)
    color_status = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.description}'
    

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    
    def get_first_paragraph(self):
        first_paragraph = self.content.split('.')

        if first_paragraph:
            return first_paragraph[0]+'.'
        else:
            return ""
    
    

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
    

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='films/')
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title