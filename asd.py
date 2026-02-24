# 1)

# nums = [1, 10, 15, 12, 7, 3, 6]
# numm = 0
#
# print(nums)
# for num in nums:
#     numm += num
#
# print("ჯამი >>:", numm)


# 2)

# nums = [1, 7, 4, 2, 7, 6, 8, 11]
# namm = 0
# print(nums)
# for num in nums:
#     if num % 2 == 0:
#         namm += 1
# print("ლუწების რაოდენობა >>:", namm)


# 3)

# words = ["კომპიუტერი", "ტელეფონი", "პლანშეტი"]
# wor = "აეიოუ"
# print(words)
# for word in words:
#     raodenoba = 0
#     for aso in word:
#         if aso in wor:
#             raodenoba += 1
#     print(f"{word}-ს ხმოვნების რაოდენობა {raodenoba}")


# 4)

first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7, 8]
common_nums = []
print(first_list)
print(second_list)
for num in first_list:
    if num in second_list:
        common_nums.append(num)

print("საერთო რიცხვები:", common_nums)