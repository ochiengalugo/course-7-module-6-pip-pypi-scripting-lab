from datetime import datetime
import os

def generate_log(log_data):
    # 1. Ensure the input is strictly a list (Raises ValueError if invalid)
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list of log entries.")
    
    # 2. Strict filename pattern matching: log_YYYYMMDD.txt
    timestamp = datetime.now().strftime("%Y%m%D").replace("/", "") 
    # Or cleaner:
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"log_{timestamp}.txt"
    
    # 3. Write contents directly to the file (handles empty lists cleanly)
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
            
    # 4. Print confirmation message including the filename
    print(f"Success: Log file created successfully at {filename}")
    
    return filename

if __name__ == "__main__":
    # Test sample data locally to see it work
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    try:
        generate_log(sample_data)
    except Exception as e:
        print(f"Error: {e}")