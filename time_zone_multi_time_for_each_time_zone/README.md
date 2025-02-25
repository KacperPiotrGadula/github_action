# 🌍 Time Zone Generation Script

---

## 📖 Project Description  
This Python script generates time schedules across multiple time zones (EMEA, AMERICA, CHINA) based on provided dates and times.  
It automatically adjusts times to the appropriate time zones, accounts for UTC offsets, and handles cross-midnight intervals (e.g., end time at 24:00).  
The output is saved to the `output_banner.txt` file and displayed in the console.

---

## ⚡ Script Features
- 🌐 Time conversion between zones: CEST/CET, AMERICA (New York), CHINA (Shanghai), UTC  
- 🕑 Supports 12-hour (AM/PM) and 24-hour time formats  
- 🏃 Handles cross-midnight intervals (e.g., end time at 24:00)  
- 📝 Automatically calculates and displays UTC offsets  
- 💾 Output generated in the `output_banner.txt` file  
- ⚙️ Accepts input arguments from the command line  

---

## 🚀 How to Run

### ✅ Requirements
- Python 3.9+  
- Support for `zoneinfo` (available in Python 3.9+)

### ⚡ Installation (optional)
```
pip install backports.zoneinfo
```

# 💡 Running the Script
```
python Time_zone_generation.py <TIMEZONE> <START_DATE> <END_DATE> <START_TIME> <END_TIME>
```

## 📅 Example

python Time_zone_generation.py ``CEST 21.02.2024 22.02.2024 14:00 24:00``

# 📝 Input Parameters

## 📝 Input Parameters

| Parameter    | Type   | Description                                                   | Example          |
|--------------|--------|---------------------------------------------------------------|------------------|
| `TIMEZONE`   | string | Time zone to be used. Supported values: `CEST`, `CET`, `AMERICA`, `CHINA`, `UTC`. | `CEST`           |
| `START_DATE` | string | Start date in `DD.MM.YYYY` format.                            | `21.02.2024`     |
| `END_DATE`   | string | End date in `DD.MM.YYYY` format.                              | `22.02.2024`     |
| `START_TIME` | string | Start time in `HH:MM` format (24-hour).                       | `14:00`          |
| `END_TIME`   | string | End time in `HH:MM` format (24-hour) or `24:00` for midnight. | `24:00`          |

# 🖨 Sample Output (output_banner.txt)
```
EMEA:  
21.02.2024 (Wednesday), 14:00 - 24:00 CEST (21.02.2024 (Wednesday) 13:00 - 23:00 UTC)

AMERICA (EST (UTC-5), 12h format - A.M./P.M.):  
21.02.2024 (Wednesday), 08:00 AM - 06:00 PM EST

CHINA (CST (UTC+8), 12h format - A.M./P.M.):  
22.02.2024 (Thursday), 09:00 PM - 07:00 AM CST
```