#!/usr/bin/python3
# prints the number of and list of its arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, args[i]))

        elif size == 0:
            printg("{} arguments.".format(size))

        else:
            print("{} argument".format(size))
            print("{}: {}".format(size, arg[1]))
