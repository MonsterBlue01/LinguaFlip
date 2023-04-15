import csv

def remove_columns(input_file, output_file, columns_to_remove):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        # Read the input CSV file
        reader = csv.reader(infile)
        # Write to the output CSV file with csv.QUOTE_NONNUMERIC option
        writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
        
        # Process the header row
        header = next(reader)
        new_header = [header[i] for i in range(len(header)) if i not in columns_to_remove]
        writer.writerow(new_header)

        # Process the remaining rows
        for row in reader:
            new_row = [row[i] for i in range(len(row)) if i not in columns_to_remove]
            writer.writerow(new_row)

# Example usage:
input_file = 'small_example.csv'
output_file = 'sample1.csv'
columns_to_remove = [1, 3]  # Column indices to remove (0-indexed)

remove_columns(input_file, output_file, columns_to_remove)