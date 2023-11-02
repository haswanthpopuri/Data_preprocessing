import os
import csv

# Specify the folder where your files are located
folder_path = 'PPDbench/reconstructed_peptides'

# Get the names of all files in the folder
file_names = os.listdir(folder_path)

# Extract the first 4 characters from each file name
first_4_characters = [file[:4] for file in file_names]

# Read the CSV file and create a list of rows to filter
filtered_rows = []

# Replace 'your_csv_file.csv' with the actual CSV file name
with open('crawl_results.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Read and save the header
    for row in csv_reader:
        if row[0][:4] in first_4_characters:  # Replace 0 with the appropriate column index
            filtered_rows.append(row)

# Write the filtered rows to a new CSV file
with open('filtered_data.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(header)  # Write the header
    csv_writer.writerows(filtered_rows)
