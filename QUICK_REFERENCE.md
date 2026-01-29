# Quick Reference Guide

## File Locations for Evaluation Criteria

### For AI-Graded Submission (Option 1)

You will need to provide GitHub URLs to these specific files:

#### 1. **models.py** (3 points)
📄 **Path**: `online_course/models.py`
- Contains: Question, Choice, Submission models
- Additional: Course, Lesson, SubmissionAnswer models
- Key features:
  - Question model with question_type choices
  - Choice model with is_correct boolean
  - Submission model with score tracking
  - SubmissionAnswer model for detailed tracking

#### 2. **admin.py** (3 points)
📄 **Path**: `online_course/admin.py`
- Contains: 7 imported classes
  1. admin (Django)
  2. User (Django auth)
  3. UserAdmin (Django auth)
  4. Course model
  5. Lesson model
  6. Question model
  7. Choice model

- Implementations included:
  - QuestionInline: For managing questions in lessons
  - ChoiceInline: For managing choices in questions
  - LessonInline: For managing lessons in courses
  - QuestionAdmin: Advanced question management
  - LessonAdmin: Advanced lesson management

#### 3. **course_details_bootstrap.html** (2 points)
📄 **Path**: `online_course/templates/course_details_bootstrap.html`
- Uses Django template tags
- Shows course name
- Displays all related lessons
- Displays all questions and choices
- Bootstrap styling

#### 4. **views.py** (2 points)
📄 **Path**: `online_course/views.py`
- Contains:
  - `submit(request, lesson_id)` function
  - `show_exam_result(request, submission_id)` function
  - Additional views: course_details, course_list

#### 5. **urls.py** (2 points)
📄 **Path**: `online_course/urls.py`
- Contains paths:
  - `'lessons/<int:lesson_id>/submit/'` → submit
  - `'submissions/<int:submission_id>/result/'` → show_exam_result
  - Additional paths for courses

#### 6. **Screenshot: Admin Site** (1 point)
📸 **How to generate**:
1. Run: `python manage.py runserver`
2. Go to: http://localhost:8000/admin/
3. Login with superuser credentials
4. Take screenshot showing:
   - "Authentication and Authorization" section
   - "OnlineCourse" section with all models
5. Save as: `03-admin-site.png`

#### 7. **Screenshot: Final Exam Result** (2 points)
📸 **How to generate**:
1. Create sample data: `python manage.py create_sample_data`
2. Go to: http://localhost:8000/
3. Take the exam
4. Submit answers
5. Take screenshot showing:
   - "Congratulations" message
   - Score percentage
   - Exam results and detailed feedback
6. Save as: `07-final.png`

---

## For Peer-Graded Submission (Option 2)

You need to provide screenshots for:

1. **01-models.png** - models.py file content
2. **02-admin-file.png** - admin.py file content
3. **03-admin-site.png** - Admin panel screenshot
4. **04-course-details.png** - course_details_bootstrap.html file content
5. **05-views.png** - views.py file content
6. **06-urls.png** - urls.py file content
7. **07-final.png** - Mock exam result screenshot

---

## Quick Commands Reference

### Initial Setup
```bash
# Windows
setup.bat

# Linux/Mac
chmod +x setup.sh
./setup.sh
```

### Manual Setup
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py create_sample_data
python manage.py runserver
```

### Access Application
- Frontend: http://localhost:8000/
- Admin: http://localhost:8000/admin/

### Run Tests
```bash
python manage.py test online_course
```

---

## Key Features Summary

### Models
✅ Question - Exam questions
✅ Choice - Answer options
✅ Submission - Student submissions
✅ SubmissionAnswer - Individual answers

### Admin Features
✅ Inline administration
✅ QuestionInline
✅ ChoiceInline
✅ LessonInline
✅ QuestionAdmin
✅ LessonAdmin

### Views
✅ submit - Take/submit exams
✅ show_exam_result - Display results
✅ course_details - Course information
✅ course_list - All courses

### Templates
✅ course_details_bootstrap.html
✅ exam_submission.html
✅ exam_result.html
✅ course_list.html
✅ base.html

### Functionality
✅ Automatic grading
✅ Score calculation
✅ Passing threshold (60%)
✅ Detailed feedback
✅ Congratulations message
✅ User authentication
✅ Responsive design

---

## File Structure (Essential Files Only)

```
online_course_project/
├── manage.py
├── requirements.txt
├── README.md
├── DEVELOPMENT.md
├── PROJECT_SUMMARY.md
├── setup.sh / setup.bat
│
├── online_course/
│   ├── migrations/
│   ├── templates/online_course/
│   │   ├── course_details_bootstrap.html ⭐
│   │   ├── exam_submission.html
│   │   ├── exam_result.html
│   │   └── course_list.html
│   ├── admin.py ⭐
│   ├── models.py ⭐
│   ├── views.py ⭐
│   └── urls.py ⭐
│
└── templates/
    └── base.html
