from datetime import datetime, timedelta, date
yesterday=datetime.now()-timedelta(1)
tomorrow=datetime.now()+timedelta(1)
difference_in_seconds=(tomorrow-yesterday).total_seconds()
print(difference_in_seconds)