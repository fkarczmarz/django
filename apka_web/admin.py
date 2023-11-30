from django.contrib import admin
from apka_web.models import Article
from .models import Task
# Register your models here.
admin.site.register(Article)
admin.site.register(Task)