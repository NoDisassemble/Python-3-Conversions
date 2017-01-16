print('''
========================================================================================================================
________  .__          __                               _________                                   __
\______ \ |__| _______/  |______    ____   ____  ____   \_   ___ \  ____   _______  __ ____________/  |_  ___________
 |    |  \|  |/  ___/\   __\__  \  /    \_/ ___\/ __ \  /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\/ __ \_  __ \\
 |    `   \  |\___ \  |  |  / __ \|   |  \  \__\  ___/  \     \___(  <_> )   |  \   /\  ___/|  | \/|  | \  ___/|  | \/
/_______  /__/____  > |__| (____  /___|  /\___  >___  >  \______  /\____/|___|  /\_/  \___  >__|   |__|  \___  >__|
        \/        \/            \/     \/     \/    \/          \/            \/          \/                 \/

------------------------------------------------------------------------------------------------------------------------
Description: Converts a given distance into various measurements.
Keywords: [Python 3, Distance Converter, Miles, Kilometers, Meters, Yards, Feet]
Jan 2017 v1.0
by
NoDisassemble.me
------------------------------------------------------------------------------------------------------------------------
''')


def Miles():
    miles = input("Enter the distance in Miles to convert: ")
    # calculate feet
    feet = float(miles) * float(5280)
    # calculate kilometers
    kilometers = float(miles) * float(1.609344)
    # calculate meters
    meters = float(miles) * float(1609.34)
    # calculate yards
    yards = float(miles) * float(1760)
    print("")
    print('''[+] %.1f Miles is equal to:
    %.5f Feet
    %.5f Kilometers
    %.5f Meters
    %.5f Yards''' % (float(miles), float(feet), float(kilometers), float(meters), float(yards)))
    print("")


def Kilometers():
    kilometers = input("Enter the distance in Kilometers to convert: ")
    # calculate meters
    meters = float(kilometers) * float(1000)
    # calculate miles
    miles = float(kilometers) * float(0.62137)
    # calculate feet
    feet = float(kilometers) * float(3280.84)
    # calculate yards
    yards = float(kilometers) * float(1093.61)
    print("")
    print('''[+] %0.1f Kilometers is equal to:
    %0.5f Meters
    %0.5f Miles
    %0.5f Feet
    %0.5f Yards''' % (float(kilometers), float(meters), float(miles), float(feet), float(yards)))
    print("")


def Meters():
    meters = input("Enter the distance in Meters to convert: ")
    # calculates kilometers
    kilometers = float(meters) * float(0.001)
    # calculates miles
    miles = float(meters) * float(0.000621371)
    # calculates feet
    feet = float(meters) * float(3.28084)
    # calculates yards
    yards = float(meters) * float(1.09361)
    print("")
    print('''[+] %0.1f Meters is equal to:
    %0.5f Kilometers
    %0.5f Miles
    %0.5f Feet
    %0.5f Yards''' % (float(meters), float(kilometers), float(miles), float(feet), float(yards)))
    print("")


def Yards():
    yards = input("Enter the distance in Yards to convert: ")
    # calculates miles
    miles = float(yards) * float(0.000568182)
    # calculates kilometers
    kilometers = float(yards) * float(0.0009144)
    # calculates meters
    meters = float(yards) * float(0.9144)
    # calculates feet
    feet = float(yards) * float(3)
    print("")
    print('''[+] %0.1f Yards is equal to:
    %0.5f Miles
    %0.5f Kilometers
    %0.5f Meters
    %0.5f Feet''' % (float(yards), float(miles), float(kilometers), float(meters), float(feet)))
    print("")


def Feet():
    feet = input("Enter the distance in Feet to convert: ")
    # calculate miles
    miles = float(feet) * float(0.000189394)
    # calculate kilometers
    kilometers = float(feet) * float(0.000304800097536)
    # calculate meters
    meters = float(feet) * float(0.3048000975359999587)
    # calculate yards
    yards = float(feet) * float(0.33333343999999998086)
    print("")
    print('''[+] %0.1f Feet is equal to:
    %0.5f Miles
    %0.5f Kilometers
    %0.5f Meters
    %0.5f Yards''' % (float(feet), float(miles), float(kilometers), float(meters), float(yards)))
    print("")


def invalid_opt():
    # Catch for invalid response
    print("[!] Invalid choice")

# Program actual
while True:
    # Options for temperature conversion to choose from
    options = {"A": ["Miles", Miles], "B": ["Kilometers", Kilometers], "C": ["Meters", Meters],
               "D": ["Yards", Yards], "E": ["Feet", Feet]}
    for option in options:
        print(option + ") " + options.get(option)[0])
    # User Input for Choice
    choice = input("Which conversion would you like to make? [A, B, C, D or E]: ")
    print("")
    val = options.get(choice.upper())
    if val is not None:
        action = val[1]
    else:
        action = invalid_opt
    action()
    input("Press Enter to convert again.")
    print("")
