# Development Guide - Online Course Platform

## Quick Start Guide

### 1. Initial Setup

#### On Linux/Mac:
```bash
chmod +x setup.sh
./setup.sh
```

#### On Windows:
```bash
setup.bat
```

### 2. Manual Setup (if scripts don't work)

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
# Enter username: admin
# Enter email: admin@example.com
# Enter password: (choose a password)

# Start development server
python manage.py runserver
```

### 3. Access the Application

- **Frontend**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

---

## Creating Sample Course Data

### Via Django Admin

1. **Navigate to Admin Panel**
   - URL: http://localhost:8000/admin/
   - Login with your superuser credentials

2. **Create a Course**
   - Click "Courses" → "Add Course"
   - Fill in:
     - Name: "Python Basics"
     - Description: "Learn Python fundamentals"
   - Click "Save"

3. **Add Lessons**
   - In the Course page, scroll to "Lessons" section
   - Click "Add Another Lesson"
   - Fill in:
     - Title: "Introduction to Python"
     - Description: "Getting started with Python"
     - Content: "Python is a high-level programming language..."
     - Order: 1
   - Add another lesson similarly

4. **Add Questions**
   - In the Lesson admin page, scroll to "Questions" section
   - Click "Add Another Question"
   - Fill in:
     - Question Text: "What is Python?"
     - Question Type: "Multiple Choice"
     - Points: 5
     - Order: 1

5. **Add Choices**
   - In the Question admin page, scroll to "Choices" section
   - Add choices with at least one marked as "Correct"
   - Examples:
     - "A programming language" ✓ (mark as correct)
     - "A snake"
     - "A library"

### Via Django Shell

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
from online_course.models import Course, Lesson, Question, Choice

# Create a course
course = Course.objects.create(
    name="Advanced Django",
    description="Master Django web development"
)

# Create lessons
lesson = Lesson.objects.create(
    course=course,
    title="Django Models",
    description="Understanding Django ORM",
    content="Django ORM is powerful...",
    order=1
)

# Create questions
question = Question.objects.create(
    lesson=lesson,
    question_text="What is a Django Model?",
    question_type="MC",
    points=10,
    order=1
)

# Create choices
Choice.objects.create(
    question=question,
    choice_text="A representation of database table",
    is_correct=True,
    order=1
)

Choice.objects.create(
    question=question,
    choice_text="A Python module",
    is_correct=False,
    order=2
)

# Exit shell
exit()
```

---

## Testing the Application

### 1. Take an Exam

1. Navigate to http://localhost:8000/
2. Click "View Course"
3. Click "Take Exam" on a lesson with questions
4. Answer all questions
5. Click "Submit Exam"
6. View your results on the results page

### 2. Run Unit Tests

```bash
python manage.py test online_course
```

### 3. Run Specific Test

```bash
python manage.py test online_course.tests.CourseModelTest
```

---

## File Structure Explained

### Models (models.py)

**Course**
- Stores course information
- Has many Lessons

**Lesson**
- Stores lesson content
- Belongs to Course
- Has many Questions

**Question**
- Stores exam questions
- Belongs to Lesson
- Has many Choices

**Choice**
- Stores answer options
- Belongs to Question

**Submission**
- Stores student exam submissions
- Tracks score and status
- Unique per (student, lesson)

**SubmissionAnswer**
- Stores individual answers
- Part of a Submission

### Views (views.py)

**submit(request, lesson_id)**
- GET: Display exam questions form
- POST: Process answers and calculate score
- Automatically grades the exam

**show_exam_result(request, submission_id)**
- Display exam results with detailed feedback
- Show correct answers
- Display score and passing status

**course_details(request, course_id)**
- Display full course information
- Show all lessons and questions (preview only)

**course_list(request)**
- Display all available courses

### Admin Configuration (admin.py)

**Inlines**
- QuestionInline: Manage questions within lessons
- ChoiceInline: Manage choices within questions
- LessonInline: Manage lessons within courses

**Model Admins**
- QuestionAdmin: Advanced question management
- LessonAdmin: Advanced lesson management
- CourseAdmin: Course management

### URL Routing (urls.py)

| URL | View | Purpose |
|-----|------|---------|
| `/courses/` | course_list | List all courses |
| `/courses/<id>/` | course_details | View course details |
| `/lessons/<id>/submit/` | submit | Take exam / Submit answers |
| `/submissions/<id>/result/` | show_exam_result | View exam results |

### Templates

**base.html**
- Main layout
- Navigation bar
- Footer

**course_list.html**
- Displays all courses
- Course cards with links

**course_details_bootstrap.html**
- Full course information
- Shows lessons and questions
- "Take Exam" button

**exam_submission.html**
- Exam form
- Radio buttons for choices
- Form validation

**exam_result.html**
- Score display
- Detailed answer feedback
- Congratulations message for passing

---

## Common Tasks

### Creating Users

```bash
python manage.py createsuperuser

# Or via shell:
python manage.py shell
from django.contrib.auth.models import User
User.objects.create_user(username='john', email='john@example.com', password='pass123')
exit()
```

### Running Migrations

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# See migration status
python manage.py showmigrations
```

### Database Management

```bash
# Create database backup
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json

# Reset database completely
rm db.sqlite3
python manage.py migrate
```

### Debugging

```bash
# Enable verbose output
python manage.py runserver --verbosity 2

# Enable debug mode (check settings.py)
# DEBUG = True (already enabled in development)
```

---

## Deployment Checklist

Before deploying to production:

- [ ] Set DEBUG = False in settings.py
- [ ] Set SECRET_KEY to a strong random value
- [ ] Configure allowed hosts
- [ ] Set up proper database (PostgreSQL recommended)
- [ ] Configure static files collection
- [ ] Set up proper media file handling
- [ ] Enable HTTPS
- [ ] Configure email backend
- [ ] Set up logging
- [ ] Run security checks: `python manage.py check --deploy`
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Create database backups
- [ ] Set up monitoring and error tracking

---

## Troubleshooting

### Port Already in Use

```bash
# On Linux/Mac
lsof -i :8000
kill -9 <PID>

# On Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use different port
python manage.py runserver 8001
```

### Database Locked

```bash
rm db.sqlite3
python manage.py migrate
```

### Static Files Not Loading

```bash
python manage.py collectstatic --noinput
```

### Module Not Found

```bash
# Ensure virtual environment is activated
which python  # Should show path in venv directory

# Reinstall requirements
pip install -r requirements.txt
```

---

## Additional Resources

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Bootstrap Documentation: https://getbootstrap.com/docs/
- Font Awesome Icons: https://fontawesome.com/

---

## Contact & Support

For issues or feature requests, please open an issue on the project repository.
