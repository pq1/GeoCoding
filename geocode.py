# Ver. 2.7.11
# Mod. Geocoder, CSV
# Author: pq1
# Description: Takes a CSV file that has addresses and writes a new CSV file that has Longitude and Latitude coordinates
# Note: Uses ArcGIS as Geocoder
# ArcGIS seems to have no rate limit for Geocoding

#----------- Steps
# Read CSV file
# Read and skip over the header
# add lat and lon column to header
# write the new header to new file
# create a variable input for the geocoder because it only accepts 1 argument; we want the Address, City, St to be in 1 line


#----- CSV pre-processing
# 1- Cut and Insert Cut cells of Address, City, Zip, St to the first 4 columns
# 2- In excel, select the Address column and replace all the commas(,) with a blank space
# 3- Select Facility Name and replace commas(,) with blank space# Read CSV file
# Read and skip over the header
# add lat and lon column to header
# write the new header to new file
# create a variable input for the geocoder because it only accepts 1 argument; we want the Address, City, St to be in 1 line

import geocoder, csv

with open('sample.csv', 'rb') as input, open('sampleLatLon.csv', 'wb') as output:
    reader = csv.reader(input, delimiter=',')
    row0 = reader.next()
    print row0
    Longitude = ['lon']
    Latitude = ['lat']
    new_line = row0 + Longitude + Latitude
    print new_line
    output.writelines([",".join(new_line)] + ['\n'])


    for row in reader:
        print row
        address = ', '.join(row[1:4]) # geocoder accepts only 1 arg, combines row[1] + row[2] + row[3]
        print address
        g = geocoder.arcgis(address)
        newLat = g.lat
        newLon = g.lng
        print newLat + newLon
        row_line = row + [str(newLon)] + [str(newLat)]
        print row_line
        output.writelines(','.join(row_line) + '\n')
        #time.sleep(2) #Time delay in sec

