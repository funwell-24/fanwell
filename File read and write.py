def process_file():
    """
    Reads a file, modifies its content, and writes to a new file with error handling.
    """
    while True:
        try:
            # Get input filename from user
            input_filename = input("Enter the name of the file to read: ")
            
            # Read the original file
            with open(input_filename, 'r') as file:
                content = file.read()
            
            # Process the content (example modification: convert to uppercase)
            modified_content = content.upper()
            
            # Get output filename from user
            output_filename = input("Enter the name of the file to write to: ")
            
            # Write the modified content
            with open(output_filename, 'w') as file:
                file.write(modified_content)
            
            print(f"Success! Modified content written to {output_filename}")
            break
            
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' was not found. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{input_filename}' or write to '{output_filename}'.")
        except IsADirectoryError:
            print(f"Error: '{input_filename}' is a directory, not a file.")
        except UnicodeDecodeError:
            print("Error: Could not decode the file content (might be a binary file).")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            break

# Run the program
if __name__ == "__main__":
    print("File Processing Program")
    print("-----------------------")
    process_file()