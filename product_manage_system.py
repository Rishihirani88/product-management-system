import mysql.connector as mysql
import tabulate as tb
con=mysql.connect(host="localhost",user="root",password="root",database="project")
cur=con.cursor()
def additem():
    pid=int(input("enter product id:-"))
    pname=input("enter product name:-")
    q=int(input("enter quantity of product in grams :-"))
    p=int(input("enter price of product:-"))
    qu="insert into product values({0},'{1}',{2},{3})".format(pid,pname,q,p)
    #"insert into product values({},'{}',{},{})".format(pid,pname,q,p)
    cur.execute(qu)
    con.commit()
    repeat()
def updateitem():
     opid=int(input("enter OLD product id:-"))
     pid=int(input("enter NEW product id:-"))
     pname=input("enter product name:-")
     q=int(input("enter quantity of product in grams :-"))
     p=int(input("enter price of product:-"))
     b=("update product set pid='{}',pname='{}',quantity_in_g='{}',price='{}' where pid='{}'").format(pid,pname,q,p,opid)
     cur.execute(b)
     no=cur.rowcount
     print("{} row(s) deleted".format(no))
     con.commit()
     print("Updating Completed")
     repeat()
def deleteitem():
    pid=int(input("enter product id that to be deleted:-"))
    d="delete from product where pid='{}'".format(pid)
    cur.execute(d)
    no=cur.rowcount
    print("{} row(s) deleted".format(no))
    con.commit()
    print("done")
    repeat()
def viewitem():
    a=cur.execute("select * from product")
    a=cur.fetchall()
    colname=["Pid","pname"," quantity","price"]
    print(tb.tabulate(a,headers=colname,tablefmt="psql"))
    repeat()
def searchitem():
    pid=int(input("enter product id to be search:-"))
    q="select * from product where pid='{}'".format(pid)
    a=cur.execute(q)
    a=cur.fetchone()
    if a is not None:
        print("pid:-",a[0])
        print("product name:-",a[1])
        print("quantity:-",a[2])
        print("price:-",a[3])
    else:
        print("NO DATA FOUND")
    repeat()
def repeat():
    c=int(input("enter 0 to go back to the menu:-"))
    if c==0:
        menu()
    else:
        input("thank you see you soon:-)")    
def menu():
    print("WELCOME")
    print("SELECT FROM FOLLOWING OPTION TO PROCEED...")
    print("1.ADD")
    print("2.UPDATE")
    print("3.DELETE")
    print("4.VIEW")
    print("5.SEARCH")
    print("6. EXIT")
    i=int(input("enter your command:-"))
    if i==1:
        additem()
    elif i==2:
        updateitem()
    elif i==3:
        deleteitem()
    elif i==4:
        viewitem()
    elif i==5:
        searchitem()
    else:
        print("thank you see you soon:-)")
menu()
