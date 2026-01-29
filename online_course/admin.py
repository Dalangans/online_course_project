from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Course, Lesson, Question, Choice, Submission, SubmissionAnswer


class QuestionInline(admin.TabularInline):
    """Inline admin for Questions within a Lesson"""
    model = Question
    extra = 1
    fields = ['question_text', 'question_type', 'points', 'order']
    ordering = ['order']


class ChoiceInline(admin.TabularInline):
    """Inline admin for Choices within a Question"""
    model = Choice
    extra = 1
    fields = ['choice_text', 'is_correct', 'order']
    ordering = ['order']


class LessonInline(admin.TabularInline):
    """Inline admin for Lessons within a Course"""
    model = Lesson
    extra = 1
    fields = ['title', 'description', 'order']
    ordering = ['order']


class QuestionAdmin(admin.ModelAdmin):
    """Admin interface for Question model"""
    list_display = ['question_text', 'lesson', 'question_type', 'points', 'order']
    list_filter = ['question_type', 'lesson', 'created_at']
    search_fields = ['question_text', 'lesson__title']
    ordering = ['lesson', 'order']
    inlines = [ChoiceInline]
    fieldsets = (
        ('Question Information', {
            'fields': ['lesson', 'question_text', 'question_type']
        }),
        ('Points and Order', {
            'fields': ['points', 'order']
        }),
    )


class LessonAdmin(admin.ModelAdmin):
    """Admin interface for Lesson model"""
    list_display = ['title', 'course', 'order', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'content', 'course__name']
    ordering = ['course', 'order']
    inlines = [QuestionInline]
    fieldsets = (
        ('Lesson Information', {
            'fields': ['course', 'title', 'order']
        }),
        ('Content', {
            'fields': ['description', 'content']
        }),
    )


class CourseAdmin(admin.ModelAdmin):
    """Admin interface for Course model"""
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']
    inlines = [LessonInline]
    fieldsets = (
        ('Course Information', {
            'fields': ['name', 'description']
        }),
    )


class SubmissionAnswerInline(admin.TabularInline):
    """Inline admin for Submission Answers within a Submission"""
    model = SubmissionAnswer
    extra = 0
    fields = ['question', 'selected_choice', 'is_correct', 'points_earned']
    readonly_fields = ['question', 'selected_choice', 'is_correct', 'points_earned']
    can_delete = False


class SubmissionAdmin(admin.ModelAdmin):
    """Admin interface for Submission model"""
    list_display = ['student', 'lesson', 'status', 'score', 'correct_answers', 'submitted_at']
    list_filter = ['status', 'lesson', 'submitted_at', 'created_at']
    search_fields = ['student__username', 'lesson__title']
    ordering = ['-submitted_at']
    readonly_fields = ['student', 'lesson', 'score', 'correct_answers', 'total_questions', 'submitted_at', 'graded_at', 'created_at', 'updated_at']
    inlines = [SubmissionAnswerInline]
    fieldsets = (
        ('Submission Information', {
            'fields': ['student', 'lesson', 'status']
        }),
        ('Results', {
            'fields': ['score', 'correct_answers', 'total_questions']
        }),
        ('Timestamps', {
            'fields': ['submitted_at', 'graded_at', 'created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    )


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission, SubmissionAdmin)
