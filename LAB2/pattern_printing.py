"""Program 6: Print three patterns for n rows -- a star triangle, a number
pattern, and a centered pyramid -- using nested loops."""


def print_star_triangle(n):
    """Right-angled triangle of stars, n rows."""
    for row in range(1, n + 1):
        print("*" * row)


def print_number_pattern(n):
    """Each row contains numbers from 1 up to the row number."""
    for row in range(1, n + 1):
        line = ""
        for col in range(1, row + 1):
            line += str(col)
        print(line)


def print_pyramid(n):
    """Simple pyramid centered using spaces."""
    for row in range(1, n + 1):
        spaces = " " * (n - row)
        stars = "*" * (2 * row - 1)
        print(spaces + stars)


def get_positive_int(prompt):
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid whole number.")
            continue
        if value <= 0:
            print("Please enter a number greater than 0.")
            continue
        return value


def main():
    n = get_positive_int("Enter the number of rows: ")

    print("\n-- Right-angled triangle of stars --")
    print_star_triangle(n)

    print("\n-- Number pattern --")
    print_number_pattern(n)

    print("\n-- Centered pyramid --")
    print_pyramid(n)


if __name__ == "__main__":
    main()
