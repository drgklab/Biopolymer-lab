import os
import glob
import matplotlib.pyplot as plt

# Define the root directory
root_directory = "/Users/vivetha/Downloads/q776a"

# Initialize variables to track the presence of keywords
desired_keyword = "/B0983-LIG"
keywords = ["770-ASN", "776-GLN", "817-ARG", "807-MET", "829-PHE", "845-MET", "849-CYS", "852-MET", "941-PHE", "942-CYS"]
keyword_flags = {keyword: 0 for keyword in keywords}

# Lists to store file numbers and keyword presence data
file_numbers = []
keyword_presence_data = {keyword: [] for keyword in keywords}

# Traverse directories and subdirectories
for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in glob.glob(os.path.join(dirpath, '*.nnb')):
        directory_parts = filename.split('/')
        num = directory_parts[-1].split('.')[0]

        try:
            # Open the file in read mode ('r')
            with open(filename, 'r') as file:
                # Read and process each line in the file
                for line in file:
                    if desired_keyword in line:
                        for keyword in keywords:
                            if keyword in line:
                                keyword_flags[keyword] = 1

            # Store the results for this file
            file_numbers.append(num)
            for keyword in keywords:
                keyword_presence_data[keyword].append(keyword_flags[keyword])

            # Reset the keyword flags for the next file
            keyword_flags = {keyword: 0 for keyword in keywords}

        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(file_numbers, keyword_presence_data[keywords[0]], label=keywords[0])

# Add bars for other keywords
for keyword in keywords[1:]:
    plt.bar(file_numbers, keyword_presence_data[keyword], label=keyword, bottom=keyword_presence_data[keywords[0]])

# Customize the plot
plt.xlabel("File Numbers")
plt.ylabel("Keyword Presence")
plt.title("Keyword Presence in Files")
plt.legend()

# Show the plot
plt.show()