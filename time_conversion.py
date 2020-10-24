#sample input is 07:05:45PM 
#sample output is 19:05:45

# s represents a time in 12-Hour clock format
## we must split : from hour minutes and secondsam_pm

# if s == pm and hour is not 12
    #we must add 12 to the hh 
# if s == am and hh is == 12 
    #hh == 00
# if s == pm and hour is == 12
    #hh == 12

# we must rejoin hour minutes and secondsam_pm with : 


def timeConversion(s):
    hour, minutes, secondsam_pm = s.split(':')

    if secondsam_pm[2:] == "PM" and hour != "12":
        hour = str(int(hour) + 12)
    if secondsam_pm[2:] == "AM" and hour == "12":
        hour = "00"
    if secondsam_pm[2:] == "PM" and hour == "12":
        hour = "12"

    converted_time = hour + ":" + minutes + ":" + secondsam_pm[0:2]

    return converted_time

print(timeConversion("07:05:45PM"))