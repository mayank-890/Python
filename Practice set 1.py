import os

# Specify the path to the directory
directory_path = '/'

# List the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)