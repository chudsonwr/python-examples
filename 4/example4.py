# Ask the user which value they want to work out, distance covered or speed requireed. 
choice = input('To work out (D)istance enter \'d\'\nTo work out (S)peed enter \'s\'\n')

# declare the variables but give them a null value, so that they can be operated on 
speed = None
distance = None

# Get the input for either distance or time depending on choice variable
if choice.lower() == 'd':
    speed = int(input('Enter the speed: '))
elif choice.lower() == 's':
    distance = int(input('Enter the distance travelling: '))
else:
    print(f"Unrecognised option: '{choice}'")

# Get the input for time as it's always required
if speed or distance:
    time = int(input('Enter the time: '))


# Perform the relevant calculation
if speed:
    distance = speed * time
    print(f"Distance covered: {distance}")
elif distance:
    speed = distance / time
    print(f"Speed required: {speed}")




