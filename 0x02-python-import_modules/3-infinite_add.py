#!/bin/bash
#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    len_ = len(sys.argv)
    if len_ == 1:
        print(0)
    else:
        j = 1
        result = 0
        while j < len_:
            result += int(sys.argv[j])
            j += 1
        print(result)
