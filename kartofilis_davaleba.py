elementi = input("შეიყვანეთ str ელემენტი: ")

listi = ['btu', 'test', 12, True, 'btu', 'python is best']
indexebi = []

for i in range(len(listi)):
    if listi[i] == elementi:
        indexebi.append(i)

if indexebi:
    print(f"ელემენტი '{elementi}'-ს ინდექსია: {indexebi}")
else:
    print(f"ელემენტი '{elementi}' სიაში არ არის.")
