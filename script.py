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
    new_list = [x for x in csv_list if x not in txt_list]
    return new_list

# Delete corresponding columns
def delete_columns(column_names, input_file):
    with open(input_file, 'r+', newline='') as csv_file:
        reader = csv.reader(csv_file)
        writer = csv.writer(csv_file)

        # Modify the header row to remove the specified columns
        header = next(reader)
        columns_to_delete = [header.index(col_name) for col_name in column_names]
        filtered_header = [header[i] for i in range(len(header)) if i not in columns_to_delete]
        csv_file.seek(0)
        writer.writerow(filtered_header)

        # Modify the remaining rows to remove the specified columns
        for row in reader:
            filtered_row = [row[i] for i in range(len(row)) if i not in columns_to_delete]
            csv_file.write(','.join(filtered_row) + '\n')

if __name__ == '__main__':
    txt_line = read_txt_file('small_example_fields.txt')
    # print(lines)

    csv_line = read_csv_file('small_example.csv')
    # print(column_name)

    new_line = compare_lists(csv_line, txt_line)
    delete_columns(new_line, 'small_example.csv')