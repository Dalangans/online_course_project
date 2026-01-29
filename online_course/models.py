from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Instructor(models.Model):
    """Model for storing instructor information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    bio = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Instructor: {self.user.get_full_name() or self.user.username}"

    class Meta:
        ordering = ['-created_at']


class Learner(models.Model):
    """Model for storing learner information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='learner_profile')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Learner: {self.user.get_full_name() or self.user.username}"

    class Meta:
        ordering = ['-enrollment_date']


class Course(models.Model):
    """Model for storing course information"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Lesson(models.Model):
    """Model for storing lesson information"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        indexes = [
            models.Index(fields=['course', 'order']),
        ]


class Question(models.Model):
    """Model for storing exam questions"""
    QUESTION_TYPE_CHOICES = (
        ('MC', 'Multiple Choice'),
        ('TF', 'True/False'),
        ('SA', 'Short Answer'),
    )
    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE_CHOICES, default='MC')
    points = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text[:50]

    class Meta:
        ordering = ['order']
        indexes = [
            models.Index(fields=['lesson', 'order']),
        ]


class Choice(models.Model):
    """Model for storing answer choices for questions"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice_text[:50]

    class Meta:
        ordering = ['order']


class Submission(models.Model):
    """Model for storing student exam submissions"""
    STATUS_CHOICES = (
        ('IN_PROGRESS', 'In Progress'),
        ('SUBMITTED', 'Submitted'),
        ('GRADED', 'Graded'),
    )
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_submissions')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='submissions')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='IN_PROGRESS')
    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(null=True, blank=True)
    graded_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.lesson.title}"

    class Meta:
        ordering = ['-submitted_at']
        unique_together = ('student', 'lesson')
        indexes = [
            models.Index(fields=['student', 'lesson']),
            models.Index(fields=['status', '-submitted_at']),
        ]


class SubmissionAnswer(models.Model):
    """Model for storing individual answers within a submission"""
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    points_earned = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.submission} - Q{self.question.id}"

    class Meta:
        unique_together = ('submission', 'question')
