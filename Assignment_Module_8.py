#1
import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='pass_word',
    autocommit=True
)

def getICAOairport(ident):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident ='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The Airport name is: {row[0]} and municipality is: {row[1]}")
    return


ident = input("Enter the ICAO: ")
getICAOairport(ident)



#2
def getICAO(iso_country):
    sql = "SELECT name, type FROM airport "
    sql += " WHERE iso_country ='" + iso_country + "'" + "order by type"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The Airport name is: {row[0]}, Type: {row[1]}")
    return


iso_country = input("Enter the Area code: ")
getICAO(iso_country)


#3

def distance1(ident):
    sql = "SELECT latitude_deg, longitude_deg FROM airport "
    sql += " WHERE ident ='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    location1 = result
    if cursor.rowcount > 0:
        for row in result:
            print(f"The latitude is: {row[0]}, longtitude: {row[1]}")
    return location1

ident1 = input("Enter the ICAO code: ")
distance1(ident1)

def distance2(ident):
    sql = "SELECT latitude_deg, longitude_deg FROM airport "
    sql += " WHERE ident ='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    location2 = result
    if cursor.rowcount > 0:
        for row in result:
            print(f"The latitude is: {row[0]}, longtitude: {row[1]}")
    return location2


ident2 = input("Enter the ICAO code: ")
distance2(ident2)

result1 = distance1(ident1)
result2 = distance2(ident2)

print("The distance is:", geodesic(result1, result2).km)


