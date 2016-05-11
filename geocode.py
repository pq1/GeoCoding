# Ver. 2.7.11
# Author: Philip Quach
# Description: Takes a CSV file that has addresses and writes a new CSV file that has Longitude and Latitude coordinates
# Read CSV file
# Read and skip over the header
# add lat and lon column to header
# write the new header to new file
# create a variable input for the geocoder because it only accepts 1 argument; we want the Address, City, St to be in 1 line
# the g.json is working with Dictionaries

#----- CSV pre-processing
# 1- Cut and Insert Cut cells of Address, City, Zip, St to the first 4 columns
# 2- In excel, select the Address column and replace all the commas(,) with a blank space
# 3- Select Facility Name and replace commas(,) with blank space

import geocoder, csv, time

with open('sample.csv', 'rb') as input, open('sampleGeo.csv', 'wb') as output: #, open('sampleGeo2', 'wb') as output2):
    reader = csv.reader(input, delimiter=',')
    row0 = reader.next() # Skips header Row
    print 'Current Header' + str(row0)
    Longitude = ['lon']
    Latitude = ['lat']
    geoMatch = ['match']
    new_line = row0 + Latitude + Longitude + geoMatch
    print 'New Header' + str(new_line)
    output.writelines([",".join(new_line)] + ['\n']) # write new header in new CSV
    count = 0

    for row in reader:
        address = ', '.join(row[:4]) # geocoder accepts only 1 arg, combines row[1] + row[2] + row[3]
        print 'Address: ' + address
        g = geocoder.arcgis(address)
        newLat = g.lat # Convert latitude
        newLon = g.lng # Convert longitude
        gDict = g.json # Convert JSON of results in a dictionary
        print gDict
        print 'confidence in : ', gDict.has_key('confidence') # Checks if there is a confidence key. The addresses that start with letters will not have confidence key
        if gDict.has_key('confidence') == False: # if the confidence is false (do not exist)
            continue
        else: # The confidence key does exist meaning that there was a score associated to it
            if gDict.get('score') >= 80:  # Checks if the score is greater than or equal to 80
                newMatch = gDict.get('score')
                row_line = row + [str(newLat)] + [str(newLon)] + [str(newMatch)]
                output.writelines(','.join(row_line) + '\n')
                count += 1
                print row_line
                print count
