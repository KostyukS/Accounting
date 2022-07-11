from application.db import people
from application import salary
from datetime import datetime


if __name__ == "__main__":
    current_date = datetime.now()
    print(current_date.strftime("Date: %d.%m.%Y  time: %H:%M:%S"'\n'))
    people.get_employees()
    salary.calculate_salary()
