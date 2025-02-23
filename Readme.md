# 🚀 **Project: Automated Python Workflows for Application Communication & Time Zone Banners**

---

## 📖 **Project Overview**  
This repository contains two automated Python scripts integrated with GitHub Actions workflows for generating:  
1. 📢 **Application Communication Reports** – Generates a structured report about application maintenance activities.  
2. 🕒 **Time Zone Banners** – Creates banners displaying time schedules across multiple time zones.

Both workflows are designed to run directly through **GitHub Actions** using **workflow dispatch**, allowing users to trigger them manually with custom inputs.

---

## 🗂 **Repository Structure**

```
/<root>
│
├── communication_for_applications/
│   └── Communication.py                # Python script for communication report generation
│
├── time_zone/
│   └── Time_zone_generation.py          # Python script for time zone banner generation
│
├── .github/
│   └── workflows/
│       ├── build_communication.yml      # GitHub Actions workflow for communication generation
│       └── build_banner.yml             # GitHub Actions workflow for time zone banner generation
│
└── README.md                            # Main documentation (this file)
```

---

## ⚡ **Key Functionalities**

### 1️⃣ **Communication Generation Script (`Communication.py`):**
- 📝 Generates communication reports for application maintenance.  
- 🌍 Maps central applications to affected systems and impacts.  
- 📄 Outputs reports to `communication_for_applications.txt`.  
- ✨ Rich-formatted terminal output using the `rich` Python library.

---

### 2️⃣ **Time Zone Banner Generation Script (`Time_zone_generation.py`):**
- 🌐 Converts and displays time schedules for EMEA, AMERICA, and CHINA time zones.  
- 🕑 Supports 12-hour (AM/PM) and 24-hour time formats.  
- 📅 Handles cross-midnight intervals.  
- 💾 Outputs banners to `output_banner.txt`.

---

## 🚀 **GitHub Actions Workflows**

### ⚙️ **1. Build Communication Workflow (`build_communication.yml`)**

#### **Trigger:** Manual (via GitHub UI - workflow dispatch)

#### **Inputs:**
| Parameter               | Type   | Description                                              | Example           |
|-------------------------|--------|----------------------------------------------------------|-------------------|
| `CENTRAL_APPLICATION`   | choice | Central app (`AstroSync`, `NeoCore`)                     | `AstroSync`       |
| `VERSION`               | string | Version number                                           | `v1.4.0`          |
| `DATE`                  | string | Maintenance date (`YYYY-MM-DD`)                          | `2024-02-25`      |
| `DOWNTIME`              | choice | Is downtime expected? (`true`/`false`)                   | `true`            |
| `CUSTOM_DOWNTIME`       | string | Downtime period (if applicable)                          | `2 hours`         |
| `AFFECTED_MARKETS`      | string | Affected regions or markets                              | `EU, US`          |
| `REASON_DESCRIPTION`    | string | Reason and short description of the maintenance           | `Performance fix` |

#### 💡 **How to trigger:**
1. Go to **GitHub → Actions** tab in this repository.
2. Select **"Build Communication"** workflow.
3. Click on **"Run workflow"** and fill in the required input fields.

#### 🏗 **What it does:**
- Installs dependencies (`rich` library).  
- Sets environment variables based on inputs.  
- Runs `Communication.py` and generates `communication_for_applications.txt`.  
- Uploads the output as an artifact for download.  

---

### ⚙️ **2. Build Banner Workflow (`build_banner.yml`)**

#### **Trigger:** Manual (via GitHub UI - workflow dispatch)

#### **Inputs:**
| Parameter    | Type   | Description                                  | Example       |
|--------------|--------|----------------------------------------------|---------------|
| `TIMEZONE`   | string | Time zone (`CEST` or `CET`)                  | `CEST`        |
| `DATE1`      | string | Start date (`DD.MM.YYYY`)                    | `21.02.2024`  |
| `DATE2`      | string | End date (`DD.MM.YYYY`)                      | `22.02.2024`  |
| `TIME1`      | string | Start time (`HH:MM`)                         | `14:00`       |
| `TIME2`      | string | End time (`HH:MM` or `24:00`)                | `24:00`       |

#### 💡 **How to trigger:**
1. Go to **GitHub → Actions** tab in this repository.
2. Select **"Build Banner"** workflow.
3. Click on **"Run workflow"** and provide the required inputs.

#### 🏗 **What it does:**
- Installs Python dependencies (`tzdata`).  
- Sets environment variables based on user inputs.  
- Runs `Time_zone_generation.py` and generates `output_banner.txt`.  
- Uploads the banner file as an artifact for download.

---

## 💡 **How to Use GitHub Actions in this Repository**

1. **Navigate to the Actions Tab**:  
   Click on the **"Actions"** tab in this repository.

2. **Choose the Workflow**:  
   - Select **"Build Communication"** to generate communication reports.  
   - Select **"Build Banner"** to create time zone banners.

3. **Trigger the Workflow**:  
   - Click the **"Run workflow"** button.  
   - Fill in the required input parameters.  
   - Click **"Run workflow"** to execute.

4. **Download the Output**:  
   After successful execution:
   - Navigate to the workflow run.
   - Scroll down to the **Artifacts** section.
   - Download the generated `.txt` files:
     - `communication_for_applications.txt` for communication reports.
     - `output_banner.txt` for time zone banners.

---

## 🛠 **Example Output Files**

### 📜 **communication_for_applications.txt**  
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
• Performance updates and optimizations.
```

---

### 📜 **output_banner.txt**  
```
EMEA:
21.02.2024 (Wednesday), 14:00 - 24:00 CEST (21.02.2024 (Wednesday) 13:00 - 23:00 UTC)

AMERICA (EST (UTC-5), 12h format - A.M./P.M.):
21.02.2024 (Wednesday), 08:00 AM - 06:00 PM EST

CHINA (CST (UTC+8), 12h format - A.M./P.M.):
22.02.2024 (Thursday), 09:00 PM - 07:00 AM CST
```

---

## 🌟 **Notes:**
- Both workflows are **manually triggered** via GitHub's **workflow_dispatch** event.  
- Ensure that the **file paths** in workflows match your repository's structure.  
- Python dependencies (`rich`, `tzdata`) are installed automatically during workflow runs.  
- Output files are available as **artifacts** after workflow completion.