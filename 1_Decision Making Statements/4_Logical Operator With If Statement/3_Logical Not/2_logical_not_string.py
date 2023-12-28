
# if the string is empty, not operator returns true

name = ""
if not name:
    print("Check")
else:
    print(f"{name}")

good_credit = False
high_income = True

if not high_income or good_credit:
    print("Not Eligible")
else:
    print("Eligible")