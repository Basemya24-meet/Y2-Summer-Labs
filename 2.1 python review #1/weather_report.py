import random
highest_temp = 0
lowest_temp = 40
alltemp = 0
aboveavg= []
dayscounter=0
temperatures = []
daytemp = []
days_of_the_week=["Sunday","Monday","Tuesday","wednesday","Thursday","friday","Saturday"]
for i in range (7):
	temperatures.append(random.randint(26,40))
	if temperatures[i]%2==0:
		dayscounter=dayscounter+1
		daytemp.append(days_of_the_week[i])
	alltemp = alltemp+temperatures[i]
	print(days_of_the_week[i],":",temperatures[i])
avgtemp = alltemp / 7
highest_temp_day=""
lowest_temp_day = " "
for i in range (7):
	if highest_temp<temperatures[i]:
		highest_temp=temperatures[i]
		highest_temp_day=days_of_the_week[i]
	if lowest_temp>temperatures[i]:
		lowest_temp=temperatures[i]
		lowest_temp_day=days_of_the_week[i]

	if avgtemp<temperatures[i]:
		aboveavg.append(days_of_the_week[i])



    	

print("shelly had ",dayscounter,"good days")
print("the avrage temp is :",avgtemp)
print("above avg days were: ", aboveavg)
print("highest temp is: ",highest_temp,"on ",highest_temp_day)
print("lowest temp is: ",lowest_temp, "on ", lowest_temp_day)