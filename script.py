import csv
from tkinter.filedialog import asksaveasfilename

# A function that returns True if all elements of the first row of the CSV file
# are included in the given list of elements, and False otherwise.
def check_first_line_elements(filename, elements):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        first_line = next(reader)
        invalid_elements = [elem for elem in first_line if elem not in valid_elements]
        return all(elem in elements for elem in first_line), invalid_elements

# Remove the columns that ZoomInfo API doesn't support
def remove_invalid_columns(input_filename, valid_elements):
    _, invalid_elements = check_first_line_elements(input_filename, valid_elements)
    cleaned_data = []
    
    with open(input_filename, 'r') as input_file:
        reader = csv.reader(input_file)
        header = next(reader)
        invalid_indices = [header.index(elem) for elem in invalid_elements]

        valid_header = [elem for elem in header if elem not in invalid_elements]
        cleaned_data.append(valid_header)
        
        for row in reader:
            valid_row = [row[i] for i in range(len(row)) if i not in invalid_indices]
            cleaned_data.append(valid_row)
            
    return cleaned_data

# Try to convert the value before replace it with
def convert_value(value, data_type):
    try:
        if data_type == bool:
            return value.lower() in ['true', '1']
        return data_type(value)
    except (ValueError, TypeError):
        return None

# Check the datatype
def clean_csv_data(cleaned_data, output_filename, field_data_types):
    with open(output_filename, 'w') as output_file:
        fieldnames = cleaned_data[0]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in cleaned_data[1:]:
            row_dict = dict(zip(fieldnames, row))
            cleaned_row = {}
            
            for field, value in row_dict.items():
                data_type = field_data_types.get(field)
                if data_type:
                    cleaned_value = convert_value(value, data_type)
                    cleaned_row[field] = cleaned_value
                else:
                    cleaned_row[field] = value
            
            writer.writerow(cleaned_row)

# The list of elements that the first row of the CSV file should contain.
valid_elements = [
    'personId',
    'firstName',
    'lastName',
    'middleName',
    'companyId',
    'companyName',
    'jobTitle',
    'contactAccuracyScore',
    'validDate',
    'lastUpdatedDate',
    'hasEmail',
    'hasSupplementalEmail',
    'hasDirectPhone',
    'hasMobilePhone',
    'hasCompanyIndustry',
    'hasCompanyPhone',
    'hasCompanyStreet',
    'hasCompanyState',
    'hasCompanyZipCode',
    'hasCompanyCountry',
    'hasCompanyRevenue',
    'hasCompanyEmployeeCount',
    'companyId',
    'companyName',
    'id',
    'email',
    'hasCanadianEmail',
    'phone',
    'directPhoneDoNotCall',
    'street',
    'city',
    'region',
    'metroArea',
    'zipCode',
    'state',
    'country',
    'continental',
    'personHasMoved',
    'withinEu',
    'withinCalifornia',
    'withinCanada',
    'validDate',
    'lastUpdatedDate',
    'noticeProvidedDate',
    'salutation',
    'suffix',
    'jobTitle',
    'jobFunction',
    'education',
    'hashedEmails',
    'picture',
    'mobilePhoneDoNotCall',
    'externalUrls',
    'employmentHistory',
    'managementLevel',
    'contactAccuracyScore',
    'companyDescriptionList',
    'companyPhone',
    'companyFax',
    'companyStreet',
    'companyCity',
    'companyState',
    'companyZipCode',
    'companyCountry',
    'companyContinent',
    'companyLogo',
    'companyDivision',
    'companySicCodes',
    'companyNaicsCodes',
    'companyWebsite',
    'companyRevenue',
    'companyRevenueNumeric',
    'companyEmployeeCount',
    'companyType',
    'companyTicker',
    'company ranking',
    'isDefunct',
    'companySocialMediaUrls',
    'isCalifornia',
    'isCanada',
    'companyPrimaryIndustry',
    'companyIndustries',
    'companyRevenueRange',
    'companyEmployeeRange',
    'locationCompanyId',
    'positionStartDate',
    'yearsOfExperience',
    'techSkills'
]

