# Read CSV file
# Use a GeoCoder to get lat and lon
# Write data into GeoJSON format

import geocoder, csv
import argparse
import json, geojson
import copy

parser = argparse.ArgumentParser(description='-----------Geocoding Help-----------')
parser.add_argument("-i", "--input", help='Required input CSV file name. There is a sample.csv in the current directory.', required=True)
parser.add_argument("-g", "--geocode", help='\'on\' or \'off\' to get geocodes from ArcGIS. Default is \'off\' since it\'s faster.')
args = parser.parse_args()

address_file = args.input
output_file = 'addresses_out.geojson'

DEFAULT_STATE = 'TX'

with open(address_file, 'rb') as input, open(output_file, 'wb') as output:
    reader = csv.DictReader(input)

    # Define new GeoJSON Feature Collection that holds everything together
    # We're using GeoJSON Features because they can hold a list of properties, which is where
    # we store all of the other data

    feature_collection = geojson.FeatureCollection([])
    address_dict = {}
    
    for row in reader:
        point = None
        if args.geocode == 'on':
            # Create a variable input for the geocoder because it only accepts 1 argument; we want the Address, City, St to be in 1 line
            address = row['Address'] + ', ' + row['City'] + ', ' + DEFAULT_STATE
            address_lat =  geocoder.arcgis(address).lat
            address_lng = geocoder.arcgis(address).lng
            point = geojson.Point([address_lng, address_lat])
            score = geocoder.arcgis(address).score
            address_dict['Score'] = score

        # Only get the fields we want from MLS
        address_dict['Address'] = row['Address']
        address_dict['City'] = row['City']
        address_dict['State'] = DEFAULT_STATE
        address_dict['SqFt Total'] = row['SqFt Total']
        address_dict['Lot Size Area'] = row['Lot Size Area']
        address_dict['Beds Total'] = row['Beds Total']
        address_dict['Baths Total'] = row['Baths Total']
        address_dict['GAR/CP/TCP'] = row['GAR/CP/TCP']
        address_dict['Current Price'] = row['Current Price'].strip()
        address_dict['Change Type'] = row['Change Type']

        feature = geojson.Feature(geometry=point, properties=address_dict)

        # Need to do a deep copy of the object in order to get unique objects into the feature_list
        # Referece: http://forums.devshed.com/python-programming-11/appending-object-list-overwrites-previous-842713.html
        feature_collection.features.append(copy.deepcopy(feature))

    json.dump(feature_collection, output, indent=4, sort_keys=False)
    output.write('\n')
