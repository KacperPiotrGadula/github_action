from datetime import datetime, timedelta
import sys

# Downloading arguments from GitHub Actions
time_zone = sys.argv[1]
start_date_banner = sys.argv[2]
end_date_banner = sys.argv[3]
start_time = sys.argv[4]
end_time = sys.argv[5]

# Converting dates to datetime objects
start_date = datetime.strptime(start_date_banner, "%d.%m.%Y")
end_date = datetime.strptime(end_date_banner, "%d.%m.%Y")
start_time_dt = datetime.strptime(start_time, "%H:%M")

# Handling the special case for the end time '24:00'
if end_time == "24:00":
    end_time_dt = datetime.strptime("00:00", "%H:%M") + timedelta(days=1)
    end_datetime = datetime.combine(end_date, end_time_dt.time())
    end_time_display = "24:00"
else:
    end_time_dt = datetime.strptime(end_time, "%H:%M")
    end_datetime = datetime.combine(end_date, end_time_dt.time())
    end_time_display = end_time

# Combining date and time
start_datetime = datetime.combine(start_date, start_time_dt.time())

# Checking whether the time interval exceeds midnight
if end_datetime <= start_datetime and start_date == end_date:
    end_datetime += timedelta(days=1)

# Calculating UTC time
if time_zone == "CEST":
    start_time_UTC = start_datetime - timedelta(hours=2)
    end_time_UTC = end_datetime - timedelta(hours=2)
elif time_zone == "CET":
    start_time_UTC = start_datetime - timedelta(hours=1)
    end_time_UTC = end_datetime - timedelta(hours=1)
else:
    print("Unknown time zone!")
    exit()

# Formatting the results
start_time_str = start_datetime.strftime("%H:%M")
end_time_str = end_time_display
start_date_banner_str = start_datetime.strftime("%d.%m.%Y")
end_date_banner_str = end_datetime.strftime("%d.%m.%Y")
start_time_UTC_str = start_time_UTC.strftime("%H:%M")
end_time_UTC_str = end_time_UTC.strftime("%H:%M")
start_date_banner_UTC = start_time_UTC.strftime("%d.%m.%Y")
end_date_banner_UTC = end_time_UTC.strftime("%d.%m.%Y")

# Correction of end date for '24:00' hour
if end_time_display == "24:00":
    end_date_banner_UTC = (end_datetime - timedelta(days=1)).strftime("%d.%m.%Y")

# Display of results
print(f"EMEA:")
if start_date_banner == end_date_banner:
    if start_date_banner_str == end_date_banner_UTC:
        if start_date_banner == start_date_banner_UTC:
            print(f"{start_date_banner_str}, {start_time_str} - {end_time_str} {time_zone} "
                f"({end_date_banner_UTC}, {start_time_UTC_str} - {end_time_UTC_str} UTC)")
        else:
            print(f"{start_date_banner_str}, {start_time_str} - {end_time_str} {time_zone} "
                f"({start_time_UTC_str} {start_date_banner_UTC} - {end_time_UTC_str} {end_date_banner_UTC} UTC)")
else:
    print(f"{start_time_str} {start_date_banner_str} - {end_time_str} {end_date_banner_str} {time_zone} "
          f"({start_time_UTC_str} {start_date_banner_UTC} - {end_time_UTC_str} {end_date_banner_UTC} UTC)")

# Calculating the time zone for America and China
start_time_AMERICA = start_time_UTC - timedelta(hours=4)
end_time_AMERICA = end_time_UTC - timedelta(hours=4)
start_time_CHINA = start_time_UTC + timedelta(hours=8)
end_time_CHINA = end_time_UTC + timedelta(hours=8)

#  Formatting the results
start_time_AMERICA_str = start_time_AMERICA.strftime("%H:%M")
end_time_AMERICA_str = end_time_AMERICA.strftime("%H:%M")
start_date_banner_AMERICA = start_time_AMERICA.strftime("%d.%m.%Y")
end_date_banner_AMERICA = end_time_AMERICA.strftime("%d.%m.%Y")

start_time_CHINA_str = start_time_CHINA.strftime("%H:%M")
end_time_CHINA_str = end_time_CHINA.strftime("%H:%M")
start_date_banner_CHINA = start_time_CHINA.strftime("%d.%m.%Y")
end_date_banner_CHINA = end_time_CHINA.strftime("%d.%m.%Y")

# Checking whether the time interval exceeds midnight for America
if end_time_AMERICA <= start_time_AMERICA and start_date_banner_UTC == end_date_banner_UTC:
    end_time_AMERICA += timedelta(days=1)

# Checking whether the time interval exceeds midnight for China
if end_time_CHINA <= start_time_CHINA and start_date_banner_UTC == end_date_banner_UTC:
    end_time_CHINA += timedelta(days=1)



# Display of additional time zonesh
print(f"AMERICA -4 UTC:")
if start_date_banner_AMERICA == end_date_banner_AMERICA:
    print(f"{start_date_banner_AMERICA}, {start_time_AMERICA_str} - {end_time_AMERICA_str} EDT ")
else:
    print(f"{start_time_AMERICA_str} {start_date_banner_AMERICA} - {end_time_AMERICA_str} {end_date_banner_AMERICA} EDT ")

print(f"CHINA +8 UTC:")
if start_date_banner_CHINA == end_date_banner_CHINA:
    print(f"{start_date_banner_CHINA}, {start_time_CHINA_str} - {end_time_CHINA_str} CST ")
else:
    print(f"{start_time_CHINA_str} {start_date_banner_CHINA} - {end_time_CHINA_str} {end_date_banner_CHINA} CST ")