if __name__ == '__main__':
    input_filename = 'C:\Personal Projects\Flow\FlowAI\FlowApp\csvprocessing\csvprocessing\small_example.csv'
    output_filename = r'{}'.format(asksaveasfilename(title="Input CSV File Name",defaultextension='.csv',filetypes=[("CSV file",".csv")])) 
    
    if check_first_line_elements(input_filename, valid_elements)[0]:
        print("All elements are valid.")
    else:
        print("Some elements are not valid. Removing invalid columns...")
        cleaned_data = remove_invalid_columns(input_filename, valid_elements)
        print("Invalid columns removed.")
    
    # Define the field_data_types dictionary here.
    field_data_types = {
        'personId': int,
        'firstName': str,
        'lastName': str,
        'middleName': str,
        'companyId': int,
        'companyName': str,
        'jobTitle': str,
        'contactAccuracyScore': float,
        'validDate': str,               # can't find example in small_example.csv and large_example.csv
        'lastUpdatedDate': str,         # can't find example in small_example.csv and large_example.csv
        'hasEmail': bool,               # can't find example in small_example.csv and large_example.csv
        'hasSupplementalEmail': bool,   # can't find example in small_example.csv and large_example.csv
        'hasDirectPhone': bool,         # can't find example in small_example.csv and large_example.csv
        'hasMobilePhone': bool,         # can't find example in small_example.csv and large_example.csv
        'hasCompanyIndustry': bool,     # can't find example in small_example.csv and large_example.csv
        'hasCompanyPhone': bool,        # can't find example in small_example.csv and large_example.csv
        'hasCompanyStreet': bool,       # can't find example in small_example.csv and large_example.csv
        'hasCompanyState': bool,        # can't find example in small_example.csv and large_example.csv
        'hasCompanyZipCode': bool,      # can't find example in small_example.csv and large_example.csv
        'hasCompanyCountry': bool,      # can't find example in small_example.csv and large_example.csv
        'hasCompanyRevenue': bool,      # can't find example in small_example.csv and large_example.csv
        'hasCompanyEmployeeCount': bool,# can't find example in small_example.csv and large_example.csv
        'companyId': int,
        'companyName': str,
        'id': int,                      # can't find example in small_example.csv and large_example.csv
        'email': str,
        'hasCanadianEmail': bool,       # can't find example in small_example.csv and large_example.csv
        'phone': str,
        'directPhoneDoNotCall': str,    # can't find example in small_example.csv and large_example.csv
        'street': str,
        'city': str,
        'region': str,                  # can't find example in small_example.csv and large_example.csv
        'metroArea': str,               # can't find example in small_example.csv and large_example.csv
        'zipCode': int, 
        'state': str,
        'country': str,
        'continental': str,             # can't find example in small_example.csv and large_example.csv
        'personHasMoved': str,          # can't find example in small_example.csv and large_example.csv (not so sure what it is)
        'withinEu': bool,
        'withinCalifornia': bool,
        'withinCanada': bool,
        'validDate': bool,
        'lastUpdatedDate': str,
        'noticeProvidedDate': str,
        'salutation': str,
        'suffix': str,
        'jobTitle': str,
        'jobFunction': str,
        'education': str,               # can't find example in small_example.csv and large_example.csv
        'hashedEmails': bool,           # can't find example in small_example.csv and large_example.csv
        'picture': str,                 # can't find example in small_example.csv and large_example.csv (Maybe it should be binary but there is no such type in CSV or Python)
        'mobilePhoneDoNotCall': str,
        'externalUrls': str,
        'employmentHistory': str,       # can't find example in small_example.csv and large_example.csv (not so sure if this datatype is proper)
        'companyDescriptionList': str,  # can't find example in small_example.csv and large_example.csv (not so sure if this datatype is proper)
        'companyPhone': str,
        'companyFax': str,
        'companyStreet': str,
        'companyCity': str,
        'companyState': str,
        'companyZipCode': int,
        'companyCountry': str,
        'companyContinent': str,
        'companyLogo': str,
        'companyDivision': str,
        'companySicCodes': int,
        'companyNaicsCodes': int,       # Change it back if it is str but not int
        'companyWebsite': str,
        'companyRevenue': int,
        'companyRevenueNumeric': int,
        'companyEmployeeCount': int,
        'companyType': str,
        'companyTicker': int,
        'company ranking': int,         # can't find example in small_example.csv and large_example.csv
        'isDefunct': bool,              # can't find example in small_example.csv and large_example.csv
        'companySocialMediaUrls': str,  # can't find example in small_example.csv and large_example.csv
        'isCalifornia': bool,           # can't find example in small_example.csv and large_example.csv
        'isCanada': bool,               # can't find example in small_example.csv and large_example.csv
        'companyPrimaryIndustry': str,
        'companyIndustries': str,
        'companyRevenueRange': str,
        'companyEmployeeRange': int,
        'locationCompanyId': int,       # can't find example in small_example.csv and large_example.csv
        'positionStartDate': str,
        'yearsOfExperience': int,       # can't find example in small_example.csv and large_example.csv
        'techSkills': str,              # can't find example in small_example.csv and large_example.csv
    }
    
    print("Checking and replacing entries with invalid data types...")
    clean_csv_data(cleaned_data, output_filename, field_data_types)
    print(f"Data types checked and cleaned. Final cleaned data saved to {output_filename}.")