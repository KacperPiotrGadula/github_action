from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
import calendar
import sys

def generate_output():

    output_lines = []

    # Interactive input from console
    time_zone = sys.argv[1]
    start_date_banner = sys.argv[2]
    end_date_banner = sys.argv[3]
    start_time = sys.argv[4]
    end_time = sys.argv[5]

    # Timezone definitions
    TIMEZONE_MAP = {
        "CEST": ZoneInfo("Europe/Warsaw"),
        "CET": ZoneInfo("Europe/Warsaw"),
        "AMERICA": ZoneInfo("America/New_York"),
        "CHINA": ZoneInfo("Asia/Shanghai"),
        "UTC": ZoneInfo("UTC")
    }

    # Validation of time zone
    if time_zone not in TIMEZONE_MAP:
        print(f"Unknown time zone: {time_zone}")
        exit(1)

    # Parsing datetime with timezone
    def parse_datetime(date_str, time_str, tz):
        dt = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M").replace(tzinfo=tz)
        return dt

    start_datetime = parse_datetime(start_date_banner, start_time, TIMEZONE_MAP[time_zone])

    if end_time == "24:00":
        end_datetime = parse_datetime(end_date_banner, "00:00", TIMEZONE_MAP[time_zone]) + timedelta(days=1)
    else:
        end_datetime = parse_datetime(end_date_banner, end_time, TIMEZONE_MAP[time_zone])

    # Checking whether the time interval exceeds midnight
    if end_datetime <= start_datetime:
        end_datetime += timedelta(days=1)

    # Converting to UTC and other time zones
    def convert_timezones(start_dt, end_dt, tz):
        start = start_dt.astimezone(tz)
        end = end_dt.astimezone(tz)
        if end <= start and start.date() == end.date():
            end += timedelta(days=1)
        return start, end

    start_time_UTC, end_time_UTC = convert_timezones(start_datetime, end_datetime, TIMEZONE_MAP["UTC"])
    start_time_AMERICA, end_time_AMERICA = convert_timezones(start_time_UTC, end_time_UTC, TIMEZONE_MAP["AMERICA"])
    start_time_CHINA, end_time_CHINA = convert_timezones(start_time_UTC, end_time_UTC, TIMEZONE_MAP["CHINA"])

    # Function to calculate UTC offset
    def get_utc_offset(dt):
        offset_seconds = dt.utcoffset().total_seconds()
        hours = int(offset_seconds // 3600)
        sign = "+" if hours >= 0 else "-"
        return f"UTC{sign}{abs(hours)}"

    america_timezone_str = f"{start_time_AMERICA.strftime('%Z')}"
    china_timezone_str = f"{start_time_CHINA.strftime('%Z')}"

    def format_date_with_day(dt):
        day_name = calendar.day_name[dt.weekday()]
        return dt.strftime(f"%d.%m.%Y ({day_name})")

    # ✅ Dodane funkcje do formatowania daty w stylu "Feb, 26th, 2025"
    def format_day_with_suffix(day):
        if 11 <= day <= 13:
            return f"{day}th"
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        return f"{day}{suffixes.get(day % 10, 'th')}"

    def format_date_american_style(dt):
        return dt.strftime("%b") + f", {format_day_with_suffix(dt.day)}, {dt.year}"

    # Formatting the results
    start_time_str = start_datetime.strftime("%H:%M")
    end_time_str = "24:00" if end_time == "24:00" else end_datetime.strftime("%H:%M")
    start_date_banner_str = format_date_with_day(start_datetime)
    end_date_banner_str = format_date_with_day(end_datetime)

    start_time_UTC_str = start_time_UTC.strftime("%H:%M")
    end_time_UTC_str = end_time_UTC.strftime("%H:%M")
    start_date_banner_UTC = format_date_with_day(start_time_UTC)
    end_date_banner_UTC = format_date_with_day(end_time_UTC)

    start_time_AMERICA_str = start_time_AMERICA.strftime("%I:%M %p")
    end_time_AMERICA_str = end_time_AMERICA.strftime("%I:%M %p")

    # ✅ Zmienione tylko tutaj - użycie nowej funkcji formatowania daty
    start_date_banner_AMERICA = format_date_american_style(start_time_AMERICA)
    end_date_banner_AMERICA = format_date_american_style(end_time_AMERICA)

    start_time_CHINA_str = start_time_CHINA.strftime("%I:%M %p")
    end_time_CHINA_str = end_time_CHINA.strftime("%I:%M %p")
    start_date_banner_CHINA = format_date_with_day(start_time_CHINA)
    end_date_banner_CHINA = format_date_with_day(end_time_CHINA)

    # Display of results
    output_lines.append(f"EMEA:")
    if start_date_banner_str == end_date_banner_UTC:
        output_lines.append(f"{start_date_banner_str}, {start_time_str} - {end_time_str} {time_zone} "
        f"({start_date_banner_UTC} {start_time_UTC_str}  - {end_time_UTC_str} UTC)")
    else:
        output_lines.append(f"{start_time_str} {start_date_banner_str} - {end_time_str} {end_date_banner_UTC} {time_zone}" f" ({start_time_UTC_str} {start_date_banner_UTC} - {end_time_UTC_str} {end_date_banner_UTC} UTC)")

    # ✅ AMERICA z formatem "Feb, 26th, 2025"
    output_lines.append(f"\nAMERICA ({america_timezone_str} ({get_utc_offset(start_time_AMERICA)}), 12h format - A.M./P.M.):")
    if start_date_banner_AMERICA == end_date_banner_AMERICA:
        output_lines.append(f"{start_date_banner_AMERICA}, {start_time_AMERICA_str} - {end_time_AMERICA_str} {america_timezone_str}")
    else:
        output_lines.append(f"{start_time_AMERICA_str} {start_date_banner_AMERICA} - {end_time_AMERICA_str} {end_date_banner_AMERICA} {america_timezone_str}")

    output_lines.append(f"\nCHINA ({china_timezone_str} ({get_utc_offset(start_time_CHINA)}), 12h format - A.M./P.M.):")
    if start_date_banner_CHINA == end_date_banner_CHINA:
        output_lines.append(f"{start_date_banner_CHINA}, {start_time_CHINA_str} - {end_time_CHINA_str} {china_timezone_str}")
    else:
        output_lines.append(f"{start_time_CHINA_str} {start_date_banner_CHINA} - {end_time_CHINA_str} {end_date_banner_CHINA} {china_timezone_str}")

    # Scal całość do jednej zmiennej
    output_content = "\n".join(output_lines)

    with open("output_banner.txt", "w") as file:
        file.write(output_content)

    return output_content

if __name__ == "__main__":
    output_summary = generate_output()
    print(output_summary)