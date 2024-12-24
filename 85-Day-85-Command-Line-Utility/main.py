import argparse
import sys

def calc(args):
    if args.o == "add":
        return args.x + args.y
    elif args.o == "sub":
        return args.x - args.y
    if args.o == "mul":
        return args.x * args.y
    if args.o == "div":
        return args.x / args.y
    else:
        return "Something went wrong"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple calculator utility. Contact Alok for more help.")
    parser.add_argument("--x", type=float, default=1.0, help="Enter the first number, default is 1.0. This is a utility for calculation. Contact Alok for more help.")
    parser.add_argument("--y", type=float, default=3.0, help="Enter the second number, default is 3.0. This is a utility for calculation. Contact Alok for more help.")
    parser.add_argument("--o", type=str, default="add", help="Enter the operation, default is add. This is a utility for calculation. Contact Alok for more help.")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))