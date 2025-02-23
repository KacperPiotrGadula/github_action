# 📢 Communication for Applications

---

## 📖 **Project Description**  
This Python script generates a structured communication report for application maintenance activities. It takes user inputs such as the central application name, version, maintenance date, downtime, affected markets, and reason for maintenance, then outputs the results to the console (with rich formatting) and saves them into a text file (`communication_for_applications.txt`).

The script uses the `rich` library to format console output for better readability and generates a consistent communication template useful for operational updates.

---

## ⚡ **Key Features**
- 🖋 **Rich-formatted output** for clear terminal display using the `rich` library  
- 📄 **Generates a text report** (`communication_for_applications.txt`)  
- 🌎 **Maps central applications** to affected systems and impact descriptions  
- ⚙️ **Takes command-line arguments** for automation in CI/CD pipelines  
- 💡 **Handles application-specific impact descriptions**  

---

## ✅ **Requirements**
- Python 3.9+  
- `rich` library (for formatted console output)

### ⚡ **Install Dependencies**
```
pip install rich
```

---
# 🚀 How to Run the Script
```
python communication_script.py <CENTRAL_APPLICATION> <VERSION> <DATE> <DOWNTIME> <AFFECTED_MARKETS> <REASON_DESCRIPTION>
```

---
# 📅 Example
python communication_script.py ``AstroSync v1.4.0 2024-02-25 "2 hours" "EU, US" "Routine maintenance and performance updates."``

---
# 📝 Input Parameters

| Parameter                | Type   | Description                                                           | Example                     |
|--------------------------|--------|-----------------------------------------------------------------------|-----------------------------|
| `CENTRAL_APPLICATION`    | string | Name of the central application (`AstroSync`, `NeoCore`)              | `AstroSync`                 |
| `VERSION`                | string | Version number for the update                                         | `v1.4.0`                    |
| `DATE`                   | string | Scheduled date for maintenance (`YYYY-MM-DD` format)                  | `2024-02-25`                |
| `DOWNTIME`               | string | Expected downtime duration                                            | `2 hours`                   |
| `AFFECTED_MARKETS`       | string | Regions or markets affected by the downtime                           | `EU, US`                    |
| `REASON_DESCRIPTION`     | string | Short description explaining the reason for maintenance               | `Routine performance updates`|


---
# 💾 Output File (communication_for_applications.txt)

```
Central Application: AstroSync
Affected Systems: SigmaFlow
Version: v1.4.0
Date: 2024-02-25
Downtime: 2 hours
Affected markets or regions: EU, US
Impact during the maintenance:
• Data synchronization service in multi-system environments.

Reason and short description:
• Routine maintenance and performance updates.
```