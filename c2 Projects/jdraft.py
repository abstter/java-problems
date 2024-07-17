def jdate_to_date():
    jdate = input('Enter a Julian date number: ')
    month = ''
    day = daynum(jdate)
    year = yearnum(jdate)
    if year % 4 == 0:
        leap_yr_offset = 1
    else:
        leap_yr_offset = 0
    if day <= 31:
        month = 'January'
    elif day <= 59 + leap_yr_offset:
        month = 'February'
    elif day <= 90 + leap_yr_offset:
        month = 'March'
    elif day <= 120 + leap_yr_offset:
        month = 'April'
    elif day <= 151 + leap_yr_offset:
        month = 'May'
    elif day <= 181 + leap_yr_offset:
        month = 'June'
    elif day <= 212 + leap_yr_offset:
        month = 'July'
    elif day <= 243 + leap_yr_offset:
        month = 'August'
    elif day <= 273 + leap_yr_offset:
        month = 'September'
    elif day <= 304 + leap_yr_offset:
        month = 'October'
    elif day <= 334 + leap_yr_offset:
        month = 'November'
    elif day <= 365 + leap_yr_offset:
        month = 'December'
    date = month + ' ' + day + ', ' + year
    print('That date is', date)
    
jdate_to_date() 