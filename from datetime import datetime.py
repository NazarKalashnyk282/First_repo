from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')

    except ValueError:
            return "Неправильний формат дати. Використовуйте формат 'рік-місяць-день'"

    now = datetime.today()
    difference_date = now - date_obj    
    return difference_date  
           

print(get_days_from_today("2024-02-03"))