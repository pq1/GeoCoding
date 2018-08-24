# navigate to data folder
# convert xlsx to csv
# Dependencies: geocoder; pandas; csv; os
# function 1: convert the xls|xlsx to csv
# function 2: process csv to new csv with correct columns and add in symbology column
# function 3: append all csv records into 1 csv file

import os
import pandas as pd
import csv

# Can we do CLI?
data_space = r'C:\Users\pquach\PycharmProjects\geocode_google_app\data'

# Global Variables


# function to read the files in the dir. It will convert the xls or xlsx files into csv files
def convert_csv(path_name):
    for file_name in os.listdir(path_name):                                                # for loop to read through the target dir
        if file_name.endswith('.xlsx') or file_name.endswith('xls'):                        # checks to see if file ends with xlsx or xls
            print(file_name)
            file_name_csv = os.path.splitext(file_name)                                     # gets the file name of xls or xlsx
            print(file_name_csv[0])
            data_xls = pd.read_excel(file_name, sheetname=0)                                # Pandas reads in the excel file and sheet1 and stores in variable name
            data_xls.to_csv(file_name_csv[0] + '.csv', encoding='utf-8', index=False)       # converts the excel file giving it the name of the original file


def arrange_csv(file_csv):
    for csv_file in os.listdir(file_csv):
        #Open main csv file to append records to
        if csv_file.endswith('.csv'):
            with open('data\\' + csv_file, 'r') as input, open('output.csv', 'w') as output:
                # Write the header https://stackoverflow.com/questions/2982023/how-to-write-header-row-with-csv-dictwriter
                fieldnames = 'DESCRIPTION, TYPE, ADDRESS, CITY, STATE, ZIP, FULL_ADDRESS, PHONE, LATITUDE, LONGITUDE, TYPE, SYMBOL'
                output.write(fieldnames + '\n')
                reader = csv.DictReader(input)

                # Check the file name to input proper type and symbol
                #print(csv_file)
                if csv_file == 'BLUE- RTP\'s.csv':
                    print(csv_file)
                    writer = csv.writer(output)
                    for row in reader:
                        # DESCRIPTION,TYPE,ADDRESS,CITY,STATE,ZIP
                        # Combine Address into 1 column
                        full_address = row['ADDRESS'] + ', ' + row['CITY'] + ' ,' + row['STATE'] + ', ' + row['ZIP']

                        # Print out only desired columns
                        print(row['DESCRIPTION'], row['TYPE'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP'],
                              full_address, row['PHONE'])
                        writer = csv.writer(output)
                        # output.writelines(combo + '\n')
                        writer.writerow(
                            [row['DESCRIPTION'], row['TYPE'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP'],
                             full_address, row['PHONE'], '', '', '2', 'measle_turquoise'])

                # for row in reader:
                #     # DESCRIPTION,TYPE,ADDRESS,CITY,STATE,ZIP
                #     # Combine Address into 1 column
                #     writer = csv.writer(output)
                #     #print(type(row))
                #     if 'ADDRESS' in row:  # Check if key in dict
                #         full_address = row['ADDRESS'] + ' ' + row['CITY'] + ' ,' + row['STATE'] + ', ' + row['ZIP']
                #         print(row['ADDRESS'])
                #         writer.writerow(['test', 'test2'])



                    # Print out only desired columns
                    #print(row['DESCRIPTION'], row['TYPE'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP'],
                    #      full_address,
                    #      row['PHONE'])


                    #writer.writerow(
                    #    [row['DESCRIPTION'], row['TYPE'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP'],
                    #     full_address,
                    #     row['PHONE'], '', '', '2', 'measle_turquoise'])
                # with open('data\\' + csv_file, 'rb') as input:
                #     reader = csv.DictReader(input).next()
                #     #row0 = reader.next()
                #     print 'Current Header: {}'.format(reader)





    # grab only necessary headers
    # combine the addresses
    # create new columns - lonitude, latitude, symbol, font
    # If the csv file has blue- go to this function that inputs the blue symbol
        # if the csv file has white- go to this function that inputs the white symbol
    # geocode

    # Notes - white or blue point
    # add in Red point

def process_blue(rtp_file):

    reader = csv.DictReader(input)
    for row in reader:
        # DESCRIPTION,TYPE,ADDRESS,CITY,STATE,ZIP
        # Combine Address into 1 column
        full_address = row['ADDRESS'] + ', ' + row['CITY'] + ' ,' + row['STATE'] + ', ' + row['ZIP']

        # Print out only desired columns
        print(row['DESCRIPTION'], row['TYPE'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP'], full_address,
              row['PHONE'])
        writer = csv.writer(output)
        # output.writelines(combo + '\n')
        writer.writerow(
            [row['DESCRIPTION'], row['TYPE'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP'], full_address,
             row['PHONE'], '', '', '2', 'measle_turquoise'])

# function that changes the directory to target space and
def change_directory(dir_path):
    os.chdir(dir_path)
    convert_csv(dir_path)

# with open('data\\BLUE- RTP's.csv', 'rb') as input: #, open(csv_file_update + '_update.csv','wb') as output:
#     reader = csv.reader(input)
#     row0 = reader.next()  # Skips header Row
#     print 'Current Header' + str(row0)
#     print(reader)
#change_directory(data_space)
arrange_csv(data_space)



