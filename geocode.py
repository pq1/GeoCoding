# Read CSV file
# Read and skip over the header
# add lat and lon column to header
# write the new header to new file
# create a variable input for the geocoder because it only accepts 1 argument; we want the Address, City, St to be in 1 line

import geocoder, csv
import argparse
import datetime
import json

parser = argparse.ArgumentParser(description='-----------Geocoding Help-----------')
parser.add_argument("-i", "--input", help='Required input CSV file name', required=True)
parser.add_argument("-g", "--geocode", help='\'on\' or \'off\' to get geocodes from ArcGIS. Default is \'off\' since it\'s faster.')
args = parser.parse_args()

address_file = args.input
output_file = 'addresses_out.json'

with open(address_file, 'rb') as input, open(output_file, 'wb') as output:
    reader = csv.DictReader(input)
    for row in reader:
        if args.geocode == 'on':
            address = row['Address'] + ', ' + row['City'] + ', TX'
            row['Latitude'] =  geocoder.arcgis(address).lat
            row['Longitude'] = geocoder.arcgis(address).lng

        json.dump(row, output, indent=4, sort_keys=True)
        output.write('\n')
