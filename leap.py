def leap_year(year):
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    leap_year(year)