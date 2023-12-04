b = int(input('Введите количество приобретаемых билетов :'))
s = 1
t = 0
x = 0
y = 0
z = 0
while s <= b:
    age = int(input('Введите возраст :'))
    if age < 18:
        x = 0
    elif 18 <= age < 25:
        y = 990
    elif age > 25:
        z = 1390
    t = x + y + z
    s += 1
if b > 3:
    t = t * 0.90

print("Сумма к оплате :", t)






