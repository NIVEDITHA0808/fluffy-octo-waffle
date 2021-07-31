import csv
import sys
import psycopg2


def insert(fname):

    dbconn = psycopg2.connect("dbname=superhero")
    cursor = dbconn.cursor()
    
    f=open(fname)
    reader = csv.reader(f) #a csv file can be written from DB with csv.writer(f) (check documentation)
    for name,gender in reader:
       
        print(name,gender)
        cursor.execute("INSERT INTO heroes (name, gender) VALUES (%s, %s)",(name, gender))
   
    dbconn.commit()
    
        
def main():
    fname = sys.argv[1]
    insert(fname)
    
main()
        
