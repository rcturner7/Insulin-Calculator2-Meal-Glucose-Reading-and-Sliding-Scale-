scale = int(input("What Carb/Insulin ratio are you on? Type the number of carbs per unit of insulin you are on. "))

ratio = int(input("How many carbs is your meal/snack? "))

blood_sugar = int(input("What is your glucos level? "))

units_of_insulin = ratio / scale

total_units = units_of_insulin

if blood_sugar < 70:
    take_less_carbs = ratio - 35
    units_of_insulin = take_less_carbs / scale
    total_units = units_of_insulin
    print(f"You need to take {total_units} units of insulin. Take adjusted less insulin, eat your food, recheck your glucose levels in 15 to 30 minutes, if glucose levels do not rise above 70 intake 30 more carbs, recheck glucose levels again if needed, and be safe.")
elif (blood_sugar >= 200) and (blood_sugar < 225):
    total_units = units_of_insulin + 1
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 225) and (blood_sugar < 250):
    total_units = units_of_insulin + 2
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 250) and (blood_sugar < 275):
    total_units = units_of_insulin + 3
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 275) and (blood_sugar < 300):
    total_units = units_of_insulin + 4
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 300) and (blood_sugar < 325):
    total_units = units_of_insulin + 5
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 325) and (blood_sugar < 350):
    total_units = units_of_insulin + 6
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 350) and (blood_sugar < 375):
    total_units = units_of_insulin + 7
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 375) and (blood_sugar < 400):
    total_units = units_of_insulin + 8
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 400) and (blood_sugar < 425):
    total_units = units_of_insulin + 9
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 425) and (blood_sugar < 450):
    total_units = units_of_insulin + 10
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 450) and (blood_sugar < 275):
    total_units = units_of_insulin + 11
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 475) and (blood_sugar < 500):
    total_units = units_of_insulin + 12
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 500) and (blood_sugar < 525):
    total_units = units_of_insulin + 13
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 525) and (blood_sugar < 550):
    total_units = units_of_insulin + 14
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 550) and (blood_sugar < 575):
    total_units = units_of_insulin + 15
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif (blood_sugar >= 575) and (blood_sugar < 600):
    total_units = units_of_insulin + 16
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
elif blood_sugar >= 600:
    total_units = units_of_insulin + 17
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
else:
    print(f"You need to take {total_units} units of insulin. Enjoy your meal.")
    


