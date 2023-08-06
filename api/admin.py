from django.contrib import admin
from .models import User, HandWriting, BinaryDict, Text, Message
from .models import Question, Answer, TypeAnswer, UserAnswer, Balance


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass


class AnswerCurrentFilter(admin.SimpleListFilter):
    title = 'Ответы'
    parameter_name = 'is_current'
    field_name = 'is_current'

    def lookups(self, request, model_admin):
        dict_answer = {
            True: "Верные",
            False: "Не верные",
        }
        for key, value in dict_answer.items():
            yield key, value

    def queryset(self, request, queryset):
        is_current = self.value()
        if is_current:
            return queryset.filter(answer__is_current=is_current)
        return queryset


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_filter = ('user', AnswerCurrentFilter)


@admin.register(HandWriting)
class HandWritingAdmin(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(BinaryDict)
class BinaryDictAdmin(admin.ModelAdmin):
    pass


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]
    list_filter = ('type_question',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeAnswer)
class TypeAnswerAdmin(admin.ModelAdmin):
    pass
