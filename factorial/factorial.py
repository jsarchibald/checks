from sys import argv, exit

def factorial(num):
    if num < 2:
        return 1

    return num * factorial(num - 1)

def main():
    if len(argv) != 2:
        print("Usage: python factorial.py <NUMBER>")
        exit(1)

    try:
        num = int(argv[1])
    except:
        print("You must provide an integer.")
        exit(2)

    print(factorial(num))

if __name__ == "__main__":
    main()
