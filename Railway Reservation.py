import pymysql as sql 
conn=sql.connect(host="localhost",user="root",passwd="",database="test")
cursor=conn.cursor()

def menu():
    print(" --------------------------------------------------------------------------------------------")
    print("                          Welcome To Railway Reservation ")
    print("1. Book a Ticket")
    print("2. Show Records")
    print("3. Cancel Ticket")
    print("4. To modify passenger details")
    print("5. To see specific passenger information")
    print()
    print("We have Trains connecting the following stations ---                FARE(in Rupees)")
    print()
    print("12649.--Howrah <--> Amritsar ===> Amritsar Express          (AC1-6200/AC2-4050/Sleeper-800)")
    print("12658.--Howrah <--> Chennai ===> Chennai Mail               (AC1-6500/AC2-4200/Sleeper-1300)")
    print("22643.--Durgapur <--> Patna ===> Patna Express              (AC1-3850/AC2-2050/Sleeper-500)")
    print("21875.--Burdwan <--> Jodhpur ===> Jodhpur Express           (AC1-6850/AC2-4280/Sleeper-1200)")
    print("32566.--Mumbai <--> Durgapur ===> Mumbai Mail               (AC1-6230/AC2-4170/Sleeper-1120)")
    print("12431.--New Delhi <--> Sealdah ===> Rajdhani Express        (AC1-8320/AC2-5300/Sleeper-3000)")
    print("25467.--Mumbai <--> Goa ===> Goa Express                    (AC1-2350/AC2-1510/Sleeper-350)")
    print("21576.--Asansol <--> Jammu ===> Jammu Tawai Express         (AC1-5740/AC2-3950/Sleeper-1270)")
    print("37981.--Kolkata <--> Puri ===> Puri Express                 (AC1-2850/AC2-1880/Sleeper-650")
    print("32356.--New Jalpaiguri <--> Burwan ===> Uttar Banga Express (AC1-3625/AC2-1950/Sleeper-625)")
    print()
    
def add_passengers():
    print("***********  PLEASE ENTER ALL YOUR DETAILS IN CAPITAL BLOCK LETTERS  ***********")
    L=[]
    trainno=int(input("ENTER TRAIN NO. : "))
    L.append(trainno)
    date=input("ENTER DATE (in the form of DD-MM-YYYY) : ")
    L.append(date)
    cls=input("ENTER CLASS(AC1/AC2/Sleeper) : ")
    L.append(cls)
    source=str(input("ENTER SOURCE : "))
    L.append(source)
    destination=str(input("ENTER DESTINATION : "))
    L.append(destination)
    a="SELECT `destination` FROM `traindetails` WHERE tnum={}".format(trainno)
    cursor.execute(a)
    df1=cursor.fetchall()
    s1=str(df1)
    x1=s1[3:len(s1)-5]
    y1=x1.upper()
    b="SELECT `source` FROM `traindetails` WHERE tnum={}".format(trainno)
    cursor.execute(b)
    df2=cursor.fetchall()
    s2=str(df2)
    x2=s2[3:len(s2)-5]
    y2=x2.upper()
    if (source==y2)and(destination==y1):
        pname=input("ENTER PASSENGER'S NAME : ")
        L.append(pname)
        age=input("ENTER AGE : ")
        L.append(age)
        sex=input("ENTER SEX (M/F) : ")
        L.append(sex)
        amt=input("ENTER AMOUNT : ")
        L.append(amt)
        pnrno=input("ENTER THE PNRNO./Ticket ID - ")
        L.append(pnrno)
        status=input("ENTER STATUS : ")
        L.append(status)
        stno=int(input("ENTER SEAT NUMBER : "))
        L.append(stno)
        sql="INSERT INTO `passengers`(`trainno`, `date`, `cls`, `source`, `destination`, `pname`, `age`, `sex`, `amt`, `pnrno`, `status`, `stno`) VALUES({},'{}','{}','{}','{}','{}',{},'{}',{},{},'{}',{})".format(trainno,date,cls,source,destination,pname,age,sex,amt,pnrno,status,stno)                                        
        cursor.execute(sql)
        conn.commit()
        print('Record of passenger inserted')
    else:
        print("SORRY !, ENTERED DETAILS DO NOT MATCH WITH OUR SERVICES.")
 
