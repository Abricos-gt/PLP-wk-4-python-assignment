 # File Handling and Exception Handling Assignment
# Author: Your Name
# Date: YYYY-MM-DD

# ------------------------------
# Custom Exception
# ------------------------------

class EmptyFileError(Exception):
    """Raised when the file is empty."""
    def __init__(self, message="The file is empty."):
        self.message = message
        super().__init__(self.message)


# ------------------------------
# Part 1: File Read & Write Challenge
# ------------------------------

def file_read_write(input_file, output_file):
    """
    Reads content from input_file, allows user to add new lines,
    modifies content, and writes it into output_file.
    """
    try:
        # Read existing content
        try:
            with open(input_file, "r", encoding="utf-8") as infile:
                content = infile.readlines()
        except FileNotFoundError:
            print(f"Input file '{input_file}' not found. Creating a new one.")
            content = []

        # Let user add new lines
        print("Enter lines to add to the file (type 'DONE' to finish):")
        while True:
            line = input()
            if line.strip().upper() == "DONE":
                break
            content.append(line + "\n")

        if not content:
            raise EmptyFileError("Cannot write an empty file.")

        # Example modification: add line numbers and convert to uppercase
        modified_content = [f"{i+1}: {line.strip().upper()}\n" for i, line in enumerate(content)]

        # Write to output file
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.writelines(modified_content)

        print(f"Content successfully written to '{output_file}'.")

    except EmptyFileError as efe:
        print(f"Custom Error: {efe}")
    except PermissionError:
        print(f"Error: Permission denied for '{output_file}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("File Read & Write Challenge completed.")


# ------------------------------
# Part 2: Error Handling Lab
# ------------------------------

def error_handling_lab():
    """
    Asks the user for a filename and attempts to open it.
    Handles errors if the file doesn’t exist or can’t be read.
    """
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                raise EmptyFileError("The selected file is empty.")
            print("File content successfully read:\n")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
    except EmptyFileError as efe:
        print(f"Custom Error: {efe}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Error Handling Lab completed.")


# ------------------------------
# Main Program
# ------------------------------

if __name__ == "__main__":
    # Part 1 demo: allow user to write and modify content
    file_read_write("data.txt", "output.txt")

    # Part 2 demo: read a file with error handling
    error_handling_lab()
