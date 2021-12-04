import re

cadena = """AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company
ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year"""

patron = r"[AEIOUaeiou]{2,3}.+txt"
print(re.findall(patron,cadena))