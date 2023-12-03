#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    objects = dir(hidden_4)
    for token in objects:
        if "__" not in token:
            print(token)
