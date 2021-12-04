import re

s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
patron = r"@robot\d!"
print(re.findall(patron,s))