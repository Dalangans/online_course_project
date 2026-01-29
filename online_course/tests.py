# Online Course App Tests
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, Lesson, Question, Choice, Submission


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Test Course',
            description='Test Description'
        )

    def test_course_creation(self):
        self.assertEqual(self.course.name, 'Test Course')
        self.assertEqual(str(self.course), 'Test Course')


class LessonModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Test Course')
        self.lesson = Lesson.objects.create(
            course=self.course,
            title='Test Lesson',
            description='Test',
            content='Test Content'
        )

    def test_lesson_creation(self):
        self.assertEqual(self.lesson.title, 'Test Lesson')
        self.assertEqual(self.lesson.course, self.course)


class QuestionModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Test Course')
        self.lesson = Lesson.objects.create(course=self.course, title='Test Lesson')
        self.question = Question.objects.create(
            lesson=self.lesson,
            question_text='What is 2+2?',
            points=5
        )

    def test_question_creation(self):
        self.assertEqual(self.question.question_text, 'What is 2+2?')
        self.assertEqual(self.question.points, 5)


class ChoiceModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Test Course')
        self.lesson = Lesson.objects.create(course=self.course, title='Test Lesson')
        self.question = Question.objects.create(lesson=self.lesson, question_text='Test?')
        self.choice = Choice.objects.create(
            question=self.question,
            choice_text='Option 1',
            is_correct=True
        )

    def test_choice_creation(self):
        self.assertEqual(self.choice.choice_text, 'Option 1')
        self.assertTrue(self.choice.is_correct)
