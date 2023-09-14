import datetime
import pytz
newTimeZone = pytz.timezone('Europe/Moscow')
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%H:%M:%S")
print(formatted_datetime)
numbers={'0':
'██████████'
'███    ███'
'███    ███'
'███    ███'
'██████████',

'1':
'    ██████'
'       ███'
'       ███'
'       ███'
'       ███',

'2':
'██████████'
'       ███'
'██████████'
'███       '
'██████████',


'3':
'██████████'
'       ███'
'██████████'
'       ███'
'██████████',

'4':
'███    ███'
'███    ███'
'██████████'
'       ███'
'       ███',

'5':
'██████████'
'███       '
'██████████'
'       ███'
'██████████',

'6':
'██████████'
'███       '
'██████████'
'███    ███'
'██████████',

'7':
'██████████'
'       ███'
'       ███'
'       ███'
'       ███',

'8':
'██████████'
'███    ███'
'██████████'
'███    ███'
'██████████',

'9':
'██████████'
'███    ███'
'██████████'
'       ███'
'██████████'}
def time():
 current_datetime = datetime.datetime.now()
 formatted_datetime = current_datetime.strftime("%I:%M:%S")
 print(formatted_datetime)
 formatted_datetime= ("**********"+" " +"**********"+"   " + "**********"+" " +"**********"+"   " +"**********"+" " +"**********"),
("**********"+" " +"**********"+" █ " + "**********"+" " +"**********"+" █ " +"**********"+" " +"**********"),
("**********"+" " +"**********"+"   " + "**********"+" " +"**********"+"   " +"**********"+" " +"**********"),
("**********"+" " +"**********"+" █ " + "**********"+" " +"**********"+" █ " +"**********"+" " +"**********"),
("**********"+" " +"**********"+"   " + "**********"+" " +"**********"+"   " +"**********"+" " +"**********")
def num():
 for formatted_datetime in numbers.values(): 
   print(formatted_datetime+" " + formatted_datetime +" " + formatted_datetime +" " +formatted_datetime +" " + formatted_datetime)
   print(formatted_datetime+"█ " + formatted_datetime +" " + formatted_datetime +" █" +formatted_datetime +" " + formatted_datetime)
   print(formatted_datetime+" " + formatted_datetime +" " + formatted_datetime +" " +formatted_datetime +" " + formatted_datetime)
   print(formatted_datetime+"█ " + formatted_datetime +" " + formatted_datetime +" █ " +formatted_datetime +" " + formatted_datetime)
   print(formatted_datetime+" " + formatted_datetime +" " + formatted_datetime +" " +formatted_datetime +" " + formatted_datetime)
num() 
