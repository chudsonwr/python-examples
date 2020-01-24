import argparse
 
parser = argparse.ArgumentParser(description='Speed and Distance Calculator.')
parser.add_argument('-t','--time', type=int, help='Input time',required=True)
parser.add_argument('-s','--speed', type=int, help='Input average speed', required=False)
parser.add_argument('-d','--distance', type=int, help='Input Distance to Cover', required=False)
args = parser.parse_args()

if args.speed:
    distance = args.speed * args.time
    print(f"Distance covered: {distance}")
elif args.distance:
    speed = args.distance / args.time
    print(f"Speed required: {speed}")
