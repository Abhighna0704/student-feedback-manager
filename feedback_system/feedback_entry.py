def add_feedback(student_id, course_code, feedback_text, score):
    feedback = {
        "student_id": student_id,
        "course_code": course_code,
        "feedback_text": feedback_text,
        "score": score
    }
    return feedback

