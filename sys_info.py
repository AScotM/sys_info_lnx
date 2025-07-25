import platform
import json

def get_system_info():
    """
    Retrieve system information using the platform module.
    Returns a dictionary with system details or None if an error occurs.
    """
    try:
        system_info = platform.uname()
        return {
            "System": system_info.system or "N/A",
            "Node Name": system_info.node or "N/A",
            "Release": system_info.release or "N/A",
            "Version": system_info.version or "N/A",
            "Machine": system_info.machine or "N/A",
            "Processor": system_info.processor or "N/A"
        }
    except Exception as e:
        print(f"An error occurred while retrieving system information: {e}")
        return None

def main():
    """
    Main function to retrieve and display system information.
    Prompts user for output format (JSON or text) and displays the result.
    """
    try:
        info = get_system_info()
        if info is None:
            print("Failed to retrieve system information.")
            return

        while True:
            try:
                output_type = input("Do you want JSON output? (y/n): ").lower()
                if output_type in ('y', 'n'):
                    break
                print("Please enter 'y' for yes or 'n' for no.")
            except EOFError:
                print("\nEOF received, defaulting to text output.")
                output_type = 'n'
                break

        if output_type == 'y':
            print(json.dumps(info, indent=2))
        else:
            print("System Information:")
            for key, value in info.items():
                print(f"{key:<12}: {value}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
