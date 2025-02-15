from datetime import datetime, timedelta

# Pobranie strefy czasowej
time_zone = input("Podaj strefę czasową (CEST lub CET): ")

# Pobranie daty startowej i końcowej
start_date_banner = input("Podaj datę startową (DD.MM.YYYY): ")
end_date_banner = input("Podaj datę końcową (DD.MM.YYYY): ")

# Pobranie godziny startu i zakończenia
start_time = input("Podaj godzinę startu (HH:MM): ")
end_time = input("Podaj godzinę zakończenia (HH:MM): ")

# Konwersja dat na obiekty datetime
start_date = datetime.strptime(start_date_banner, "%d.%m.%Y")
end_date = datetime.strptime(end_date_banner, "%d.%m.%Y")
start_time_dt = datetime.strptime(start_time, "%H:%M")

# Obsługa specjalnego przypadku dla godziny zakończenia '24:00'
if end_time == "24:00":
    end_time_dt = datetime.strptime("00:00", "%H:%M") + timedelta(days=1)
    end_datetime = datetime.combine(end_date, end_time_dt.time())
    end_time_display = "24:00"
else:
    end_time_dt = datetime.strptime(end_time, "%H:%M")
    end_datetime = datetime.combine(end_date, end_time_dt.time())
    end_time_display = end_time

# Łączenie daty i czasu
start_datetime = datetime.combine(start_date, start_time_dt.time())

# Sprawdzenie, czy przedział czasowy przekracza północ
if end_datetime <= start_datetime and start_date == end_date:
    end_datetime += timedelta(days=1)

# Obliczanie czasu UTC
if time_zone == "CEST":
    start_time_UTC = start_datetime - timedelta(hours=2)
    end_time_UTC = end_datetime - timedelta(hours=2)
elif time_zone == "CET":
    start_time_UTC = start_datetime - timedelta(hours=1)
    end_time_UTC = end_datetime - timedelta(hours=1)
else:
    print("Nieznana strefa czasowa!")
    exit()

# Formatyzowanie wyników
start_time_str = start_datetime.strftime("%H:%M")
end_time_str = end_time_display
start_date_banner_str = start_datetime.strftime("%d.%m.%Y")
end_date_banner_str = end_datetime.strftime("%d.%m.%Y")
start_time_UTC_str = start_time_UTC.strftime("%H:%M")
end_time_UTC_str = end_time_UTC.strftime("%H:%M")
start_date_banner_UTC = start_time_UTC.strftime("%d.%m.%Y")
end_date_banner_UTC = end_time_UTC.strftime("%d.%m.%Y")

# Poprawienie daty końcowej w przypadku godziny '24:00'
if end_time_display == "24:00":
    end_date_banner_UTC = (end_datetime - timedelta(days=1)).strftime("%d.%m.%Y")

# Wyświetlanie wyników
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

# Obliczanie strefy czasowej dla Ameryki oraz China
start_time_AMERICA = start_time_UTC - timedelta(hours=4)
end_time_AMERICA = end_time_UTC - timedelta(hours=4)
start_time_CHINA = start_time_UTC + timedelta(hours=8)
end_time_CHINA = end_time_UTC + timedelta(hours=8)

# Formatyzowanie wyników
start_time_AMERICA_str = start_time_AMERICA.strftime("%H:%M")
end_time_AMERICA_str = end_time_AMERICA.strftime("%H:%M")
start_date_banner_AMERICA = start_time_AMERICA.strftime("%d.%m.%Y")
end_date_banner_AMERICA = end_time_AMERICA.strftime("%d.%m.%Y")

start_time_CHINA_str = start_time_CHINA.strftime("%H:%M")
end_time_CHINA_str = end_time_CHINA.strftime("%H:%M")
start_date_banner_CHINA = start_time_CHINA.strftime("%d.%m.%Y")
end_date_banner_CHINA = end_time_CHINA.strftime("%d.%m.%Y")

# Sprawdzenie, czy przedział czasowy przekracza północ dla Ameryki
if end_time_AMERICA <= start_time_AMERICA and start_date_banner_UTC == end_date_banner_UTC:
    end_time_AMERICA += timedelta(days=1)

# Sprawdzenie, czy przedział czasowy przekracza północ dla Chin
if end_time_CHINA <= start_time_CHINA and start_date_banner_UTC == end_date_banner_UTC:
    end_time_CHINA += timedelta(days=1)



# Wyświetlanie dodatkowych stref czasowych
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