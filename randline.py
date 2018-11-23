import random
import sys
import datetime

def timeOfDay(time):
    if time.hour <= 2 or time.hour >= 18:
        return 'evening'
    elif time.hour <= 12:
        return 'morning'
    else:
        return 'afternoon'

def dayOrNight(time):
    if time.hour <= 4 or time.hour >= 20:
        return 'night'
    else:
        return 'day'

def todayOrTonight(time):
    if time.hour <= 4 or time.hour >= 20:
        return 'tonight'
    else:
        return 'today'

def dayOfWeek(time):
    return time.strftime('%A')

def main():
    lines = open(sys.argv[1]).readlines()
    name = sys.argv[2] if len(sys.argv) > 2 else 'stranger'
    now = datetime.datetime.now()
    print(lines[random.randrange(len(lines))].strip() % {
        'timeOfDay': timeOfDay(now),
        'dayOrNight': dayOrNight(now),
        'todayOrTonight': todayOrTonight(now),
        'dayOfWeek': dayOfWeek(now),
        'name': name
    })

if __name__ == "__main__":
    main()
