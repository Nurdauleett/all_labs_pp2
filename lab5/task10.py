import re 


with open("task10_row.txt") as f:
    data = f.read()

matches=re.sub(r"[A-Z]",'_',data)
print(matches)