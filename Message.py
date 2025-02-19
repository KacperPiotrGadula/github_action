def main():
    central_application = input("Central Application: ")
    version = input("Version: ")
    date = input("Date (YYYY-MM-DD): ")
    downtime = input("Downtime: ")
    affected_markets = input("Affected markets or regions: ")
    reason_description = input("Reason and short description: ")

    print("\nOutput:\n")
    print(f"Central Application: {central_application}")
    
    affected_systems_mapping = {
        "function": "application_1",
        "service": "application_2"
    }

    central_app_key = central_application.lower().strip()
    if central_app_key in affected_systems_mapping:
        affected_systems = affected_systems_mapping[central_app_key]
        print(f"Affected Systems: {affected_systems}")
    else:
        affected_systems = input("Affected Systems: ")

    print(f"Version: {version}")
    print(f"Date: {date}")
    print(f"Downtime: {downtime}")
    print(f"Affected markets or regions: {affected_markets}")
    
    impact_mapping = {
        "function": "\n- Possible brief interruptions of the service.\n"
                    "- Possible issues with reaching the endpoint.\n",
                    
        "service": "\n- The maintenance will have impact on services.\n"
                         "- Inability to upload file.\n"
                         "- No downtime is expected but if a call fails please retry in few minutes.\n"
    }

    central_app_key = central_application
    if central_app_key in impact_mapping:
        impact = impact_mapping[central_app_key]
        print(f"Impact during the maintenance: {impact}")
    else:
        impact = input("Impact during the maintenance: ")

    print(f"Reason and short description: \n - {reason_description}")

    
    file_name = "output.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Central Application: {central_application}\n")
        file.write(f"Affected Systems: {affected_systems}\n")
        file.write(f"Version: {version}\n")
        file.write(f"Date: {date}\n")
        file.write(f"Downtime: {downtime}\n")
        file.write(f"Affected markets or regions: {affected_markets}\n")
        file.write(f"Impact during the maintenance: {impact}\n")
        file.write(f"Reason and short description:\n - {reason_description}\n")
    print(f"The data was saved in a file: {file_name}")

if __name__ == "__main__":
    main()