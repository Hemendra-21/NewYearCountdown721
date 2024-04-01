from datetime import datetime, timedelta

# Enter input in this form...ex: "Jul 21 2023 2:50pm"
date_string = input("Enter date in string format: ")
date_obj = datetime.strptime(date_string, "%b %d %Y %I:%M %p")
year = date_obj.year

new_year_date = datetime(year+1, 1, 1)

time_left = new_year_date - date_obj
days_left = time_left.days
sec_left = time_left.seconds
hours = sec_left//3600
minutes_left = (sec_left % 3600)//60
result = "{} days {} hours {} minutes".format(days_left, hours, minutes_left)
print("Time left for next New Year is: ", result)
