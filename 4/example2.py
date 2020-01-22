import sys, getopt
# Store defaults
speed = 0
time = 0
distance = 0

# Read command line args
try:
    myopts, args = getopt.getopt(sys.argv[1:],"t:d:s:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -d distance -t time OR -s speed -t time" % sys.argv[0])
    sys.exit(2)
 
###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-d':
        distance = int(a)
    elif o == '-t':
        time = int(a)
    elif o == '-s':
        speed = int(a)
    else:
        print("Usage: %s -d distance -t time OR -s speed -t time" % sys.argv[0])

# print(f"Distance: {distance}\nTime: {time}\nSpeed: {speed}\n")

if speed > 0:
    distance = speed * time
    print(f"Distance covered: {distance}")
elif distance > 0:
    speed = distance / time
    print(f"Speed required: {speed}")




