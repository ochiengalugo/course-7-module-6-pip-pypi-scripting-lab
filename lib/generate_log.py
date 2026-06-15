from datetime import datetime
import requests

def fetch_data():
    # URL provided in Step 4 of the lab instructions
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Fetch the API data
    post_data = fetch_data()
    
    if post_data:
        # Define mock log entry data matching Step 2 instructions
        log_data = ["User logged in", "User updated profile", "Report exported"]
        
        # Format the unique filename: log_YYYY-MM-DD_HH-MM-SS.txt
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"log_{timestamp}.txt"
        
        # Write the log data and the fetched API title to the file
        with open(filename, "w") as file:
            for entry in log_data:
                file.write(f"{entry}\n")
            
            # Appending API content as requested in Step 4
            api_title = post_data.get("title", "No title found")
            file.write(f"Fetched Post Title: {api_title}\n")
            
        print(f"Log written to {filename}")

if __name__ == "__main__":
    main()