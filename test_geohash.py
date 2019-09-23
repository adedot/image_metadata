# tests.py
import geohash
import pdb
import psycopg2
import load_image_geojson

# Add your database connection information
dbname = "your database"
user = "your username"
password = "your password"
host = "your localhost or ip address"
table = "image_metadata"
start = '20180820'
end = '20180821'


load_image_geojson.load_geojson_into_postgres(dbname,user, password, table, start, end)

def test_some_results():
    start_datetime = '8-20-18 19:48:00 UTC'
    end_datetime = '8-21-18 00:00:00 UTC'
    start_timestamp = geohash.create_timestamp(start_datetime)
    end_timestamp = geohash.create_timestamp(end_datetime)

    query = geohash.create_geohash_range_query(start_timestamp, end_timestamp)
    result_json = {"type": "FeatureCollection","crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },"features":[[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016782,37.7956815]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016804,37.7956823]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016746,37.7956978]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016006,37.7956017]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016741,37.7956861]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4015177,37.7950703]},"properties":{"count":29,"geohash":"9q8zn8mu","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4014953,37.7946665]},"properties":{"count":29,"geohash":"9q8zn8mc","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4014704,37.7948539]},"properties":{"count":29,"geohash":"9q8zn8mf","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016279,37.7954781]},"properties":{"count":29,"geohash":"9q8zn8my","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4015861,37.7952943]},"properties":{"count":29,"geohash":"9q8zn8mv","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016698,37.7956792]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016762,37.7956779]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016772,37.7956761]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016739,37.795679]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016799,37.7956824]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016535,37.7956845]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}],[{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4016853,37.795687]},"properties":{"count":29,"geohash":"9q8zn8mz","color":"#00ff00"}}]]}

    try:
        connect_str = "dbname='{}' user='{}' password='{}' host='{}'".format(dbname,user,password,host)
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        geo_json = geohash.to_geojson(rows)
        assert geo_json == result_json
        cursor.close()
        conn.close()
    except Exception as e:
        # pass
        print("\nUh oh, can't connect. Invalid dbname, user or password? \n")
        print(e)

def test_no_results():
    start_datetime = '8-20-18 19:50:00 UTC'
    end_datetime = '8-21-18 00:00:00 UTC'
    start_timestamp = geohash.create_timestamp(start_datetime)
    end_timestamp = geohash.create_timestamp(end_datetime)

    query = geohash.create_geohash_range_query(start_timestamp, end_timestamp)
    # print(query)

    no_result_json = {"type": "FeatureCollection","crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },"features":[]}

    try:

        connect_str = "dbname='{}' user='{}' password='{}' host='{}'".format(dbname,user,password,host)
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        geo_json = geohash.to_geojson(rows)
        assert geo_json == no_result_json
        cursor.close()
        conn.close()
    except Exception as e:
        # pass
        print("\nUh oh, can't connect. Invalid dbname, user or password? \n")
        print(e)