from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
import calendar
import sys

def generate_output():

    output_lines = []

    # Inputs for EMEA, America, and China
    timezones = [
        (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], "EMEA"),
        (sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], "AMERICA"),
        (sys.argv[11], sys.argv[12], sys.argv[13], sys.argv[14], sys.argv[15], "CHINA")
    ]

    # Timezone definitions
    TIMEZONE_MAP = {
        "CEST": ZoneInfo("Europe/Warsaw"),
        "CET": ZoneInfo("Europe/Warsaw"),
        "AMERICA": ZoneInfo("America/New_York"),
        "CHINA": ZoneInfo("Asia/Shanghai"),
        "UTC": ZoneInfo("UTC")
    }

    def parse_datetime(date_str, time_str, tz):
        dt = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M").replace(tzinfo=tz)
        return dt

    def convert_timezones(start_dt, end_dt, tz):
        start = start_dt.astimezone(tz)
        end = end_dt.astimezone(tz)
        if end <= start and start.date() == end.date():
            end += timedelta(days=1)
        return start, end

    def get_utc_offset(dt):
        offset_seconds = dt.utcoffset().total_seconds()
        hours = int(offset_seconds // 3600)
        sign = "+" if hours >= 0 else "-"
        return f"UTC{sign}{abs(hours)}"

    def format_date_with_day(dt):
        day_name = calendar.day_name[dt.weekday()]
        return dt.strftime(f"%d.%m.%Y ({day_name})")

    def format_region_output(region, tz, start_datetime, end_datetime, time2):
        start_utc, end_utc = convert_timezones(start_datetime, end_datetime, TIMEZONE_MAP["UTC"])

        if region == "EMEA":
            start_time_str = start_datetime.strftime("%H:%M")
            end_time_str = "24:00" if time2 == "24:00" else end_datetime.strftime("%H:%M")
            start_date_banner_str = format_date_with_day(start_datetime)
            end_date_banner_utc = format_date_with_day(end_utc)
            start_time_utc_str = start_utc.strftime("%H:%M")
            end_time_utc_str = end_utc.strftime("%H:%M")

            if start_date_banner_str == end_date_banner_utc:
                return [
                    f"{region}:",
                    f"{start_date_banner_str}, {start_time_str} - {end_time_str} {tz} "
                    f"({end_date_banner_utc} {start_time_utc_str} - {end_time_utc_str} UTC)"
                ]
            else:
                return [
                    f"{region}:",
                    f"{start_time_str} {start_date_banner_str} - {end_time_str} {end_date_banner_utc} {tz} "
                    f"({start_time_utc_str} {start_date_banner_str} - {end_time_utc_str} {end_date_banner_utc} UTC)"
                ]

        else:
            start_time_str = start_datetime.strftime("%I:%M %p")
            end_time_str = end_datetime.strftime("%I:%M %p")
            start_date_banner_str = format_date_with_day(start_datetime)
            end_date_banner_str = format_date_with_day(end_datetime)
            tz_str = f"{start_datetime.strftime('%Z')} ({get_utc_offset(start_datetime)})"

            if start_date_banner_str == end_date_banner_str:
                return [
                    f"\n{region} ({tz_str}, 12h format - A.M./P.M.):",
                    f"{start_date_banner_str}, {start_time_str} - {end_time_str} {start_datetime.strftime('%Z')}"
                ]
            else:
                return [
                    f"\n{region} ({tz_str}, 12h format - A.M./P.M.):",
                    f"{start_time_str} {start_date_banner_str} - {end_time_str} {end_date_banner_str} {start_datetime.strftime('%Z')}"
                ]

    # Process each region
    for tz, date1, date2, time1, time2, region in timezones:
        if tz not in TIMEZONE_MAP:
            print(f"Unknown time zone: {tz}")
            exit(1)

        start_datetime = parse_datetime(date1, time1, TIMEZONE_MAP[tz])
        end_datetime = parse_datetime(date2, time2, TIMEZONE_MAP[tz])

        if time2 == "24:00":
            end_datetime = parse_datetime(date2, "00:00", TIMEZONE_MAP[tz]) + timedelta(days=1)

        if end_datetime <= start_datetime:
            end_datetime += timedelta(days=1)

        output_lines.extend(format_region_output(region, tz, start_datetime, end_datetime, time2))

    output_content = "\n".join(output_lines)

    with open("output_banner.txt", "w") as file:
        file.write(output_content)

    return output_content

if __name__ == "__main__":
    output_summary = generate_output()
    print(output_summary)