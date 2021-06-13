import os
import sqlite3
os.chdir(os.getcwd())
chek = 0
def dbank():
    if chek == 0:
        dbanq = input \
            ("Do you want to create a new drug bank ? Doing so will clear any existing database.. y for yes..n for no?\n")
    else:
        dbanq = input("Drug bank not found..do you want to create one..y for yes..n for no?\n")
    while dbanq.lower() != "y" and dbanq.lower() != "n":
        print("Enter a valid response  y or n !!!")
        if chek == 0:
            dbanq = input \
                ("Do you want to create a new drug bank ? Doing so will erase any previous drug bank record. y for yes..n for no?\n")
        else:
            dbanq = input("Drug bank not found..do you want to create one..y for yes..n for no?\n")

    if dbanq.lower( )== "y":
        print("Please wait a few seconds while your drug bank file is being created..")
        index = 0

        with open("drug_list.csv") as pr:
            creadb = sqlite3.connect("drugdb.db")
            c = creadb.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS drugdb(No INTEGER,drugs TEXT,Shelf_no TEXT)")
            clear = "DELETE FROM drugdb"
            c.execute(clear)
            for drug in pr:
                index = index + 1
                drug = drug.replace(",", "")
                drug = drug.strip('\n')
                shelf = ""


                c.execute("INSERT INTO drugdb VALUES(?,?,?)",(index,drug,shelf))
            creadb.commit()

    elif dbanq.lower() == "n":
        print("Okay")
        return "nothing"
dbank()
while True:
    chek = 1

    if os.path.isfile("drugdb.db"):

        try:
            creadb = sqlite3.connect("drugdb.db")
            c=creadb.cursor()
        except:
            print("Something went wrong in file opening")
            chek=0
            dbank()
            continue
        question = ""
        while question != "1" and question != "2" and question != "3" :
            question=input("Input '1' for drug location, '2' to know the drugs in any location and '3' to add a drug to the database.\n")
        if question == "1":
            drugloc = []
            dimp = input("Input drug\n")

            c.execute("SELECT No,drugs FROM drugdb WHERE drugs LIKE ?",('%'+dimp+'%',))
            drugloc = c.fetchall()[:]

            for row in drugloc:
                print("No:",row[0],"Drug:",row[1])





            if len(drugloc) > 0:
                numput = ""
                w = 0
                while w == 0:
                    try:
                        numput = int(input("Enter corresponding valid number to get drug location.\n"))
                    except:
                        ValueError
                        continue

                    w=1

                c.execute("SELECT * FROM drugdb WHERE No == ?",(numput,))
                locshow = c.fetchall()[:]
                print("The drug",locshow[0][1],"is at Location :",locshow[0][2])
                chput = ""
                while chput.lower() != "y" and chput.lower() != "n":

                    chput = input("Do you want to edit the location? y for yes..n for no \n")
                if chput.lower() == "y":
                    location = input("Enter the shelf_no\n")
                    c.execute("UPDATE drugdb SET shelf_no = ? WHERE No == ?",(location,numput))
                    creadb.commit()
                    c.execute("SELECT * FROM drugdb WHERE No == ?", (numput,))
                    change=c.fetchall()[:]
                    
                    print("DRUG:",change[0][1] ,"is at" ,"SHELF",change[0][2] )


                elif chput.lower() == "n":
                    pass
            elif len(drugloc) == 0:
                print('Drug not found')
        elif question == "2":
            shelf = input("Input shelf location\n")
            c.execute("SELECT * FROM drugdb WHERE Shelf_no == ?",(shelf,))
            lhold = c.fetchall()[:]
            print("The drugs in shelf",shelf,'are :')
            for row in lhold:
                print(row[1])

        elif question == "3":
            new_drug = input("Enter the name of the new drug\n")
            new_drug = new_drug.upper()
            shelf = input("Enter the shelf number\n")
            c.execute("SELECT * FROM drugdb")
            index = len(c.fetchall()) + 1
            c.execute("INSERT INTO drugdb VALUES(?,?,?)",(index,new_drug,shelf))
            creadb.commit()
            
    else:
        resp = dbank()
        if resp == "nothing":
            break


