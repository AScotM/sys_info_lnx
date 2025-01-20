import platform
import json

def get_system_info():
    try:
        system_info = platform.uname()
        return {
            "System": system_info.system,
            "Node Name": system_info.node,
            "Release": system_info.release,
            "Version": system_info.version,
            "Machine": system_info.machine,
            "Processor": system_info.processor
        }
    except AttributeError as e:
        # If some attributes are not available, we'll just return what we can
        return {
            attr: getattr(system_info, attr, "N/A") for attr in 
            ['system', 'node', 'release', 'version', 'machine', 'processor']
        }
    except Exception as e:
        print(f"An error occurred while retrieving system information: {e}")
        return {}  # Return an empty dictionary if there's a severe error

def main():
    try:
        info = get_system_info()
        
        # Ask user for output preference
        while True:
            output_type = input("Do you want JSON output? (y/n): ").lower()
            if output_type in ('y', 'n'):
                break
            print("Please enter 'y' for yes or 'n' for no.")
        
        if output_type == 'y':
            # JSON output
            try:
                print(json.dumps(info, indent=2))
            except TypeError as e:
                print(f"Error in JSON formatting: {e}")
        else:
            # Regular text output
            print("System Information:")
            for key, value in info.items():
                print(f"{key}: {value}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
