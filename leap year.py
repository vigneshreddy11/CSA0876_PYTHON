def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def find_anniversary(year, is_leap):
    if is_leap:
        next_anniversary = year + 4
        print(f"The next anniversary in a leap year will be in {next_anniversary}")
    else:
        previous_anniversary = year - 4
        print(f"The previous anniversary in a non-leap year was in {previous_anniversary}")

# Example usage:
anniversary_year = 2024
leap_year = is_leap_year(anniversary_year)
find_anniversary(anniversary_year, leap_year)
