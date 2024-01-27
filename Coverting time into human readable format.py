#Coverting time into human readable format
#Input --> "09.05.1945 06:07"
#Output --> "9 May Year 1945 06 hours 07 minutes"

timestamp="09.06.1945 06:07"
months=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
list=timestamp.split()

date=[]
for i in list[0].split("."):
    date.append(i)

time=[]
for i in list[1].split(":"):
    time.append(i)
 
month=months[int(date[1])-1]
print(f"{date[0]} {month} Year {date[2]} {time[0]} hours {time[1]} minutes")
