import time

print("Seconds since January 1, 1970: ", time.time(), " or ", format(time.time(), ".2e"), " in scientific notation")
print(time.strftime("%B %d %Y"))