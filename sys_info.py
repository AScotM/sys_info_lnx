import platform
import json

def get_system_info():
    system_info = platform.uname()
    return {
        "System": system_info.system,
        "Node Name": system_info.node,
        "Release": system_info.release,
        "Version": system_info.version,
        "Machine": system_info.machine,
        "Processor": system_info.processor
    }

def main():
    info = get_system_info()
    
    # Ask user for output preference
    output_type = input("Do you want JSON output? (y/n): ").lower()
    
    if output_type == 'y':
        # JSON output
        print(json.dumps(info, indent=2))
    else:
        # Regular text output
        print("System Information:")
        for key, value in info.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
