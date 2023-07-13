y=int(input("hourly wage : "))
h=int(input("overtime hours : "))
total_hours=int(input("total numbers of regular hours : "))
if(h>0):
	pay=h*y*1.5
total_weekly_pay=y*total_hours+pay
print("hourly wage :"+str(y))
print("total regular hours : "+str(total_hours))
print("total overtime hours : "+str(h))
print("total weekly pay : "+str(total_weekly_pay))
