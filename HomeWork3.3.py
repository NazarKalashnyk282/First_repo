from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d')
        next_birthday = datetime(today.year, birthday.month, birthday.day)

        if next_birthday < today:
            next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

        if (next_birthday - today).days <= 7:
            if next_birthday.weekday() >= 5:
                next_birthday += timedelta(days=(7 - next_birthday.weekday()))
            congrats_date = next_birthday.strftime('%Y.%m.%d')
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': congrats_date})

    return upcoming_birthdays

users = [
    {'name': 'Oleksandr', 'birthday': '1990.03.13'},
    {'name': 'Ann', 'birthday': '1985.12.30'},
    {'name': 'Viktoria', 'birthday': '1995.02.10'},
]

upcoming = get_upcoming_birthdays(users)
print(upcoming)