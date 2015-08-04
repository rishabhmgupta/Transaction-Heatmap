import geocoder
import csv

rows = []
#fieldnames = ['location', 'extra', 'lat', 'lng', 'state', 'country']
fieldnames = ['Address', 'lat', 'lng']

with open('Addresses.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for line in reader:
        g = geocoder.tomtom(line['Address'])
        #print(line['Address'])
        # Add the CSV line data into the Geocoder JSON result

        #result = str(g.lat)+','+str(g.lng)
        result = g.json
        result.update(line)

        # Store Geocoder results in a list to save it later
        rows.append(result)

with open('geocoded.csv','w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)