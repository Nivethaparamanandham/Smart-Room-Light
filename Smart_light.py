print("SMART ROOM LIGHT CONTROL")

person = input("Enter 1 if person is present: ")
dark = input("Enter 1 if room is dark: ")

if person == "1" and dark == "1":
    print("Light Status: ON")
else:
    print("Light Status: OFF")
