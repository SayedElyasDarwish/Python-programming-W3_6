M_TO_KM = 0.001
KM_TO_M = 1000.0
G_TO_LB = 0.002205
LB_TO_G = 453.6

print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")
print()

if choice == "1":
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice = input("Your choice: ")
    if choice == "1":
        meters = float(input("Insert meters: "))
        print(f"{meters:.1f} m is {meters * M_TO_KM:.1f} km")
    elif choice == "2":
        kilometers = float(input("Insert kilometers: "))
        print(f"{kilometers:.1f} km is {kilometers * KM_TO_M:.1f} m")
    elif choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice = input("Your choice: ")
    if choice == "1":
        grams = float(input("Insert grams: "))
        print(f"{grams:.1f} g is {grams * G_TO_LB:.4f} lb")
    elif choice == "2":
        pounds = float(input("Insert pounds: "))
        print(f"{pounds:.1f} lb is {pounds * LB_TO_G:.1f} g")
    elif choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
