# imports necessary packages
import csv
import os
import re


# opens csv file named 'metadata.csv' -- change if the name of the csv does not match
with open('metadata.csv', newline='') as md:

    # creates a new dialect s it does not read commas within double quotes as a delimiter
    csv.register_dialect('smart_csv', quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)

    # reads the csv as a dictionary object using the custom dialect
    reader = csv.DictReader(md, dialect="smart_csv")

    # gets column headers
    cols = reader.fieldnames

    # iterates through records in csv
    for record in reader:

        # Creates a file path based on the identifier using 'identifier'
        # This is following the template CSV provided by FromThePage
        # If the identifier column is named differently, change the code accordingly
        file_path = './files_to_sort/' + record['folder_id'] + '/' + 'metadata.yml'
        
        # checks if the record is in the folder to avoid a key error
        if record['folder_id'] in os.listdir("./files_to_sort/"):
            
            # creates the YAML file in each folder and writes metadata in the format: '<metadata attribute>: ”<sdf value>”'
            with open(file_path, 'w', encoding='utf-8') as f:
                for col in cols:
                    f.write(col+': "'+record[col]+'"\n')

# confirms that the script ran successfully
print('YAML files created.')
