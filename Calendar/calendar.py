year = int(input("Enter an year between 1901 and 2099: "))
month = int(input("Enter a month from 1 to 12: "))
date = int(input("Enter a date: "))

months_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

temp = 2 + (((365*(year-1901))+((year-1901)//4))%7)
sum_months = 0
for i in range(month-1):
   sum_months += months[i]
if year%4==0 and month>2:
   sum_months += 1

temp += sum_months
day = temp % 7

print(f"{months_name[month-1]}, {year}")

calendar = []
temp_row = []
col_count = 0
row_count = 0
count = 1

for i in range(day):
   temp_row.append(" ")
   col_count += 1


for i in range(months[month-1]):
   if count == date:
      temp_row.append(f"*{count}")
   else:
      temp_row.append(f"{count}")
   col_count += 1
   count += 1
   if col_count == 7:
      col_count = 0
      calendar.append(temp_row)
      row_count += 1
      temp_row = []
for i in range(7-col_count):
   temp_row.append("")
calendar.append(temp_row)

print("Sun Mon Tue Wed Thu Fri Sat")

for i in range(row_count+1):
    for j in range(7):
        print("{:>3}".format(calendar[i][j]), end=" ")
    print("")