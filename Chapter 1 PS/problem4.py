import os

# Specify the directory path
directory_path = '/Affan Documents'

# Print the contents of the directory
try:
    # List the contents of the directory
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied for accessing the directory '{directory_path}'.")