import re

patron = r"[4-6]{1}\d{3}-*[0-9]{4}-*[0-9]{4}-*[0-9]{4}"

lista = ['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456']
for tarjeta in lista:
    if re.match(patron,tarjeta):
        y = re.split(r"-",tarjeta)
        z = "".join(y)
        x = 0
        for i in range(1,15):
            if z[i]==z[i+1]:
                x = x + 1
        if x>=3:
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")