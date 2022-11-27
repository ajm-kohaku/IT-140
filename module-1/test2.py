"""
The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
"""
input_month = input()
input_day = int(input())

if input_month.lower() == 'january' and input_day in range(1, 32):
    season = 'Winter'
elif input_month.lower() == 'february' and input_day in range(1, 30):
    season = 'Winter'
elif input_month.lower() == 'march':
    if input_day in range(1, 20):
        season = 'Winter'
    elif input_day in range(20, 32):
        season = 'Spring'
    else:
        season = 'Invalid'
elif input_month.lower() == 'april' and input_day in range(1, 31):
    season = 'Spring'
elif input_month.lower() == 'may' and input_day in range(1, 32):
    season = 'Spring'
elif input_month.lower() == 'june':
    if input_day in range(1, 21):
        season = 'Spring'
    elif input_day in range(21, 31):
        season = 'Summer'
    else:
        season = 'Invalid'
elif input_month.lower() == 'july' and input_day in range(1, 32):
    season = 'Summer'
elif input_month.lower() == 'august' and input_day in range(1, 32):
    season = 'Summer'
elif input_month.lower() == 'september':
    if input_day in range(1, 22):
        season = 'Summer'
    elif input_day in range(22, 31):
        season = 'Autumn'
    else:
        season = 'Invalid'
elif input_month.lower() == 'october' and input_day in range(1, 32):
    season = 'Autumn'
elif input_month.lower() == 'november' and input_day in range(1, 31):
    season = 'Autumn'
elif input_month.lower() == 'december':
    if input_day in range(1, 22):
        season = 'Autumn'
    elif input_day in range(22, 32):
        season = 'Winter'
    else:
        season = 'Invalid'
else:
    season = 'Invalid'

print(season)
