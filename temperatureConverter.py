print('''
================================================================================================
___________                     _________                                   __
\__    ___/___   _____ ______   \_   ___ \  ____   _______  __ ____________/  |_  ___________
  |    |_/ __ \ /     \\\____ \  /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\/ __ \_  __ \\
  |    |\  ___/|  Y Y  \  |_> > \     \___(  <_> )   |  \   /\  ___/|  | \/|  | \  ___/|  | \/
  |____| \___  >__|_|  /   __/   \______  /\____/|___|  /\_/  \___  >__|   |__|  \___  >__|
             \/      \/|__|             \/            \/          \/                 \/

================================================================================================

Description: Converts a given Temperature into other Temperature measurements.
Keywords: [Python 3, Temperature Conversion, Celsius, Fahrenheit, Kelvin]
Jan 2017 v1.0
by
NoDisassemble.me
------------------------------------------------------------------------------------------------
''')


def Fahrenheit():
    fahrenheit = input("Enter degrees in Fahrenheit to be converted to Celsius/Kelvin: ")
    # calculates celsius
    celsius = (float(fahrenheit) - 32) / 1.8
    # calculates kelvin
    kelvin = (float(fahrenheit) + 459.67) * 5 / 9
    print("")
    print('''[+] %0.1f degrees Fahrenheit is equal to:
    %0.1f degrees Celsius
    %0.1f degrees Kelvin''' % (
        float(fahrenheit), float(celsius), float(kelvin)))
    print("")


def Celsius():
    celsius = input("Enter degrees in Celsius to be converted to Fahrenheit/Kelvin: ")
    # calculates Fahrenheit
    fahrenheit = (float(celsius) * float(1.8) + float(32))
    # calculates kelvin
    kelvin = (float(celsius) + 273.15)
    print("")
    print('''[+] %0.1f degrees Celsius is equal to:
    %0.1f degrees Fahrenheit
    %0.1f degrees Kelvin''' % (float(celsius), float(fahrenheit), float(kelvin)))
    print("")


def Kelvin():
    kelvin = input("Enter degrees in Kelvin to be converted to Celsius/Fahrenheit: ")
    # Calculates Celsius
    celsius = (float(kelvin) - 273.15)
    # calculates fahrenheit
    fahrenheit = (float(kelvin) * 9 / 5 - 459.67)
    print("")
    print('''[+] %0.1f degrees Kelvin is equal to:
    %0.1f degrees Celsius
    %0.1f degrees Fahrenheit''' % (float(kelvin), float(celsius), float(fahrenheit)))
    print("")


def invalid_opt():
    # Catch for invalid response
    print("[!] Invalid choice")

# Actual program
while True:
    # Options for temperature conversion to choose from
    options = {"A": ["Celsius to Fahrenheit/Kelvin", Celsius], "B": ["Fahrenheit to Celsius/Kelvin", Fahrenheit],
               "C": ["Kelvin to Celsius/Fahrenheit", Kelvin], }
    for option in options:
        print(option + ") " + options.get(option)[0])
    # User Input for Choice
    choice = input("Which conversion would you like to make? [A, B or C]: ")
    print("")
    val = options.get(choice.upper())
    if val is not None:
        action = val[1]
    else:
        action = invalid_opt
    action()
    input("Press Enter to convert again.")
    print("")
