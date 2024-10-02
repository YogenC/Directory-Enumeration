'''''
Navigate to a website's /robots.txt file.
Select the entire contents of the page by pressing CTRL + A.
Copy the selected text and paste it into a text file.
Use the text file as input for the script below, which will filter the paths.
The filtered paths can then be used with main.py to check if the pages listed in robots.txt are accessible.
'''''


import os

def filter_disallowed_paths(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            input_data = file.read()

        disallowed_paths = [line.split(":")[1].strip() for line in input_data.splitlines() if line.startswith("Disallow:")]

        with open(output_file, 'w') as file:
            for path in disallowed_paths:
                file.write(f"{path}\n")

        print(f"Filtered paths saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))

    file = input("Enter file name (with extension, e.g., disallow_entries.txt): ")
    
    input_file = os.path.join(script_directory, file) 
    output_file = os.path.join(script_directory, "filtered_paths.txt")

    filter_disallowed_paths(input_file, output_file)
