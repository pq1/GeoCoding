# Packages needed for running
1. Geocoder
2. GeoJSON

# Using the Geocode Script
`python geocode.py --input <input csv file here>`

There is an optional, but recommended command: `-g or --geocode <on|off>` The default is setting is off for testing/performance sake; it's slower when it needs to hit the Geocoder service.

For more information, use the help flag: `-h or --help`

# GeoCoding
Using the GeoCoder Plug-in for Python to add a latitude and longitude column a CSV file.
The original CSV does not have the column and the new CSV file is added to it.
Trying to simplify the code. Open to suggestions!
Need to look at which service is being used to Geocode. Currently uses the ArcGIS service. Google service tends to be more accruate.

Source:https://pypi.python.org/pypi/geocoder

# GeoJSON
The GeoJSON format is used to output addresses.
Here is a summary of the hierarchy of the data types: ![](https://github.com/pq1/GeoCoding/blob/master/geojson_summary.png)
