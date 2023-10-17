import os

# Function to create a new script file for a custom command
def create_custom_command(command_name, command_code):
    # Define the directory where custom command scripts will be stored
    custom_commands_directory = "custom_commands"

    # Ensure the custom commands directory exists, or create it if it doesn't
    if not os.path.exists(custom_commands_directory):
        os.makedirs(custom_commands_directory)

    # Define the file path for the custom command script
    script_file_path = os.path.join(custom_commands_directory, command_name + ".py")

    # Check if a script with the same name already exists
    if os.path.exists(script_file_path):
        print(f"Error: The command '{command_name}' already exists.")
        return

    # Create the script file and write the provided code to it
    with open(script_file_path, "w") as script_file:
        script_file.write(command_code)

    print(f"Custom command '{command_name}' created successfully!")


# Main program
if __name__ == "__main__":
    # Get user input for the new command name
    command_name = input("Enter the name for the new custom command: ")

    print("Enter the code for the new custom command (Python code):")

    # Read multiple lines of input until the end of file (EOF) is reached
    command_code = ""
    while True:
        try:
            line = input()
            command_code += line + "\n"
        except EOFError:
            break

    # Create the custom command script
    create_custom_command(command_name, command_code)
