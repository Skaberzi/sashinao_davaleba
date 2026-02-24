# with open("files/example.txt") as file:
#     content = file.read()
# reversed_content = content[::-1]
# with open("files/reversed.txt", "w") as file:
#     file.write(reversed_content)
# with open("files/reversed.txt") as file:
#     print(file.read())



# files = ["files/file1.txt", "files/file2.txt", "files/file3.txt"]
#
# with open("files/combined.txt", "w") as f:
#     for filename in files:
#         with open(filename, "r") as file:
#             f.write(file.read())



# students = {
#     "ლაშა": 21,
#     "მარი": 22,
#     "გიორგი": 20,
#     "თამარი": 23
# }
#
# with open("files/students.txt", "w", encoding="utf-8") as file:
#     for name, age in students.items():
#         file.write(f"{name}: {age}\n")
#
# with open("files/students.txt", encoding="utf-8") as file:
#     content = file.read()
#     print(content)





# contacts = {}
#
# with open("files/contacts.txt", encoding="utf-8") as file:
#     for line in file:
#         name, phone = line.strip().split(":")
#         contacts[name] = phone
#
# search_name = input("შეიყვანეთ ახალი მომხმარებლის სახელი >>:")
#
# if search_name in contacts:
#     print(f"{search_name}-ის ნომერია: {contacts[search_name]}")
# else:
#     new_phone = input("კონტაქტი არ წერია წიგნაკში, შეიყვანეთ ახალი ნომერი >>:")
#     contacts[search_name] = new_phone
#     print("კონტაქტი შეიქმნა")
#
#     with open("contacts.txt", "w", encoding="utf-8") as file:
#         for name, phone in contacts.items():
#             file.write(f"{name}:{phone}\n")
