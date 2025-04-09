def generate_report(feedback_list):
    report_lines = ["Student Feedback Report", "-"*30]
    for fb in feedback_list:
        report_lines.append(
            f"Student: {fb['student_id']} | Course: {fb['course_code']}\n"
            f"Score: {fb['score']} | Feedback: {fb['feedback_text']}\n"
        )
    return "\n".join(report_lines)

