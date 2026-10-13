import sys

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print("Please provide a year as an argument.")