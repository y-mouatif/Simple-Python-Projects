print("Welcome to The Unit Converter")
print()
#a list with all the conversions available
conversions = [(1, "km","mi"),
               (2, "mi","km"),
               (3, "kg","lbs"),
               (4, "lbs","kg"),
               ]
#functions that will do the conversion
def km_to_mi(km):
    return km * 0.621371

def mi_to_km(mi):
    return mi * 1.60934

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs * 0.453592
print("Conversion Options:")
for conversion in conversions:
    print(f"{conversion[0]}. Convert {conversion[1]} to {conversion[2]}")

#while loop that will check if the choice is valid
while True:
    choice = int(input("Enter the number corresponding to the conversion you want to perform: "))
    
    if choice in range(1, 5):
        break; #breaking out of the loop iof the choiuce is valid
    else:
        print("Invalid choice. Please enter a valid conversion option.")



if choice == 1:
    km = float(input("Enter the distance in kilometers: "))
    miles = km_to_mi(km)
    print(f"{km} kilometers is equal to {miles} miles.")
elif choice == 2:
    mi = float(input("Enter the distance in miles: "))
    kilometers = mi_to_km(mi)
    print(f"{mi} miles is equal to {kilometers} kilometers.")
elif choice == 3:
    kg = float(input("Enter the weight in kilograms: "))
    pounds = kg_to_lbs(kg)
    print(f"{kg} kilograms is equal to {pounds} pounds.")
elif choice == 4:
    lbs = float(input("Enter the weight in pounds: "))
    kilograms = lbs_to_kg(lbs)
    print(f"{lbs} pounds is equal to {kilograms} kilograms.")
