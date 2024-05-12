def converter_day_month(date_sqlite_format):
    day, month = map(int, date_sqlite_format.split('-'))


    months = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
              'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']


    if 1 <= month <= 12:
        return f'{day} {months[month - 1]}'
    else:
        return f"Неверный формат даты: {date_sqlite_format}"
print(converter_day_month("1-5"))

