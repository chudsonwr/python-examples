
size = input('Enter cube side length in cm: ')

try:
    size = int(size)
except:
    print("Hey dude thats not a number!")
    exit()

volume = size**3 * 1000

print(f"This is the volume in mm3: {volume}")


