#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        print("{} arguments{}".format(argc - 1, ":" if argc > 1 else "."))
    else:
        print("1 argument:")
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
