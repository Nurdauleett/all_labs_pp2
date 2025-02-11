from datetime import datetime
time=datetime.now()
withoutmil=time.strftime("%Y-%m-%d, %H:%M:%S")
print(withoutmil)