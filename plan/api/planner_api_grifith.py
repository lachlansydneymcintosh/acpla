# Import warranted packages
import requests
import json

course_code = '2043LHS'
degree_code = '1601'

url_program_base = 'https://degrees.griffith.edu.au/rest-api/v3/'

url = 'https://degrees.griffith.edu.au/rest-api/v3/course/2043LHS'

# API Request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f'Succesful API call')
else:
    print('Failed request')

print('\n')

# Extract details

# 
request_type = 'c'

# COURSEs
if request_type == 'c':
    course_name = data['name']
    course_code = data['code']
    course_student_contribution_band = data['studentContributionBand']
    course_description = data['description']
    course_credit_points = data['creditPoints']
    course_awarded_credit_points = data['awardedCreditPoints']
    course_is_restricted = data['isRestricted']

    # Offerings
    if 'offerings' in data:  # Ensure the 'offerings' key exists
        for i, offering in enumerate(data['offerings']):  # Loop through the offerings
            print(f'Offering {i + 1}:')
            course_year = offering['offeringTerm']['year']
            course_trimester = offering['offeringTerm']['category']

            if 'timeTables' in offering:
                for j, timetables in enumerate(offering['timeTables']):
                    if 'classes' in timetables:
                        for k, class_item in enumerate(timetables['classes']):
                            course_class_code = class_item['code']
                            course_class_type_full = class_item['componentType']
                            #``course_class_type_short = class_item['cl']

                            print(course_class_code)
                            print('\n')

                    else:
                        print('No classes found.')
            else:
                print('No timetables found.')
    else:
        print('No offerings found.')
