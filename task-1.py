duration = input('Какой промежуток времени вас интересует: ')
minute = 60
hour = minute * 60
day = hour * 24
month = day * 12
duration_int = int(duration)
minute_int = duration_int // minute
hour_int = minute_int // minute
day_int = hour_int // 24
month_int = day_int // 30
year_int = month_int // 12
i = 0
while True:
    if duration_int < minute:
        print(f'{duration} sec')
    elif minute_int < minute:
        print(f'{minute_int} min {duration_int % minute} sec')
    elif hour_int < 24:
        print(f'{hour_int} hour {minute_int % minute} min {duration_int % minute} sec')
    elif day_int < 30:
        print(f'{day_int} day {hour_int % 24} hour {minute_int % minute} min {duration_int % minute} sec')
    elif month_int < 12:
        print(f'{month_int} month {day_int % 30} day {hour_int % 24} hour {minute_int % minute} min {duration_int % minute} sec')
    else:
        print(f'{year_int} year {month_int % 12} month {day_int % 30} day {hour_int % 24} hour {minute_int % minute} min {duration_int % minute} sec')
    break