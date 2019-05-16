from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pubdate'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pubdate', 'was_published_recently')
    list_filter = ['pubdate']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)