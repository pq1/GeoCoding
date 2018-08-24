
# Time to Process: 9 secs

# Next steps: Add in Geocoder into Long | Lat columns (would make the script run longer)

import csv
import os
import pandas as pd

data_space = r'C:\Users\pquach\PycharmProjects\geocode_google_app\data'

# function to read the files in the dir. It will convert the xls or xlsx files into csv files
def convert_csv(path_name):
    for file_name in os.listdir(path_name):                                                # for loop to read through the target dir
        if file_name.endswith('.xlsx') or file_name.endswith('xls'):                        # checks to see if file ends with xlsx or xls
            print(file_name)
            file_name_csv = os.path.splitext(file_name)                                     # gets the file name of xls or xlsx
            print(file_name_csv[0])
            data_xls = pd.read_excel(file_name, sheetname=0)                                # Pandas reads in the excel file and sheet1 and stores in variable name
            data_xls.to_csv(file_name_csv[0] + '.csv', encoding='utf-8', index=False)       # converts the excel file giving it the name of the original file

# Convert xls/xlsx to CSV files
def change_directory(dir_path):
    os.chdir(dir_path)
    convert_csv(dir_path)

change_directory(data_space)


with open('BLUE- RTP\'s.csv', 'rb') as input, open('output.csv', 'wb') as output:
    # Write the header
    fieldnames = 'DESCRIPTION, TYPE, ADDRESS, CITY, STATE, ZIP, FULL_ADDRESS, PHONE, LATITUDE, LONGITUDE, TYPE, SYMBOL'
    output.write(fieldnames + '\n')
    reader = csv.DictReader(input)
    for row in reader:
        # Combine Address into 1 column
        full_address = row['ADDRESS'] + ', ' + row['CITY'] + ' ,' + row['STATE'] + ', ' + row['ZIP']
        phone_number = '(' + row['PHONE'][0:3] + ')' + row['PHONE'][4:7] + '-' + row['PHONE'][8:]
        # Print out only desired columns
        # print(row['DESCRIPTION'], row['TYPE'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP'], full_address, phone_number)
        writer = csv.writer(output)
        writer.writerow([row['DESCRIPTION'], row['TYPE'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP'], full_address, phone_number, '', '', '2', 'measle_turquoise'])

with open('WHITE- ACE Cash.csv', 'rb') as input, open('output.csv', 'ab') as output:
    reader = csv.DictReader(input)
    for row in reader:
        # Combine Address into 1 column
        full_address = row['Address'] + ', ' + row['City'] + ' ,' + row['ST'] + ', ' + row['Zip']
        phone_number = '(' + row['Phone'][0:3] + ') ' + row['Phone'][3:6] + '-' + row['Phone'][6:]
        # print(row['Center Name'], '', row['Address'], row['City'], row['ST'], row['Zip'], full_address, phone_number)
        writer = csv.writer(output)
        writer.writerow([row['Center Name'], '', row['Address'], row['City'], row['ST'], row['Zip'], full_address, phone_number, '', '', '1', 'measle_white'])

# Need to check the phone number - sometimes there is a 1 in front
with open('WHITE- Fidelity Express.csv', 'rb') as input, open('output.csv', 'ab') as output:
    reader = csv.DictReader(input)
    for row in reader:
        full_address = row['Address'] + ', ' + row['City'] + ' ,' + row['St'] + ', ' + row['Zip'][0:5]
        if row['Loc Phone'][0] == '1':
            phone_number_1 = phone_number = '(' + row['Loc Phone'][1:4] + ') ' + row['Loc Phone'][4:7] + '-' + row['Loc Phone'][7:]
            writer = csv.writer(output)
            writer.writerow([row['Location Name'], '', row['Address'], row['City'], row['St'], row['Zip'][0:5], full_address, phone_number_1, '', '', '1', 'measle_white'])
        else:
            phone_number = phone_number = '(' + row['Loc Phone'][0:3] + ') ' + row['Loc Phone'][3:6] + '-' + row['Loc Phone'][6:]
            writer = csv.writer(output)
            writer.writerow([row['Location Name'], '', row['Address'], row['City'], row['St'], row['Zip'][0:5], full_address, phone_number, '', '', '1', 'measle_white'])

with open('WHITE- MoneyGram.csv', 'rb') as input, open('output.csv', 'ab') as output:
    reader = csv.DictReader(input)
    for row in reader:
        full_address = row['Physical Address Line1'] + ', ' + row['Physical Address City'] + ', ' + row['Physical Address State/Province Code'] + ', ' + row['Zip Code'][0:5]
        phone_number = '(' + row['Phone Number'][0:3] + ') ' + row['Phone Number'][3:6] + '-' + row['Phone Number'][6:]
        writer = csv.writer(output)
        writer.writerow([row['Display Name'], row['Industry Description'], row['Physical Address Line1'], row['Physical Address City'], row['Physical Address State/Province Code'], row['Zip Code'][0:5], full_address, phone_number, '', '', '1', 'measle_white'])