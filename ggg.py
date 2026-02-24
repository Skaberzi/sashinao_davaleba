n = int(input("შეიყვანეთ რიცხვი >>: "))

for nums1 in range(1, n + 1):
    num = ">> :"

    for nums2 in range(nums1):
        num = num + str(nums1)

    print(num)