# Read and Write Challenge: Modify file content

# Open the original file in read mode
with open("data.txt", "r") as input_file:
    # Read the file content
    content = input_file.read()

# Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Open a new file in write mode
with open("output.txt", "w") as output_file:
    # Write the modified content to the new file
    output_file.write(modified_content)

print("File has been read and modified content written to 'output.txt'!")

# Error Handling Lab: Safely handle file errors
try:
    # Ask the user for the filename
    filename = input("data.txt ")

    # Try to open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
