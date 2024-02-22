from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.


from .models import *

class ImageInline(admin.TabularInline):
    model = ExtraBlog  # BlogImage modeliga bog'langan bo'lishi kerak
    extra = 1

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Blog, BlogPostAdmin)

# Admin User

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'country')
    list_filter = ('age', 'gender', 'country', 'liked_blogs')
    search_fields = ['user__username', 'address', 'about_yourself']

admin.site.register(UserProfile, UserProfileAdmin)

# Usefull Data

class ImageInlineUsefull(admin.TabularInline):
    model = ExtraUsefull  # BlogImage modeliga bog'langan bo'lishi kerak
    extra = 1

class UsefullPostAdmin(admin.ModelAdmin):
    inlines = [ImageInlineUsefull]

admin.site.register(UsefullData, UsefullPostAdmin)

# Others

admin.site.register(Message)
admin.site.register(VisasData)
admin.site.register(MessageUsefull)

admin.site.register(MessageUser)

admin.site.register(PopularPosts)