def show_passengers():
    
    print('ALL PASSENGERS DETAIL')
    a="select * from passengers"
    cursor.execute(a)
    df=cursor.fetchall()
    for i in df:
        print(i)  

def cancel():
    t=0
    print("BEFORE ANY CHANGES IN THE STATUS")
    cursor.execute("select * from passengers")
    y=int(input("Enter the passenger's pnrno ="))
    df=cursor.fetchall()
    for i in df:
        if i[-3]==y:
            gul=i
            t=1
            break
    if t==1:
        b="DELETE FROM `passengers` WHERE pnrno={}".format(y)
        cursor.execute(b)
        conn.commit()
        print("YOUR TICKET HAS BEEN CANCELLED.")
    else:
        print(str(y)+" is invalid PNRNO.")
            
def disp_pnrno():
    t=0
    print("PNR STATUS WINDOW")
    a=int(input("ENTER your PNRNO : "))   
    y="select * from passengers"
    cursor.execute(y)
    df=cursor.fetchall()
    for i in df:
        if i[-3]==a:
            info=i
            t=1
            break
    if t==1:
        print(info)
    else:
        print(str(a)+"it is Invalid PNR")
              
def update_passengers():
    print("DETAIL TO BE MODIFIED -")
    print("1. Passenger Name")
    print("2. Passenger Age")
    print("3. Class")
    cho=int(input("Enter choice = "))
    i=int(input("enter PNRNO. -"))
    if cho==1:
        t=0
        a=input("Modified Name :")
        y="select * from passengers"
        cursor.execute(y)
        df=cursor.fetchall()
        for data in df:
            if data[-3]==i:
                info=data
                t=1
                break
        if t==1:
            z="UPDATE `passengers` SET `pname`='{}' WHERE pnrno={}".format(a,i)
            cursor.execute(z)
            conn.commit()
            print("NAME UPDATED")
        else:
            print(str(i)+"it is Invalid PNRNO")
            
    elif cho==2:
       t=0
       b=int(input("Modified age :"))
       y="select * from passengers"
       cursor.execute(y)
       df1=cursor.fetchall()
       for data in df1:
           if data[-3]==i:
               info=data
               ti=1
               break
       if ti==1:
           z="UPDATE `passengers` SET `age`='{}' WHERE pnrno={}".format(b,i)
           cursor.execute(z)
           conn.commit()
           print("AGE UPDATED")
       else:
           print(str(i)+"it is Invalid PNRNO")
        
    elif cho==3:
        d=input("Modified Class =")
        j=int(input("enter train number ="))
        if d=="AC1":
            trf1="select * from traindetails where tnum={}".format(j)
            cursor.execute(trf1)
            df1=cursor.fetchall()
            for i in df1:
                if i[0]==j:
                    gul=int(i[-3])
                    t=1
                break
            if t==1:
                b1="UPDATE `passengers` SET cls='{}',amt={} WHERE pnrno={}".format(d,gul,j)
                cursor.execute(b1)
                conn.commit()
        elif d=="AC2":
            trf2="select * from traindetails where tnum={}".format(j)
            cursor.execute(trf2)
            df2=cursor.fetchall()
            for i in df2:
                if i[0]==j:
                    gul=int(i[-2])
                    t=1
                break
            if t==1:
                b2="UPDATE `passengers` SET cls='{}',amt={} WHERE pnrno={}".format(d,gul,j)
                cursor.execute(b2)
                conn.commit()
        elif d=="Sleeper":
            trf3="select * from traindetails where tnum={}".format(j)
            cursor.execute(trf3)
            df3=cursor.fetchall()
            for i in df3:
                if i[0]==j:
                    gul=int(i[-1])
                    t=1
                break
            if t==1:
                b3="UPDATE `passengers` SET cls='{}',amt={} WHERE pnrno={}".format(d,gul,j)
                cursor.execute(b3)
                conn.commit()
        print("RECORD UPDATED")

menu()
while True:
    opt=int(input("ENTER YOUR CHOICE = "))
    if opt==1:
        print(add_passengers())
    elif opt==2:
        show_passengers()
    elif opt==3:
        cancel()
    elif opt==4:
        print(update_passengers())
    elif opt==5:
        disp_pnrno()
    else:
        print("INVALID OPTION !")
    x=input("DO YOU WANT TO CONTINUE?(y/n) - ")
    if x=='n' or x=='N':
        break
    else:
        continue
