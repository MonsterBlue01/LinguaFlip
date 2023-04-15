import csv

# A function that read from txt and return a list
def read_txt_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

# A function that read from csv and return a list
def read_csv_file(filename):
    with open(filename, 'r', encoding='iso-8859-1') as csv_file:    # NOTE: I met a bug and I add "encoding='iso-8859-1'" to solve it. If you met a bug relate to Unicode, please think about if we should add this to the "read_txt_file" (Although I didn't meet the error for "read_txt_file")
        reader = csv.reader(csv_file)
        column_names = next(reader)

    return column_names

# A function that takes csv list and txt list. And do the most important task
def compare_lists(csv_list, txt_list):
    # Compare the lists and create a new list with indices of elements not in the txt_list
    result_list = [i for i, element in enumerate(csv_list) if element not in txt_list]

    return result_list

# Delete corresponding columns
def remove_columns(input_file, output_file, columns_to_remove):
    with open(input_file, 'r', newline='', encoding='iso-8859-1') as infile, open(output_file, 'w', newline='') as outfile:
        # Read the input file as plain text
        lines = infile.readlines()

        # Process the header row
        header = lines[0].strip().split(',')
        new_header = [header[i] for i in range(len(header)) if i not in columns_to_remove]
        outfile.write(','.join(new_header) + '\n')

        # Process the remaining rows
        for line in lines[1:]:
            row = line.strip().split(',')
            new_row = [row[i] for i in range(len(row)) if i not in columns_to_remove]
            outfile.write(','.join(new_row) + '\n')

# General function that take care about almost everything 
def delete_column_func(txt_file, input_csv, output_csv):
    txt_line = read_txt_file(txt_file)
    csv_line = read_csv_file(input_csv)

    new_line = compare_lists(csv_line, txt_line)
    remove_columns(input_csv, output_csv, new_line)

# Test case
if __name__ == '__main__':
    txt_file = 'large_example_fields.txt'
    input_csv = 'large_example.csv'
    output_csv = 'sample1.csv'
    delete_column_func(txt_file, input_csv, output_csv)