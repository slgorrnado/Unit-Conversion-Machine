# Final Project: Unit Converter

def length_converter():
    print("Length Converter")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print("Length in feet:", round(feet, 2))
    elif choice == 2:
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print("Length in meters:", round(meters, 2))
    else:
        print("Invalid choice")


def mass_converter():
    print("Mass Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        kilograms = float(input("Enter mass in kilograms: "))
        pounds = kilograms * 2.20462
        print("Mass in pounds:", round(pounds, 2))
    elif choice == 2:
        pounds = float(input("Enter mass in pounds: "))
        kilograms = pounds / 2.20462
        print("Mass in kilograms:", round(kilograms, 2))
    else:
        print("Invalid choice")


def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", round(fahrenheit, 2))
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius:", round(celsius, 2))
    else:
        print("Invalid choice")


def pressure_converter():
    print("Pressure Converter")
    print("1. Pascals to PSI")
    print("2. PSI to Pascals")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pascals = float(input("Enter pressure in Pascals: "))
        psi = pascals / 6895
        print("Pressure in PSI:", round(psi, 2))
    elif choice == 2:
        psi = float(input("Enter pressure in PSI: "))
        pascals = psi * 6895
        print("Pressure in Pascals:", round(pascals, 2))
    else:
        print("Invalid choice")


def volume_converter():
    print("Volume Converter")
    print("1. Liters to Gallons")
    print("2. Gallons to Liters")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        liters = float(input("Enter volume in Liters: "))
        gallons = liters * 0.264172
        print("Volume in Gallons:", round(gallons, 2))
    elif choice == 2:
        gallons = float(input("Enter volume in Gallons: "))
        liters = gallons / 0.264172
        print("Volume in Liters:", round(liters, 2))
    else:
        print("Invalid choice")


def speed_converter():
    print("Speed Converter")
    print("1. m/s to mph")
    print("2. mph to m/s")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ms = float(input("Enter speed in m/s: "))
        mph = ms * 2.237
        print("Speed in mph:", round(mph, 2))
    elif choice == 2:
        mph = float(input("Enter speed in mph: "))
        ms = mph / 2.237
        print("Speed in m/s:", round(ms, 2))
    else:
        print("Invalid choice")


def density_converter():
    print("Density Converter")
    print("1. kg/m^3 to g/cm^3")
    print("2. g/cm^3 to kg/m^3")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        kgm = float(input("Enter density in kg/m^3: "))
        gcm = kgm / 1000
        print("Density in g/cm^3:", round(gcm, 2))
    elif choice == 2:
        gcm = float(input("Enter density in g/cm^3: "))
        kgm = gcm * 1000
        print("Density in kg/m^3:", round(kgm, 2))
    else:
        print("Invalid choice")


def main():
    print("\nWelcome to the Unit Conversion Machine!")
    active = True
    while active:
        print("\nChoose the type of conversion:")
        print("1. Length")
        print("2. Mass")
        print("3. Temperature")
        print("4. Pressure")
        print("5. Volume")
        print("6. Speed")
        print("7. Density")
        print("8. Quit")
        print("-" * 31)
        option = int(input("Select a measurement 1-7 (type 8 to quit): "))
        if option == 1:
            length_converter()
        elif option == 2:
            mass_converter()
        elif option == 3:
            temperature_converter()
        elif option == 4:
            pressure_converter()
        elif option == 5:
            volume_converter()
        elif option == 6:
            speed_converter()
        elif option == 7:
            density_converter()
        elif option == 8:
            print("Thanks for using the Unit Conversion Machine!")
            print("NOTE: the Unit Conversion Machine rounds all answers to 2 decimals")
            active = False
        else:
            print("{error}")
            print("Invalid selection. Please enter a number between 1 and 7 (or type 8 to quit).")


main()
