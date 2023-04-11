#WARNING: This program is just a demonstration of how json data can be loaded on a postgreSQL database using python and only works for AIRBNB Listings dataset from insideairbnb.com


#!/usr/bin/env python


import sys
import pandas as pd
import psycopg
from psycopg import sql
from io import StringIO
from datetime import datetime


# Defining the function to connect to the postgresql database
def connect(parameters):
    conn=None
    try:
        print('Connection to the PostgreSQL database...')
        conn=psycopg.connect(**parameters)
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn

# Defining extraction and transformation function
def extract_transform(filename):
    dataframe=pd.read_csv(filename)
    df_listing=dataframe[['id','host_id','listing_url','name','description']]
    df_host=dataframe[['host_id','host_url','host_name','host_verifications','host_identity_verified']]
    data=[df_listing,df_host]
    return data

# Defining table check function to verify the existense of tables in a given database
def table_check(tablename):
    cur=conn.cursor()
    string_1="SELECT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='"
    string_2=tablename
    string_3="');"

    query=string_1+string_2+string_3

    cur.execute(query)
    table_status=cur.fetchone()[0]   #Above query outputs a list in which first element is the boolean result of the query
    if table_status == False:
        create_table(tablename)

    cur.close()


# Defining create table function
def create_table(table):
    tablename=table
    cur=conn.cursor()
    if tablename=='listing':
        cur.execute(''' CREATE TABLE listing (
                                                id bigint PRIMARY KEY,
                                                host_id int,
                                                listing_URL varchar(60),
                                                name varchar(100),
                                                description varchar(1000),
                                                FOREIGN KEY (host_id) REFERENCES host(host_id)
                                                )
                                                ''')
    elif tablename=='host':
        cur.execute(''' CREATE TABLE host (
                                            host_id int PRIMARY KEY,
                                            host_url varchar(50),
                                            host_name varchar(40),
                                            host_verifications varchar(40),
                                            host_identity_verified varchar(1)
                                            )
                                            ''')
    conn.commit()
    cur.close()

#Defining function to load data into database

def load(conn,df,table):
    buffer=StringIO()
    df.to_csv(buffer,header=False,index=False)
    buffer.seek(0)
    cur=conn.cursor()
    
    #Creating a tmp table in the database
    cur.execute(f"CREATE TEMP TABLE tmp_table (LIKE {table})")
    
    #Loading the data from buffer into the tmp table
    try:
        with buffer as f:
            with cur.copy(sql.SQL("COPY tmp_table FROM STDIN WITH (FORMAT CSV)")) as copy:
                while data := f.read(1000000):  #Random block size 1000000
                    copy.write(data)

        #Copying from tmp_table to final table using INSERT ON CONFILCT DO NOTHING to avoid error due to duplicate values

        cur.execute(f"INSERT INTO {table} SELECT * FROM tmp_table ON CONFLICT DO NOTHING;")

        #Droping the tmp table
        cur.execute(f"DROP TABLE tmp_table;")
        conn.commit()

        print("Loading of csv  in database table ",table)


    except(Exception,psycopg.DatabaseError) as error:
        print('Error:%s',error)
        conn.rollback()
        cur.close()

    cur.close()

#Defining Log function
def log(message):
    timestamp_format='%Y-%h-%d-%H-%M-%S'
    now=datetime.now()
    timestamp=now.strftime(timestamp_format)
    with open ('logfile.txt','a') as f:
        f.write(timestamp+','+message+'\n')

# Main

if __name__=="__main__":
    if len(sys.argv)!= 7:
        print("")
        sys.exit(-1)

    tables=['host','listing']

    csv_file=sys.argv[1]
    param_dic={'host':sys.argv[2],
               'port':sys.argv[3],
               'user':sys.argv[4],
               'password':sys.argv[5],
               'dbname':sys.argv[6]
               }

    log("Connecting to Database...")
    conn=connect(param_dic)

    log("Extraction and Transformation Started")
    data=extract_transform(csv_file)
    log("Extraction and Transformation Completed")
    
    log("Checking tables")
    for table in tables:
        table_check(table)

    log("Checking of tables complete")
    

    log("Loading Listing Data into Listing Table")
    load(conn,data[0],'listing')
    log("Loading of Listing Table complete")

    log("Loading Host Data into Host Table")
    load(conn,data[1],'host')
    log("Loading of Host Table Complete")

    log("Process Complete")





