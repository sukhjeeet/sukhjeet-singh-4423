RED = "red"
BLUE = "blue"
YELLOW = "yellow"

color1 = input("Enter first primary color (red, blue, yellow): ")
color2 = input("Enter second primary color (red, blue, yellow): ")


if color1 not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color1")
elif color2 not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
    #collaborating the colors
    if color1 == RED:
     if color2 == BLUE:
            print("Purple")
     else: # color2 must be YELLOW
            print("Orange")
    elif color1 == BLUE:
        if color2 == RED:
            print("Purple")
        else: # color2 must be YELLOW
            print("Green")
    else: # color1 must be YELLOW
        if color2 == RED:
            print("Orange")
        else: # color2 must be BLUE
            print("Green")
