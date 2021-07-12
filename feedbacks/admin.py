from django.contrib import admin
from .models import *
import feedbacks.translation

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feedback._meta.fields]

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
