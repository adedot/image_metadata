
# Start postgres on the mac os:

    pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

    pg_ctl -D /usr/local/var/postgres stop -s -m fast

# create postgis exstension for database:

    CREATE EXTENSION postgis;

# Create virtual enviromnet

    python3 -m venv {environment_name}

# Install packages

    pip install -r requirements.txt

# Run the following to load geojson into a date range:

    python load_image_geojson.py -start {start} -end {end} -d {database} -u {user} -p {password}  -t {table}

    ## if you want to load files between 08-20-2018 and 08-21-2018
    python load_image_geojson.py -start  '20180820' -end '20180821' -d database -u user -p password  -t table

# To out geojson given a time range of '8-20-18 00:00:00 UTC' -end '8-21-18 00:00:00 UTC':

    python geohash.py -d your_database -u user -p password -host localhost -start '8-20-18 00:00:00 UTC' -end '8-21-18 00:00:00 UTC' > results.geojson

# To run tests:

    (note: you will have to add your database credentials in test_geohash.py)
    pytest test_geohash.py

# To run tests with output
    (note: you will have to add your database credentials in test_geohash.py)
    pytest test_geohash.py -ra -s





