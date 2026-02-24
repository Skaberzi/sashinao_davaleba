def add_student(students, name, grades):
    students[name] = grades


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def get_grade_letter(average):
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"


def find_top_student(students):
    top_student = None
    top_average = 0

    for name, grades in students.items():
        avg = calculate_average(grades)
        if avg > top_average:
            top_average = avg
            top_student = name

    return top_student, top_average


def get_students_by_grade(students, letter):
    result = []

    for name, grades in students.items():
        avg = calculate_average(grades)
        if get_grade_letter(avg) == letter:
            result.append(name)

    return result
