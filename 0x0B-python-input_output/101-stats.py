#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""


def print_stats(file_size, stats):
    """Prints total file size and valid codes count."""

    print("File size: {}".format(file_size))
    for code in sorted(stats):
        print("{}: {}".format(code, stats[code]))


if __name__ == "__main__":
    import sys

    file_size = 0
    possible_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in possible_codes:
                    if stats.get(line[-2], -1) == -1:
                        stats[line[-2]] = 1
                    else:
                        stats[line[-2]] += 1
            except IndexError:
                pass

            if count % 10 == 0:
                print_stats(file_size, stats)

        print_stats(file_size, stats)
    except KeyboardInterrupt:
        print_stats(file_size, stats)
        raise
