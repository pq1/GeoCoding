# Read CSV file
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

