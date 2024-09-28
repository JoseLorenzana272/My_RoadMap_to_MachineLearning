weight_measurement = input("(L)bs or (K)g: ")

while weight_measurement != "L" and weight_measurement != "K":
    print("Invalid input. Please enter either 'L' or 'K'.")
    weight_measurement = input("(L)bs or (K)g: ")
    
if weight_measurement == "L":
    weight = float(input("Enter weight in pounds: "))
    weight_kg = weight * 0.45
    print(f"You are {weight_kg} kilos.")
else:
    weight = float(input("Enter weight in kilos: "))
    weight_lbs = weight / 0.45
    print(f"You are {weight_lbs} pounds.")
