from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
import calendar
import sys

def generate_output():

    output_lines = []

    # Inputs for region, timezone, and time range
    selected_region = sys.argv[1].upper()
    selected_timezone = sys.argv[2].upper()
    date1, date2, time1, time2 = sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]

    # Updated Timezone definitions with corrected region mapping
    TIMEZONE_MAP = {
        "CEST": ZoneInfo("Europe/Warsaw"),
        "CET": ZoneInfo("Europe/Warsaw"),
        "AMERICA": ZoneInfo("America/New_York"),  # Handles EST/EDT automatically
        "CHINA": ZoneInfo("Asia/Shanghai"),       # CST for China Standard Time
        "UTC": ZoneInfo("UTC")
    }

    def parse_datetime(date_str, time_str, tz):
        return datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M").replace(tzinfo=tz)

    def convert_timezones(start_dt, end_dt, tz):
        start, end = start_dt.astimezone(tz), end_dt.astimezone(tz)
        if end <= start and start.date() == end.date():
            end += timedelta(days=1)
        return start, end

    def get_utc_offset(dt):
        hours = int(dt.utcoffset().total_seconds() // 3600)
        sign = "+" if hours >= 0 else "-"
        return f"UTC{sign}{abs(hours)}"

    def format_date_with_day(dt):
        return dt.strftime(f"%d.%m.%Y ({calendar.day_name[dt.weekday()]})")

    def format_region_output(region, base_tz, start_datetime, end_datetime, time2):
        region_tz = TIMEZONE_MAP[base_tz] if region == "EMEA" else TIMEZONE_MAP[region]
        start_dt_region, end_dt_region = convert_timezones(start_datetime, end_datetime, region_tz)
        start_dt_utc, end_dt_utc = convert_timezones(start_datetime, end_datetime, TIMEZONE_MAP["UTC"])

        start_time_str = start_dt_region.strftime("%H:%M")
        end_time_str = "24:00" if time2 == "24:00" else end_dt_region.strftime("%H:%M")
        start_date_str = format_date_with_day(start_dt_region)
        end_date_str = format_date_with_day(end_dt_region)

        start_time_utc_str = start_dt_utc.strftime("%H:%M")
        end_time_utc_str = end_dt_utc.strftime("%H:%M")
        start_date_utc_str = format_date_with_day(start_dt_utc)
        end_date_utc_str = format_date_with_day(end_dt_utc)

        tz_str = f"{start_dt_region.strftime('%Z')} ({get_utc_offset(start_dt_region)})"

        if region == "EMEA":
            output_lines.append("EMEA:")
            if start_date_str == end_date_utc_str:
                output_lines.append(
                    f"{start_date_str}, {start_time_str} - {end_time_str} {base_tz} "
                    f"({start_date_utc_str} {start_time_utc_str} - {end_time_utc_str} UTC)"
                )
            else:
                output_lines.append(
                    f"{start_time_str} {start_date_str} - {end_time_str} {end_date_utc_str} {base_tz} "
                    f"({start_time_utc_str} {start_date_utc_str} - {end_time_utc_str} {end_date_utc_str} UTC)"
                )
        else:
            output_lines.append(
                f"\n{region} ({tz_str}, 12h format - A.M./P.M.):"
            )
            if start_date_str == end_date_str:
                output_lines.append(
                    f"{start_date_str}, {start_dt_region.strftime('%I:%M %p')} - {end_dt_region.strftime('%I:%M %p')} {tz_str}"
                )
            else:
                output_lines.append(
                    f"{start_dt_region.strftime('%I:%M %p')} {start_date_str} - {end_dt_region.strftime('%I:%M %p')} {end_date_str} {tz_str}"
                )

    # Process only the selected region
    if selected_region in ["EMEA", "AMERICA", "CHINA"] and selected_timezone in ["CEST", "CET"]:
        base_timezone = selected_timezone if selected_region == "EMEA" else selected_region
        start_datetime = parse_datetime(date1, time1, TIMEZONE_MAP[base_timezone])
        end_datetime = parse_datetime(date2, time2, TIMEZONE_MAP[base_timezone])

        if time2 == "24:00":
            end_datetime = parse_datetime(date2, "00:00", TIMEZONE_MAP[base_timezone]) + timedelta(days=1)

        if end_datetime <= start_datetime:
            end_datetime += timedelta(days=1)

        format_region_output(selected_region, base_timezone, start_datetime, end_datetime, time2)
    else:
        output_lines.append("Invalid region or timezone specified. Please select from EMEA, AMERICA, CHINA and CEST/CET.")

    with open("output_banner.txt", "w") as file:
        file.write("\n".join(output_lines))

    return "\n".join(output_lines)

if __name__ == "__main__":
    print(generate_output())