```

⭐ = Required for evaluation

---

## Submission Checklist

### Option 1 (AI-Graded)
- [ ] GitHub repository created and public
- [ ] models.py URL copied
- [ ] admin.py URL copied
- [ ] course_details_bootstrap.html URL copied
- [ ] views.py URL copied
- [ ] urls.py URL copied
- [ ] Admin site screenshot (03-admin-site.png)
- [ ] Exam result screenshot (07-final.png)

### Option 2 (Peer-Graded)
- [ ] 01-models.png screenshot
- [ ] 02-admin-file.png screenshot
- [ ] 03-admin-site.png screenshot
- [ ] 04-course-details.png screenshot
- [ ] 05-views.png screenshot
- [ ] 06-urls.png screenshot
- [ ] 07-final.png screenshot

---

## Grading Points Breakdown

| Item | Points | File/Screenshot |
|------|--------|-----------------|
| Models | 3 | models.py |
| Admin Configuration | 3 | admin.py |
| Admin Site Screenshot | 1 | 03-admin-site.png |
| Course Details Template | 2 | course_details_bootstrap.html |
| Views Functions | 2 | views.py |
| URL Paths | 2 | urls.py |
| Exam Result Screenshot | 2 | 07-final.png |
| **TOTAL** | **15** | - |

---

## Screenshot Guidelines

### Admin Site Screenshot (03-admin-site.png)
- Show "Django administration" header
- Show "Authentication and Authorization" section
- Show "OnlineCourse" section
- Show all registered models (Course, Lesson, Question, Choice, Submission)

### Exam Result Screenshot (07-final.png)
- Show "Congratulations" message (indicates passing)
- Show score in percentage (e.g., "85%")
- Show "Correct Answers" count
- Show exam results/feedback
- Can show quiz or difficulty with correct answers clearly marked

---

## Troubleshooting

### Port 8000 already in use
```bash
python manage.py runserver 8001
```

### Database error
```bash
rm db.sqlite3
python manage.py migrate
```

### Import errors
```bash
pip install -r requirements.txt
```

### Admin won't load
```bash
python manage.py createsuperuser
```

---

## Documentation Files Included

- **README.md** - Main documentation
- **DEVELOPMENT.md** - Developer guide with examples
- **PROJECT_SUMMARY.md** - Complete project overview
- **QUICK_REFERENCE.md** - This file

---

## Contact Points in Code

Look for these functions in your submission:

### views.py
```python
def submit(request, lesson_id):
    # Handles exam submission and grading

def show_exam_result(request, submission_id):
    # Displays exam results with feedback
```

### admin.py
```python
class QuestionInline(admin.TabularInline):
class ChoiceInline(admin.TabularInline):
class LessonInline(admin.TabularInline):
class QuestionAdmin(admin.ModelAdmin):
class LessonAdmin(admin.ModelAdmin):
```

### models.py
```python
class Question(models.Model):
class Choice(models.Model):
class Submission(models.Model):
```

---

## Success Indicators

✅ All 15 points achievable
✅ All requirements met
✅ Code is clean and documented
✅ Application is fully functional
✅ Responsive design with Bootstrap
✅ Automatic grading system works
✅ Screenshots show expected output

---

**Ready for Submission!** 🎉
