from datetime import datetime, timedelta

DAYS_AHEAD = 7


def get_birthday_people(date: datetime, people: list) -> list:
    result = []
    if people and date:
        for person in people:
            if not (date.month - person["birthday"].month) and not (date.day - person["birthday"].day):
                result.append(person)
    
    return result


def get_celebration_day(date: datetime) -> str:
    # if the date is a dayoff we should return Monday
    if date.strftime("%w") in "06":
        return "Monday"
    else:
        return date.strftime("%A")


def get_birthdays_per_week(persons: list) -> None:
    result_dict = {}

    current_date = datetime.today()

    for days_delta in range(DAYS_AHEAD + 1):
        check_date = current_date + timedelta(days=days_delta)

        # get a list of all birthday people for the check date
        btd_people = get_birthday_people(check_date, persons)
        if btd_people:
            celeb_day = "Today" if days_delta == 0 else get_celebration_day(check_date)
            entry = [bp["name"] for bp in btd_people]
            try:
                result_dict[celeb_day].extend(entry)
            except KeyError:
                result_dict[celeb_day] = entry

    # output
    for each in result_dict:
        print(each, ': ', sep='', end='')
        print(", ".join(result_dict[each]))


if __name__ == "__main__":
    get_birthdays_per_week([])