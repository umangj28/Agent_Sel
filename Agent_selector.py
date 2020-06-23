import random
import numpy
import mysql.connector

#Method is_avialable takes list of agents(of specified role) as an argument and returns true if the agent is available else false
def is_available(name):
    sql="select availability from agent_status where agent_name='"+name+"'" #extracting data from mysql database
    mycursor.execute(sql)
    myresult1=mycursor.fetchall()
    for x in myresult1:
        if (''.join(x))=='Yes':
            return True
        elif (''.join(x))=='No':
            return False

# Function is_available takes the list of agents(of the specified roles) as input and returns the time since the agent is available.
def available_since(name):
    maxx=0
    mycursor.execute("select days from agent_status where agent_name='"+name+"'")
    result3 = mycursor.fetchall()
    r=list(sum(result3,()))
    for i in r:
        if i!=None:
            return i

#Function issue takes user inputs i.e. list of required roles and the availablity mode, and returns the agents by checking all the constraints.
def issue(agent_list,agent_mode):
    l=[]
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="mysql123", database="mysql")
    mycursor.execute("select roles from agent_status")
    result1 = mycursor.fetchall()
    for i in agent_list:
        mycursor.execute("select agent_name from agent_status where roles like '%"+i+"%'")
        c = mycursor.fetchall()
        l+=c  #list l stores all the agents from the database that have the exact matching roles as given by the user.
    l3=[]
    z=[]
    for i in l:
        a=(is_available(''.join(i))) #from list l we check which agents are currently available
        l1=list(sum(l,()))
        if a==True:
            z+=i    #currently available agents are stored in list z.
    #print(z)
    b=[]
    if agent_mode=='all available': #if mode is all_available then all agents with the matching roles are returned, if the given roles are sales,support
                                    #the agents which have both sales and support as their roles are returned.
        for j in set(z):
            if z.count(j)==len(agent_list):
                l3.append(j)
        return l3
    elif agent_mode=='least busy': #in least busy mode the agents who are available from the longest time are returned.
        for i in z:
            v=available_since(i)
            b.append(v)
        #print(b)
        f="select agent_name from agent_status where days='"+str(max(b))+"'"
        mycursor.execute(f)
        return mycursor.fetchall()
    elif agent_mode=='random': #in random mode a agent having the matching roles is randomly returned.
        for j in set(z):
            if z.count(j)==len(agent_list):
                l3.append(j)
        return random.choices(l3)
    else:
        return "Incorrect availability mode"

if __name__=="__main__":
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="mysql123", database="mysql")
    mycursor = mydb.cursor()
    print("Enter the roles list(sales/support/spanish-speaker) in order to obtain the agents alotted to the same:")
    al=list(input().split())
    print("Enter the availability modes from the three:all available,least busy,random:")
    am=input()
    print(issue(al,am))