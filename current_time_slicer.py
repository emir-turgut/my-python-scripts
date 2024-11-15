def current_time_slicer():

    from datetime import datetime

    current_time = str(datetime.now())

    current_year = current_time[0:4]
    current_month = current_time[5:7]
    current_day = current_time[8:10]
    current_hour = current_time[11:13]
    current_minute = current_time[14:16]
    current_second = current_time[17:19]
    current_microseconds = current_time[20:26]

    return {
        "year": current_year,
        "month": current_month,
        "day": current_day,
        "hour": current_hour,
        "minute": current_minute,
        "second": current_second,
        "microseconds": current_microseconds
    }
