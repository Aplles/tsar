from django.contrib import admin
from .models import User, HandWriting, BinaryDict, Text, Message, Room, Code, Verdict, Commandment
from .models import Question, Answer, TypeAnswer, UserAnswer, Balance, TypeQuestion, Role


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'ip_address')
    list_display_links = ('id',)
    search_fields = ('username',)
    save_on_top = True
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    ordering = ('id', 'username')
    fieldsets = [
        ("Общая информация", {'fields': ['username', 'email', 'password', 'ip_address']}),
        ('Права доступа', {'fields': ['is_superuser', 'user_permissions', 'groups', 'is_staff', 'is_active']}),
        ('Прочая информация',
         {'fields': ['last_login', 'date_joined', 'first_name', 'last_name']}),
    ]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(TypeQuestion)
class TypeQuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, ]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Verdict)
class VerdictAdmin(admin.ModelAdmin):
    pass


@admin.register(Commandment)
class CommandmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_filter = ('user',)


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
