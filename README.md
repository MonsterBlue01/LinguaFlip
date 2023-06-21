# CSV Data Cleaning Tool
This tool is designed to clean CSV data, especially tailored for ZoomInfo API's CSV data. It filters out unsupported columns and cleans the data based on predefined data types.

## Features
1. Checks if all elements in the first row (header) are valid and removes any invalid columns.
2. Validates each data entry against the specified data type and replaces the invalid entries with a None value.

## Code Explanation
The code starts by importing the necessary libraries: csv for `CSV` file handling, and `tkinter.filedialog` to prompt the user to choose a save location for the cleaned CSV file.

The main functionality of the code is encapsulated within the following functions:

1. `check_first_line_elements(filename, elements)`: Checks if all elements of the first row in the CSV file are included in the valid_elements list. It returns a boolean indicating this, along with any invalid elements.

2. `remove_invalid_columns(input_filename, valid_elements)`: If invalid columns are present, this function reads the CSV file, removing columns that are not present in the valid_elements list.

3. `convert_value(value, data_type)`: Converts a given value to the desired data type, if possible. If conversion fails, it returns None.

4. `clean_csv_data(cleaned_data, output_filename, field_data_types)`: This function writes the cleaned data to the output CSV file. It also converts the data entries in each row to the predefined data type using convert_value(). If the data type conversion fails, it replaces the value with None.

5. The `if __name__ == '__main__'`: block defines the flow of the program. It calls the above functions to process the input file and save the cleaned data to the output file.

## Usage
1. Specify your input CSV file in the `input_filename` variable.
2. Run the script. It will prompt you to choose a location and name for the output CSV file.
3. The script will check if all columns from the input file are supported. If not, it removes the unsupported columns.
4. The script then cleans the data according to the data type defined in `field_data_types`. Invalid entries will be replaced by `None`.
5. The cleaned data is saved to the output CSV file.

## Note
The `field_data_types` dictionary needs to be manually adjusted according to the actual data types of your columns.

## Requirements
- Python 3.x
- tkinter library for Python
- A CSV file to clean

## Contact
If you have any questions or feedback, please feel free to reach out. Enjoy using the CSV Data Cleaning Tool!

## Future Enhancements
Dynamically infer data types instead of manually defining them.
Use command line arguments for input and output file paths for more flexible usage.
Add support for more data types or formats.