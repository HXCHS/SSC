import os
import time
import pyfiglet
import subprocess

from colorama import init, Fore, Back, Style
init()

# Sample user data (replace this with reading from the 'logins' file)
users = {
    "aearnes01": {"password": "password", "clearance_level": "SSC"},
    "dragondung": {"password": "bigdickrandy", "clearance_level": "SSC"},
    "daroon": {"password": "sailor", "clearance_level": "Student"}
}

# Sample files data with classification levels (replace this with reading from directories)
files = {
    "SSC-Agent-List": {"classification": "SSC", "content": "Project Leader: Alexa Earnest, Agent: Donovin Mundie, Agent: Darren Saylor."},
    "OperationAlpha": {"classification": "SCA", "content": "Attempt to 'Break Into' the school through a back door, durring lunch.\nThe Objective is to see if it is possile for anyone, an adult, to break in as well.\n \nAssigned Agents: Alexa Earnest \n \nDate: November 29th, 2023 | C Lunch\n \nResults: Successfully Broke Into the School \n \nDetails: Exited School at the Door at the end of D Hall Near the Activity Directors Office.\n I proceeded to Go to the door at the outside staircase near the C200s, a person came to the door and nodded no,\n they wouldnt let me in. I then walked the path to the YMCA and walked back, \n and headed to door C5 or D5 the one where the courtyard meets C100's and I was let in after I knocked on the door."},
    "OperationBravo": {"classification": "SCA", "content": ""},
}
def check_repository():
    status_output = subprocess.run(['git', 'status', '-uno'], capture_output=True, text=True)
    status = status_output.stdout.lower()

    if 'your branch is behind' in status:
        print("Warning: Repository is outdated. Please update before running the program.")
    else:
        print("Repository is up to date.")
# Function to authenticate users
def authenticate():
    #os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal screen
    custom_fig = pyfiglet.Figlet(font='slant')
    ascii_art = custom_fig.renderText('Agent Login')
    print(ascii_art)
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Simulating authorization check with a loading bar
    print("Checking authorization...") 
    progress_width = 20
    for i in range(progress_width + 1):
        time.sleep(0.1)  # Simulating authorization check delay
        progress = "=" * i + " " * (progress_width - i)
        print(f"\r[{progress}] {i * 100 // progress_width}% ", end="", flush=True)
    # Simulated authentication success
    if username in users and password == users[username]["password"]:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal screen
        print(f"\n{Fore.GREEN}Authentication successful!{Style.RESET_ALL}")
        return users[username]["clearance_level"]
    else:
        return None


# Function to display available files based on user's clearance level
def display_files(clearance_level):
    time.sleep(5)  # Simulating authorization check delay
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal screen
    custom_fig = pyfiglet.Figlet(font='slant')
    ascii_art = custom_fig.renderText('SSC Archives')
    print(ascii_art)
    print("-----------------------------------")
    print("| Available files:")
    print("-----------------------------------")
    for file_name, file_info in files.items():
        file_classification = file_info["classification"]
        if (clearance_level == "SSC" and file_classification in ["SSC", "SCA", "Student"]) or \
           (clearance_level == "SCA" and file_classification in ["SCA", "Student"]) or \
           (clearance_level == "Student" and file_classification == "Student"):
            print(f"| {Fore.GREEN}{file_name} - Classification: {file_classification}{Style.RESET_ALL}")  # Display in green color for better visibility
            print("-----------------------------------")


# Function to view file content based on user's choice
def view_file_content(choice):
    if choice in files:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal screen
        print(f"{Fore.YELLOW}File content:{Style.RESET_ALL}\n{Fore.RED}{files[choice]['content']}{Style.RESET_ALL}")
    else:
        print("Invalid File Choice.")
# Main function
def main():
    check_repository()  # Check repository status before proceeding
    clearance = authenticate()
    if clearance:
        print(f"Welcome! Your clearance level is {Fore.YELLOW + Style.BRIGHT}{clearance}{Style.RESET_ALL}.")
        display_files(clearance)
        file_choice = input("Enter the file you want to view: ")
        view_file_content(file_choice)
    else:
        print(f"\n{Fore.RED + Style.BRIGHT}Authentication failed.{Style.RESET_ALL}")  # Display in red color for failure
        time.sleep(2)  # Simulating authorization check delay
        authenticate()
# Run the program
if __name__ == "__main__":
    main()


