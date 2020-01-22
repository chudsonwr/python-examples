

distance = 0
speed = 0

time = int(input('Enter the time: '))
try:
    speed = int(input('Enter the speed (hit Enter if unknown: '))
except ValueError:
    speed = 0

if speed == 0:
    try:
        distance = int(input('Enter the distance travelling: '))
    except ValueError:
        distance = 0



if speed:
    distance = speed * time
    print(f"Distance covered: {distance}")
elif distance:
    speed = distance / time
    print(f"Speed required: {speed}")




