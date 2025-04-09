def count_feedback_by_course(feedback_list):
    count = {}
    for fb in feedback_list:
        course = fb["course_code"]
        count[course] = count.get(course, 0) + 1
    return count

