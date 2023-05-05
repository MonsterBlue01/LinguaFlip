import csv

# A function that returns True if all elements of the first row of the CSV file
# are included in the given list of elements, and False otherwise.
def check_first_line_elements(filename, elements):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        first_line = next(reader)
        # ------test------
        invalid_elements = [elem for elem in first_line if elem not in valid_elements]
        print(invalid_elements)
        # ----------------
        return all(elem in elements for elem in first_line)

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
    'company Fax',
    'companyStreet',
    'companyCity',
    'companyState',
    'companyZipCode',
    'companyCountry',
    'company Continent',
    'companyLogo',
    'company Division',
    'companySicCodes',
    'companyNaicsCodes',
    'companyWebsite',
    'company Revenue',
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
    filename = 'small_example.csv'
    if check_first_line_elements(filename, valid_elements):
        print("All elements are valid.")
    else:
        print("Some elements are not valid.")
