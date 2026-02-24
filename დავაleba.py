math_students = {"გიორგი", "ნინო", "დავით", "ანა", "ლევან", "მარიამ", "ნიკა", "თამარ", "გიგა",
                 "სალომე", "ირაკლი", "ნათია", "ლუკა", "ელენე", "გურამ"}

physics_students = {"დავით", "ანა", "ლევან", "ირაკლი", "ნათია", "ლუკა", "ზურა", "კેથી",
                    "ბექა", "მაკა", "სოფო"}

chemistry_students = {"ლევან", "მარიამ", "ნიკა", "ლუკა", "ელენე", "გურამ", "მაკა", "ლაშა",
                      "სოფო", "ვანო", "ნანა", "თორნიკე", "დარეჯან"}

only_math = math_students - (physics_students | chemistry_students)

at_least_two = ((math_students & physics_students) |
                (math_students & chemistry_students) |
                (physics_students & chemistry_students))

subjects = {
    (len(math_students), "მათემატიკა"),
    (len(physics_students), "ფიზიკა"),
    (len(chemistry_students), "ქიმია")
}

most_popular = max(subjects)[1]

print("მხოლოდ მათემატიკა:", len(only_math), only_math)
print("მინიმუმ ორი საგანი:", len(at_least_two), at_least_two)
print("ყველაზე პოპულარული საგანი:", most_popular)