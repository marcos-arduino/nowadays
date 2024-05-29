import datetime
import calendar
from datetime import timedelta

def weekday(weekday):
                match weekday:
                    case 0:
                        return "Lunes"
                    case 1:
                        return "Martes"
                    case 2:
                        return "Miercoles"
                    case 3:
                        return "Jueves"
                    case 4:
                        return "Viernes"
                    case 5:
                        return "Sabado"
                    case 6:
                        return "Domingo"

def schedule(day_of_the_week, file):
    with open("archive/schedules.txt", "r", encoding="utf-8") as schedules_file:
        for line in schedules_file:
            if day_of_the_week in line:
                file.write(line.replace(f'{day_of_the_week} ', ''))

# def new_dates(date_day, day_of_the_week, calendar_file):
#     with open("archive/dates.txt", "w+", encoding="utf-8") as dates_file:
#         inbox(date_day, day_of_the_week, dates_file)
#         lines = dates_file.readlines()
#         for line in lines:
#             new_date = line
#             if (f"{date_day}" in new_date):
#                 new_date = new_date.replace(f'{date_day} ', '')
#             if (day_of_the_week in new_date):
#                 new_date = new_date.replace(f'{day_of_the_week} ', '')
#             new_date = f"+{new_date}"
#             i = lines.index(line)
#             lines.pop(i)
#             calendar_file.write(new_date)
#         dates_file.writelines(lines)
#       inbox(date_day, day_of_the_week, dates_file)
#       lines = dates_file.readlines()
#       for line in lines:
#           new_date = line
#           if (f"{date_day}" in new_date) or (day_of_the_week in new_date):
#               new_date = new_date.replace(f'{date_day} ', '')
#               new_date = new_date.replace(f'{day_of_the_week} ', '')
#               new_date = f"+{new_date}"
#               file.write(new_date)
#               i = lines.index(line)
#               while line != lines[i]:
#                   dates_file.write(lines[i])
#                   i += 1

# def inbox(day, day_of_the_week, dates_f):
#     with open("inbox.txt", "w+", encoding="utf-8") as inbox_file:
#         lines = inbox_file.readlines()
#         for line in lines:
#             if (day_of_the_week in line) or (day in line):
#                 new_line = line
#                 dates_f.write(new_line)
#                 i = lines.index(line)
#                 lines.pop(i)
#         inbox_file.writelines(lines)
#        lines = inbox_file.readlines()
#        for line in lines:
#            if day_of_the_week or day in line:
#                new_line = line
#                new_line = new_line.replace(f'{day_of_the_week} ', '')
#                new_line = new_line.replace(f'{day} ', '')
#                file.write(new_line)
#                i = lines.index(line)
#                while line != lines[i]:
#                    inbox_file.write(lines[i])
#                    i += 1



año = datetime.date.today().year
mes = datetime.date.today().month
hoy = datetime.date.today()
#print(año, mes)

mes_mostrar = calendar.Calendar(firstweekday=0).monthdays2calendar(year=año, month=mes)

#mes = calendar.Calendar.monthdatescalendar(datetime.datetime.now().year, datetime.datetime.now().month)
calendario = calendar.TextCalendar(firstweekday=0).formatmonth(año, mes, 0, 0)
#semana = calendar.TextCalendar(firstweekday=0).formatweek(año, 5, 0, 0)

#####################################################
now = datetime.date.today()                         
#print(datetime.date.today()+timedelta(days=1))     
for i in range(20):                                 
    datetime.date.today()+timedelta(days=i)         
#####################################################

with open("calendar.txt", "w", encoding="utf-8") as file:
    #file.write(f"{now}\n")
    #file.write(f"{calendario}\n")
    #file.write(f"{calendar.Calendar(firstweekday=0).monthdays2calendar(year=año, month=mes)}\n")
    #file.write(f"{calendar.Calendar(firstweekday=0).monthdayscalendar(year=año, month=mes)}\n")
    for i in range(28):
        day = (hoy + timedelta(days=i))
        day_of_week_str = weekday(day.weekday())
        file.write(f"{day} {day_of_week_str}\n")
        schedule(day_of_week_str, file)
        # new_dates(day, day_of_week_str, file)
        #print((hoy+timedelta(days=i)).day)
        file.write("\n")
                #print(todo())


with open("calendar.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        if str(hoy) in line:
            i = lines.index(line)
            print(f"hoy: \n{line}")
            while f"\n" != lines[i]:
                i += 1
                print(lines[i].strip(f"\n"))
        if str(hoy+timedelta(days=1)) in line:
            print(f"mañana: \n{line}")
            while f"\n" != lines[i]:
                i += 1
                print(lines[i].strip(f"\n"))


# print(calendar.Calendar(firstweekday=0).monthdayscalendar(year=año, month=mes))
# for i in calendar.Calendar(firstweekday=0).monthdayscalendar(year=año, month=mes):
#     for j in i:
#         print(j)
#         if datetime.date.today().day == j:
#             print(calendar.Calendar(firstweekday=0).monthdayscalendar(year=año, month=mes).index(i)) #esto me dice en que semana esta el dia, si cambio todo el choclo por i.index(j) me dice en dia de la semana esta



