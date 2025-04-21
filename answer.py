def read_and_modify_file():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (example: make it uppercase)
        modified_content = content.upper()

        # Create a new filename
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
