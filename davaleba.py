# users = [
#     {"id": 1, "name": "ნუგო"},
#     {"id": 2, "age": 21},
#     {"id": 1, "age": 30},
#     {"id": 3, "name": "ხრუსტალი"},
#     {"id": 2, "name": "ზალიკო"} ]
#
# shedegi = {}
#
# for user in users:
#     user_id = user["id"]
#
#     if user_id not in shedegi:
#         shedegi[user_id] = {}
#
#     for key in user:
#         shedegi[user_id][key] = user[key]
#
# print(users)
# print(shedegi)
#
#
# categories = {
#     "ხილი": ["ვაშლი", "ბანანი"],
#     "ბოსტნეული": ["სტაფილო", "ხახვი"],
#     "საკონდიტრო": ["ბანანი", "ტორტი"] }
#
# inverted = {}
#
# for category, nivtebi in categories.items():
#     for nivti in nivtebi:
#         if nivti not in inverted:
#             inverted[nivti] = []
#         inverted[nivti].append(category)
#
# print(categories)
# print(inverted)

