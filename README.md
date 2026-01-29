# Online Course Django Application

A comprehensive Django application for managing online courses with exam functionality.

## Features

### Models
- **Course**: Main course container
- **Lesson**: Course subdivisions with content
- **Question**: Exam questions associated with lessons
- **Choice**: Answer options for multiple-choice questions
- **Submission**: Student exam submissions
- **SubmissionAnswer**: Individual answers within a submission

### Admin Interface
- Inline administration for nested relationships
- QuestionInline: Manage questions within lessons
- ChoiceInline: Manage choices within questions
- LessonInline: Manage lessons within courses
- QuestionAdmin: Advanced question administration
- LessonAdmin: Advanced lesson administration
- CourseAdmin: Course management

### Views
1. **submit(request, lesson_id)**: 
   - GET: Display exam questions
   - POST: Process and grade exam submissions
   
2. **show_exam_result(request, submission_id)**:
   - Display exam results with detailed feedback
   - Show correct/incorrect answers
   - Display score and passing status

3. **course_details(request, course_id)**:
   - Display full course information
   - Show all lessons with questions
   - Provide exam entry points

4. **course_list(request)**:
   - Display all available courses

### Templates
- **base.html**: Main layout with Bootstrap 5
- **course_list.html**: Course catalog
- **course_details_bootstrap.html**: Course details with questions
- **exam_submission.html**: Exam taking interface
- **exam_result.html**: Results display with detailed feedback

## Project Structure

```
online_course_project/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── online_course_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── online_course/
│   ├── migrations/
│   ├── templates/
│   │   └── online_course/
│   │       ├── course_details_bootstrap.html
│   │       ├── exam_submission.html
│   │       ├── exam_result.html
│   │       └── course_list.html
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── templates/
    └── base.html
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd online_course_project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application:
- Home: http://localhost:8000/
- Admin: http://localhost:8000/admin/

## Usage

### Creating Content in Admin

1. **Create a Course**:
   - Go to Admin > Courses
   - Click "Add Course"
   - Fill in name and description

2. **Add Lessons**:
   - Within Course admin, use LessonInline
   - Add lesson title, description, and content

3. **Add Questions**:
   - Within Lesson admin, use QuestionInline
   - Create questions with type and points

4. **Add Choices**:
   - Within Question admin, use ChoiceInline
   - Add choice text and mark correct answer

### Taking Exams

1. Navigate to Courses page
2. Click "View Course"
3. Click "Take Exam" for any lesson
4. Answer all questions
5. Click "Submit Exam"
6. View detailed results

## Models Details

### Question Model
- question_text: TextField
- question_type: Choice (Multiple Choice, True/False, Short Answer)
- points: IntegerField (default: 1)
- order: IntegerField for custom ordering
- Relationships: ForeignKey to Lesson

### Choice Model
- choice_text: TextField
- is_correct: BooleanField
- order: IntegerField
- Relationships: ForeignKey to Question

### Submission Model
- student: ForeignKey to User
- lesson: ForeignKey to Lesson
- status: Choice (IN_PROGRESS, SUBMITTED, GRADED)
- score: IntegerField (0-100, percentage)
- correct_answers: IntegerField
- total_questions: IntegerField
- submitted_at: DateTimeField
- graded_at: DateTimeField
- Unique constraint: (student, lesson)

## Admin Configuration

### Imports (7 classes)
```python
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Course, Lesson, Question, Choice, Submission, SubmissionAnswer
```

### Inline Admins
- **QuestionInline**: Manage questions in lessons
- **ChoiceInline**: Manage choices in questions
- **LessonInline**: Manage lessons in courses

### Model Admins
- **QuestionAdmin**: Custom administration for questions
- **LessonAdmin**: Custom administration for lessons

## Grading System

- Automatically calculates percentage score
- Marks each answer as correct/incorrect
- Awards points based on correct answers
- Passing score: 60%
- Allows retaking exams

## Development Notes

- Uses SQLite database for development
- Bootstrap 5 for responsive design
- Django template language for rendering
- Authentication required for exam submission
- Automatic timestamp tracking for submissions

## API Endpoints

- `GET /courses/` - List all courses
- `GET /courses/<id>/` - Course details
- `GET /lessons/<id>/submit/` - Display exam
- `POST /lessons/<id>/submit/` - Submit exam
- `GET /submissions/<id>/result/` - View results

## Security Features

- Login required for exam submissions
- User can only view their own results
- CSRF protection on forms
- Input validation
- Database transactions for submission processing

## Future Enhancements

- REST API endpoints
- Student progress tracking
- Course certificates
- Discussion forums
- Video content support
- Progress analytics dashboard

## License

MIT License - see LICENSE file for details

## Support

For issues or questions, please reach out to the development team.
