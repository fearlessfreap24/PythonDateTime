from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

# Current UTC Time
def getUtcNowTime():
    return datetime.utcnow()


# Current System time
def getSysTime():
    return datetime.now()


# Let's say that your maintenance window starts at 2300 (11:00 PM civilian time)
# use a time object to create a variable for that time
def getMaintWindowStart():
    return time(23, 0, 0)


# let's say that the maintence window ends at 0500 (5:00 AM civilian time)
# use a time object to create a variable for that time
def getMaintWindowEnd():
    return time(5, 0, 0)


# if you know the time zone difference you can adjust UTC time with the difference
#  either add or subtract the number of hours in the difference
# in the return statement we created a timedelta object so that we could do the math
def getUTCwithTimeZone(timezone):
    # time zones west of Prime Meridian
    if timezone < 0:
        return getUtcNowTime() - timedelta(hours=abs(timezone))
    # time zones east of the Prime Meridian
    else:
        return getUtcNowTime() + timedelta(hours=timezone)


# Let's tie this all together. This function will take the current UTC time adjusted
# with the time zone and determine if it is in the maintenance window
def isInMaintWindow(currentTime):
    if currentTime.hour == getMaintWindowStart().hour and currentTime.hour < getMaintWindowEnd().hour:
        return True

    # implied else
    return False



def main():
    utcNow = getUtcNowTime()
    print(f"UTC time is - {str(utcNow)}")
    
    sysTime = getSysTime()
    print(f"System time is - {str(sysTime)}")

    dfwTimeZone = -5
    utcWithTimeZone = getUTCwithTimeZone(dfwTimeZone)
    print(f"UTC time adjusted with time zone - {str(utcWithTimeZone)}")

    maintStart = getMaintWindowStart()
    print(f"Maintenance window starts at - {str(maintStart)}")

    maintEnd = getMaintWindowEnd()
    print(f"Maintenance window ends at - {str(maintEnd)}")

    # lets create a list of times to test 
    listOfTimes = [ time(4, 59, 39), time(22, 59, 59), time(0, 0, 1)]

    for i in listOfTimes:
        if i.hour == maintStart.hour or i.hour < maintEnd.hour:
            print(f"{str(i)} is in maintenance window")
        else:
            print(f"{str(i)} in NOT in maintenance window")

    print(f"The current UTC time adjusted with time zone is {str(utcWithTimeZone)}")
    print(f"it is in the Maintenance Window = {isInMaintWindow(utcWithTimeZone)}")



if __name__ == "__main__":
    main()

