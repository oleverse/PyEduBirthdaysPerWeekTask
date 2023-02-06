from datetime import datetime, timedelta

COLLEAGUES = [
    {"name": "Anna", "birthday": datetime(2008, 2, 11)},
    {"name": "Notanna", "birthday": datetime(2001, 2, 12)},
    {"name": "Clare", "birthday": datetime(1996, 12, 30)},
]

DAYS_AHEAD = 7


def get_birthday_people(date: datetime, people: list) -> list:
    result = []
    if people and date:
        for person in people:
            if not (date.month - person["birthday"].month) and not (date.day - person["birthday"].day):
                result.append(person)
    
    return result


def get_celebration_day(date: datetime) -> str:
    if date.strftime("%w") in "06":
        return "Monday"
    else:
        return date.strftime("%A")


def get_birthdays_per_week(persons: list) -> None:
    
    current_date = datetime.today()

    week_ahead_list = [(current_date + timedelta(days=d)) for d in range(DAYS_AHEAD)]
    
    for d in week_ahead_list:
        btd_people = get_birthday_people(d, persons)
    
        if btd_people:
            celeb_day = get_celebration_day(d)
            print(f'{celeb_day}: ', end='')
            print(", ".join([bp["name"] for bp in btd_people]))



if __name__ == "__main__":
    get_birthdays_per_week(COLLEAGUES)