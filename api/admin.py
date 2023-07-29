from django.contrib import admin
from .models import User, HandWriting, BinaryDict
from .models import Question, Answer, TypeAnswer, UserAnswer


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(HandWriting)
class HandWritingAdmin(admin.ModelAdmin):
    pass


@admin.register(BinaryDict)
class BinaryDictAdmin(admin.ModelAdmin):
    pass


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeAnswer)
class TypeAnswerAdmin(admin.ModelAdmin):
    pass
