"""
Dummy Project that will display the total marks obtained by students in different 
subjects based on the selections made 
in the console"""

#import the required libraries

import sqlite3

"""
Writing the program as Class-object model
"""

class SQLConnector:

    def __init__(self,database,con=0):
        self.con = sqlite3.connect(database)

    def apply_logic(self,num):
        cur = self.con.cursor()
        cur.execute("SELECT sum(marks) FROM students WHERE subject ='Chemistry'")
        chem_marks = cur.fetchall()
        cur.execute("SELECT sum(marks) FROM students WHERE subject ='Physics'")
        phy_marks = cur.fetchall()
        cur.execute("SELECT sum(marks) FROM students WHERE subject ='Biology'")
        bio_marks = cur.fetchall()
        switcher ={
            1:chem_marks,
            2:phy_marks,
            3:bio_marks
        }

        result = switcher.get(num,'-1')

        if result is not '-1':
            for i in result:
                for j in range(len(i)):
                    return result[j][0]
        else:
            return "Invalid Operation"

        self.con.commit()
        self.con.close()

    if __name__=="__main__":
        print("Select any number below in order to run the required condition")
        print("Type 1 to display the total marks scored by Students in Chemistry")
        print("Type 2 to display the total marks scored by Students in Physics")
        print("Type 3 to display the total marks scored by Students in Biology")
        n = int(input())
        sql = SQLConnector("python-sql.db")
        print(sql.apply_logic(n))
