import datetime 

x = datetime.datetime.now()
print(x)
print(datetime.datetime(2020, 5, 17))
print(datetime.datetime(2023,5,4,23,34,33))

so = x.strftime("%d/%b/%y")
# so = x.strftime("%d/%m/%y")
print(x.strftime("%x"))

print(x.strftime("%A"))
print(x.strftime("%I"))

print(x.year)
print(so)
print(x.strftime("%B"))

print(type(so))
