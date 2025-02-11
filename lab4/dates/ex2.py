from datetime import date, timedelta, datetime
tomorrow=date.today()+timedelta(1)
yesterday=date.today()-timedelta(1)
print("Today is ", date.today())
print("Tomorrow is ", tomorrow)
print("Yesterday is ", yesterday)