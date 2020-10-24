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