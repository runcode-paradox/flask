import mysql.connector

m = mysql.connector.connect(host="localhost",
                            port="3306",
                            user="root",
                            password="mypass",
                            database="devi",
                            auth_plugin='mysql_native_password')
# k = mysql.connector.connect('localhost',)
b = m.cursor()
b.execute("select * from doctor")
n=b.fetchall()
l=[]
def inii():
    for i in range(0,len(n)):
        d_name=n[i][1]
        h_name=n[i][2]
        rank=n[i][5]
        fees=n[i][3]
        spec=n[i][4]
        pic=n[i][7]
        d={"d_name":d_name,"h_name":h_name,"rank":rank,"fee":fees,"spec":spec,"pic":pic}
        l.append(d)
    return l
# b.execute("select * from orghospital where location like 'd%'")
# r=b.fetchall()
# l=[]
# for i in r:
#     l.append(i)
# print(l)
d=inii()

