import psycopg2
from datetime import datetime
import json

def to_geojson(rows, root='features'):

    return "{\"type\": \"FeatureCollection\"," + \
    "\"crs\": { \"type\": \"name\", \"properties\": { \"name\": \"urn:ogc:def:crs:OGC:1.3:CRS84\" } }," +\
    "\"" + root + "\":" + json.dumps(rows, separators=(',', ':')) + "}"


def create_timestamp(datetime_string):
    datetime_value = datetime.strptime(datetime_string, '%m-%d-%y %H:%M:%S %Z')
    # print("datetime value=", datetime_value)
    date_timestamp = int(datetime.timestamp(datetime_value))
    # print("date timestamp =", date_timestamp)

    return date_timestamp

def create_geohash_range_query(start_timestamp, end_timestamp):
    return """SELECT row_to_json((select l from
        ( select 'Feature' as type, st_asgeojson(wkb_geometry)::json as geometry,
            (select row_to_json(t) from
                (select (select count(*) from image_metadata
                    where captured_on_epoch > {start}
                    and  captured_on_epoch < {end}),
                    ST_GeoHash(wkb_geometry,8) "geohash", '#00ff00' as color) t) as "properties" ) as l))
            from image_metadata
            where captured_on_epoch > {start}
            and  captured_on_epoch < {end}""".format(start=start_timestamp, end=end_timestamp)


if __name__ == "__main__":


    import argparse

    parser = argparse.ArgumentParser(description='give a date range to output a geojson within that ranges')
    parser.add_argument('-d', required=True, help="database")
    parser.add_argument('-u', required=True, help="user")
    parser.add_argument('-p', required=True, help="password")
    parser.add_argument('-host', required=True, help="host")
    parser.add_argument('-start', required=True, help="start date in the format of mm-dd-yy HH:MM:SS timezone")
    parser.add_argument('-end', required=True, help="end date in the format of mm-dd-yy HH:MM:SS timezone")
    args = parser.parse_args()

    # current date and time
    start_datetime = args.start
    end_datetime = args.end
    start_timestamp = create_timestamp(start_datetime)
    end_timestamp = create_timestamp(end_datetime)
    dbname = args.d
    user = args.u
    password = args.p
    host = args.host

    query = create_geohash_range_query(start_timestamp, end_timestamp)

    try:

        connect_str = "dbname='{}' user='{}' password='{}' host='{}'".format(dbname,user,password,host)
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(to_geojson(rows))
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)