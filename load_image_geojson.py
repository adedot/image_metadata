
import subprocess
from datetime import datetime, timedelta

def load_geojson_into_postgres(dbname,user, password, table, start, end):
    date_value = datetime.strptime(start, '%Y%m%d')
    end_date = datetime.strptime(end, '%Y%m%d')
    while date_value <= end_date:
        file = "{}.geojson".format(date_value.strftime('%Y%m%d'))
        date_value = date_value + timedelta(1)

        statement = 'ogr2ogr -f PostgreSQL PG:"dbname={} user={} password={}"' \
         ' {} -nln {} -append'.format(dbname,user, password, file, table)
        try:
            print(statement)
            subprocess.check_output(statement, shell=True)
            print("{} has been loaded into {}".format(file, table))
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="""python load_image_geojson.py -start {start} -end {end} -d {database} -u {user} -p {password}  -t {table}""")
    parser.add_argument('-start', required=True, help="start date in the format of yyyymmdd ie. 20180820")
    parser.add_argument('-end', required=True, help="end date in the format of yyyymmdd ie. 20180821")
    parser.add_argument('-d', required=True, help="database")
    parser.add_argument('-u', required=True, help="user")
    parser.add_argument('-p', required=True, help="password")
    parser.add_argument('-t', required=True, help="table")
    args = parser.parse_args()
    print(args)
    start = args.start
    end = args.end
    dbname = args.d
    user = args.u
    password = args.p
    table = args.t

    load_geojson_into_postgres(dbname,user, password, table, start, end)
