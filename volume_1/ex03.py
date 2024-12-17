print("\nSKELETON COMPETITION\n")

minutes_hanna = int(input("Enter Hanna Neise's minutes "))
seconds_hanna = int(input("Enter Hanna Neise's seconds "))
milliseconds_hanna = int(input("Enter Hanna Neise's milliseconds "))
minutes_jackie = int(input("Enter Jackie Narracott's minutes "))
seconds_jackie = int(input("Enter Jackie Narracott's seconds "))
milliseconds_jackie = int(input("Enter Jackie Narracott's milliseconds "))
minutes_kimberley = int(input("Enter Kimberley Bos's minutes "))
seconds_kimberley = int(input("Enter Kimberley Bos's seconds "))
milliseconds_kimberley = int(input("Enter Kimberley Bos's milliseconds "))

time_hanna = (
    str(minutes_hanna) + " Minutes",
    str(seconds_hanna) + " Seconds",
    str(milliseconds_hanna) + " Milliseconds",
)

time_jackie = (
    str(minutes_jackie) + " Minutes",
    str(seconds_jackie) + " Seconds",
    str(milliseconds_jackie) + " Milliseconds",
)

time_kimberley = (
    str(minutes_kimberley) + " Minutes",
    str(seconds_kimberley) + " Seconds",
    str(milliseconds_kimberley) + " Milliseconds",
)

print("\n")

print("Hanna Neise's Time: " + str(time_hanna))
print("Jackie Narracott's Time: " + str(time_jackie))
print("Kimberley Bos's Time: " + str(time_kimberley))

total_seconds_hanna = (
    (minutes_hanna * 60) + seconds_hanna + (milliseconds_hanna * 0.001)
)
total_seconds_jackie = (
    (minutes_jackie * 60) + seconds_jackie + (milliseconds_jackie * 0.001)
)
total_seconds_kimberley = (
    (minutes_kimberley * 60) + seconds_kimberley + (milliseconds_kimberley * 0.001)
)

print("\n")

print("Total time in seconds for Hanna Neise: " + str(total_seconds_hanna))
print("Total time in seconds for Jackie Narracott: " + str(total_seconds_jackie))
print("Total time in seconds for Kimberley Bos: " + str(total_seconds_kimberley))

print("\n")

speed_hanna = total_seconds_hanna / 100
speed_jackie = total_seconds_jackie / 100
speed_kimberley = total_seconds_kimberley / 100

print("\n")

print("Hanna Neise's Speed: " + str(round(speed_hanna)) + " meters/sec")
print("Jackie Narracott's Speed: " + str(round(speed_jackie)) + " meters/sec")
print("Kimberley Bos's Speed: " + str(round(speed_kimberley)) + " meters/sec")