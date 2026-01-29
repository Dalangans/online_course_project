from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.db import transaction
from .models import Course, Lesson, Question, Choice, Submission, SubmissionAnswer


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def submit(request, lesson_id):
    """
    Handle exam submission for a lesson.
    GET: Display the exam questions
    POST: Process and submit exam answers
    """
    lesson = get_object_or_404(Lesson, id=lesson_id)
    
    if request.method == 'POST':
        # Create or get existing submission
        submission, created = Submission.objects.get_or_create(
            student=request.user,
            lesson=lesson,
            defaults={'status': 'SUBMITTED'}
        )
        
        if not created and submission.status != 'IN_PROGRESS':
            return redirect('show_exam_result', submission_id=submission.id)
        
        with transaction.atomic():
            # Clear previous answers if resubmitting
            if not created:
                SubmissionAnswer.objects.filter(submission=submission).delete()
            
            submission.status = 'SUBMITTED'
            submission.submitted_at = timezone.now()
            
            # Get all questions for this lesson
            questions = Question.objects.filter(lesson=lesson)
            correct_count = 0
            total_points = 0
            earned_points = 0
            
            # Process each answer
            for question in questions:
                choice_id = request.POST.get(f'question_{question.id}')
                
                if choice_id:
                    try:
                        selected_choice = Choice.objects.get(id=choice_id)
                        is_correct = selected_choice.is_correct
                        points_earned = question.points if is_correct else 0
                        
                        if is_correct:
                            correct_count += 1
                        
                        SubmissionAnswer.objects.create(
                            submission=submission,
                            question=question,
                            selected_choice=selected_choice,
                            is_correct=is_correct,
                            points_earned=points_earned
                        )
                        
                        earned_points += points_earned
                    except Choice.DoesNotExist:
                        pass
                
                total_points += question.points
            
            # Calculate and save results
            submission.total_questions = questions.count()
            submission.correct_answers = correct_count
            
            # Calculate percentage score
            if total_points > 0:
                submission.score = int((earned_points / total_points) * 100)
            else:
                submission.score = 0
            
            submission.status = 'GRADED'
            submission.graded_at = timezone.now()
            submission.save()
        
        return redirect('show_exam_result', submission_id=submission.id)
    
    # GET request - display exam questions
    questions = Question.objects.filter(lesson=lesson).prefetch_related('choices')
    
    # Check if student already has a submission for this lesson
    existing_submission = Submission.objects.filter(
        student=request.user,
        lesson=lesson
    ).first()
    
    context = {
        'lesson': lesson,
        'questions': questions,
        'existing_submission': existing_submission,
    }
    
    return render(request, 'online_course/exam_submission.html', context)


@login_required(login_url='login')
def show_exam_result(request, submission_id):
    """
    Display the results of a submitted exam.
    Shows score, correct/incorrect answers, and detailed feedback.
    """
    submission = get_object_or_404(Submission, id=submission_id)
    
    # Ensure the user can only view their own results
    if submission.student != request.user and not request.user.is_staff:
        return redirect('course_list')
    
    # Get answers for this submission with optimized queries
    answers = SubmissionAnswer.objects.filter(submission=submission).select_related(
        'question__lesson',
        'selected_choice'
    ).prefetch_related('question__choices')
    
    # Prepare detailed results
    detailed_results = []
    for answer in answers:
        result = {
            'question': answer.question,
            'question_text': answer.question.question_text,
            'selected_choice': answer.selected_choice,
            'is_correct': answer.is_correct,
            'points_earned': answer.points_earned,
            'total_points': answer.question.points,
            'all_choices': answer.question.choices.all(),
        }
        detailed_results.append(result)
    
    # Calculate additional statistics
    total_points_possible = sum(r['total_points'] for r in detailed_results)
    total_points_earned = sum(r['points_earned'] for r in detailed_results)
    passing_score = 60  # 60% is passing score
    is_passed = submission.score >= passing_score
    
    context = {
        'submission': submission,
        'detailed_results': detailed_results,
        'total_points_possible': total_points_possible,
        'total_points_earned': total_points_earned,
        'is_passed': is_passed,
        'passing_score': passing_score,
    }
    
    return render(request, 'online_course/exam_result.html', context)


def course_details(request, course_id):
    """
    Display detailed information about a course including all lessons and their questions.
    """
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course).prefetch_related('questions__choices')
    
    context = {
        'course': course,
        'lessons': lessons,
    }
    
    return render(request, 'online_course/course_details_bootstrap.html', context)


def course_list(request):
    """Display list of all available courses"""
    courses = Course.objects.all().prefetch_related('lessons')
    
    context = {
        'courses': courses,
    }
    
    return render(request, 'online_course/course_list.html', context)
