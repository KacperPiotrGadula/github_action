from rich import print
import sys

def main():
    central_application = sys.argv[1]
    version = sys.argv[2]
    date = sys.argv[3]
    downtime = sys.argv[4]
    affected_markets = sys.argv[5]
    reason_description = sys.argv[6]

    print("\nOutput:\n")
    print(f"[bold]Central Application:[/bold] {central_application}")
    
    affected_systems_mapping = {
        "AstroSync": "SigmaFlow",
        "NeoCore": "OptiNet, DataPulse",
    }
    
    if central_application in affected_systems_mapping:
        affected_systems = affected_systems_mapping[central_application]
        print(f"[bold]Affected Systems:[/bold] {affected_systems}")

    print(f"[bold]Version:[/bold] {version}")
    print(f"[bold]Date:[/bold] {date}")
    print(f"[bold]Downtime:[/bold] {downtime}")
    print(f"[bold]Affected markets or regions:[/bold] {affected_markets}")
    
    impact_mapping = {
        "AstroSync":    "\n• Data synchronization service in multi-system environments. \n"
        "NeoCore":      "\n• Real-time data management core. \n"
    }

    if central_application in impact_mapping:
        impact = impact_mapping[central_application]
        print(f"[bold]Impact during the maintenance:[/bold] {impact}")

    print(f"[bold]Reason and short description:[/bold] \n • {reason_description}")

    
    file_name = "communication_for_applications.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Central Application: {central_application}\n")
        file.write(f"Affected Systems: {affected_systems}\n")
        file.write(f"Version: {version}\n")
        file.write(f"Date: {date}\n")
        file.write(f"Downtime: {downtime}\n")
        file.write(f"Affected markets or regions: {affected_markets}\n")
        file.write(f"Impact during the maintenance: {impact}\n")
        file.write(f"Reason and short description:\n• {reason_description}\n")

if __name__ == "__main__":
    main()