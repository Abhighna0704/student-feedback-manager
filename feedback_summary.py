def summarize_feedback(feedback_list):
    summary = {}
    for feedback in feedback_list:
        course = feedback["course_code"]
        summary.setdefault(course, []).append(feedback["score"])
    return {course: sum(scores)/len(scores) for course, scores in summary.items()}

