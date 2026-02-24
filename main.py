from student_manager import (
    add_student,
    calculate_average,
    get_grade_letter,
    find_top_student,
    get_students_by_grade)

def main():
    students = {}

    add_student(students, "ვაჟა", [90, 95, 88])
    add_student(students, "გიორგი", [70, 75, 72])
    add_student(students, "გურამი", [85, 80, 82])
    add_student(students, "ლუკა", [55, 60, 58])

    for name, grades in students.items():
        avg = calculate_average(grades)
        letter = get_grade_letter(avg)
        print(f"{name}: საშუალო = {avg}, შეფასება = {letter}")

    top_name, top_avg = find_top_student(students)
    print(f"\nსაუკეთესო სტუდენტი: {top_name} ({top_avg})")

    a_students = get_students_by_grade(students, "A")
    print("A შეფასების სტუდენტები:", a_students)


if __name__ == "__main__":
    main()