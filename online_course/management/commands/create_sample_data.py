from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from online_course.models import Course, Lesson, Question, Choice
from django.utils import timezone


class Command(BaseCommand):
    help = 'Create sample course data for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))

        # Create sample courses
        course1, created = Course.objects.get_or_create(
            name='Python Basics',
            defaults={'description': 'Learn the fundamentals of Python programming'}
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created course: {course1.name}'))

        course2, created = Course.objects.get_or_create(
            name='Django Web Development',
            defaults={'description': 'Master web development with Django framework'}
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created course: {course2.name}'))

        # Create lessons for course1
        lesson1, created = Lesson.objects.get_or_create(
            course=course1,
            title='Introduction to Python',
            defaults={
                'description': 'Getting started with Python',
                'content': 'Python is a high-level, interpreted programming language known for its simplicity and readability.',
                'order': 1
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created lesson: {lesson1.title}'))

        # Create questions for lesson1
        question1, created = Question.objects.get_or_create(
            lesson=lesson1,
            question_text='What is Python?',
            defaults={
                'question_type': 'MC',
                'points': 5,
                'order': 1
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created question: {question1.question_text}'))

            # Create choices for question1
            Choice.objects.create(
                question=question1,
                choice_text='A high-level programming language',
                is_correct=True,
                order=1
            )
            Choice.objects.create(
                question=question1,
                choice_text='A type of snake',
                is_correct=False,
                order=2
            )
            Choice.objects.create(
                question=question1,
                choice_text='A web framework',
                is_correct=False,
                order=3
            )

        # Create another question
        question2, created = Question.objects.get_or_create(
            lesson=lesson1,
            question_text='What is the correct way to create a list in Python?',
            defaults={
                'question_type': 'MC',
                'points': 5,
                'order': 2
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created question: {question2.question_text}'))

            Choice.objects.create(
                question=question2,
                choice_text='my_list = [1, 2, 3]',
                is_correct=True,
                order=1
            )
            Choice.objects.create(
                question=question2,
                choice_text='my_list = (1, 2, 3)',
                is_correct=False,
                order=2
            )
            Choice.objects.create(
                question=question2,
                choice_text='my_list = {1, 2, 3}',
                is_correct=False,
                order=3
            )

        # Create lesson2 for course2
        lesson2, created = Lesson.objects.get_or_create(
            course=course2,
            title='Django Models',
            defaults={
                'description': 'Understanding Django ORM and Models',
                'content': 'Django Models are the single source of truth for your data. They contain the essential fields and behaviors.',
                'order': 1
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created lesson: {lesson2.title}'))

        # Create questions for lesson2
        question3, created = Question.objects.get_or_create(
            lesson=lesson2,
            question_text='What is a Django Model?',
            defaults={
                'question_type': 'MC',
                'points': 10,
                'order': 1
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created question: {question3.question_text}'))

            Choice.objects.create(
                question=question3,
                choice_text='A Python class that represents a database table',
                is_correct=True,
                order=1
            )
            Choice.objects.create(
                question=question3,
                choice_text='A type of file in Django',
                is_correct=False,
                order=2
            )
            Choice.objects.create(
                question=question3,
                choice_text='A database query tool',
                is_correct=False,
                order=3
            )

        # Create test user if doesn't exist
        test_user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'testuser@example.com',
                'first_name': 'Test',
                'last_name': 'User'
            }
        )

        if created:
            test_user.set_password('password123')
            test_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created test user: {test_user.username}'))

        self.stdout.write(self.style.SUCCESS('\n✓ Sample data created successfully!\n'))
        self.stdout.write('You can now:')
        self.stdout.write('1. Log in to admin at http://localhost:8000/admin/')
        self.stdout.write('   Username: admin')
        self.stdout.write('2. View courses at http://localhost:8000/')
        self.stdout.write('3. Take exams to test the application')
