
# if list,dict,tuple is empty,(the condition will be satisfied) not operator returns true

names = ["Thara","Tom","Hanks"]

if not names:
    print("No names")
else:
    print(f"{names}")

country = {
    "Europe": "Paris",
    "Africa": "Egypt",
    "Asia": "South Korea"
}


print("No country") if not country else print(f"{country}")


