from datetime import datetime

dt = datetime(2022,12,13,11,10,12)
print(dt)
print(dt.year,dt.month,dt.hour,dt.minute,dt.second)

print(dt.strftime(format='%Y-%m-%d'))
print(dt.strftime(format='%Y년%m월%d일 %A'))

print(datetime.now())
cur = datetime.now()

print(cur.strftime(format="%Y-%m-%d %A"))
