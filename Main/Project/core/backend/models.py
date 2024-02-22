from django.db import models

# Create your models here.

# Extra Liblaries

# Blog model
from django.urls import reverse

from django.contrib.auth.models import User

class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_blogs = models.ManyToManyField('Blog', blank=True)
    
    age = models.IntegerField(choices=[
        (0, 'Select Age Range'),
        (1, '9 - 16'),
        (2, '17 - 22'),
        (3, '23 - 28'),
        (4, '29 - 35'),
        (5, '36 - 40'),
        (6, '41 - 55'),
        (7, '55 and above'),
    ], default=0, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ], blank=True)
    country = models.CharField(max_length=2, choices=[
        ('UZ', 'Uzbekistan'),
        ('DE', 'Germany'),
        ('IN', 'India'),
        ('CN', 'China'),
        ('GB', 'United Kingdom'),
    ], blank=True)
    address = models.CharField(max_length=255, blank=True)
    about_yourself = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    # images = models.ImageField(upload_to='backend/static/Home/Assets/Images/BlogImages')
    photo = models.ImageField(upload_to='static/Home/Assets/Images/BlogImages', default='backend/static/Home/Assets/Images/BlogImages/germanyDefaultImages.jpg')
    description_f_body = models.TextField(null=False, blank=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255)

    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.title)

    
    def get_absolute_url(self):
        # Bu metod orqali har bir blog post uchun unikal URL qaytariladi
        return reverse('blog-detail', args=[str(self.id)])
    
    
class ExtraBlog(models.Model):
    post = models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/Home/Assets/Images/BlogImages', null=True, blank=True)
    description = models.TextField(null=True)

    link_name = models.CharField(max_length=255, null=True, blank=True)
    link_address = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.post.title
    
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    

class UsefullData(models.Model):
    title = models.CharField(max_length=255)
    # images = models.ImageField(upload_to='backend/static/Home/Assets/Images/BlogImages')
    photo = models.ImageField(upload_to='static/Home/Assets/Images/BlogImages', default='backend/static/Home/Assets/Images/BlogImages/germanyDefaultImages.jpg')
    description_f_body = models.TextField(null=False, blank=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255)

    likes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.title)
    
    # def get_absolute_url(self):
    #     # Bu metod orqali har bir useful data post uchun unikal URL qaytariladi
    #     return reverse('usefuldata-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Usefull"
        verbose_name_plural = "Usefull Datas"
        # translatable_fields = ("description", "tags")
    

class ExtraUsefull(models.Model):
    post = models.ForeignKey(UsefullData, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/Home/Assets/Images/BlogImages', null=True, blank=True)
    description = models.TextField(null=True)

    link_name = models.CharField(max_length=255, null=True, blank=True)
    link_address = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.post.title
    

class MessageUsefull(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(UsefullData, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    
    

class VisasData(models.Model):
    title = models.CharField(max_length=255)
    colors = models.CharField(max_length=255, null=True, choices=[('Blue', 'Blue'),
        ('Purple', 'Purple'), ('Yellow', 'Yellow'), ('Pink', 'Pink')])
    images = models.ImageField(upload_to='static/Home/Assets/Images/BlogImages')
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)


class MessageUser(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.name
    

class PopularPosts(models.Model):
    address = models.URLField(null=True, blank=True)
    images = models.ImageField(upload_to='static/Home/Assets/Images/BlogImages')

    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address