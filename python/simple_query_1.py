import psycopg2
import sys
import csv

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')
    #printing description of the query
    print("This query returns the balance of the user corresponding to the user_id that has been inputted.\n")
    #Giving cues for the inputs
    print("Input: eileenmao\n")
    
def show_balance():
    #asking user for user id to show input
    heading("Show balance")    
    uid = input("User ID: ")
    show_balance_helper(uid)

def show_balance_helper(uid):
    #executing the query itself
    tmpl = '''
        SELECT balance
          FROM Users
         WHERE user_id = %s
    '''
    cmd = cur.mogrify(tmpl, [uid])
    cur.execute(cmd)
    rows = cur.fetchall()
    #print balance
    for row in rows:
        balance = row
        print("Balance: %s" % (balance))
    #printing description of the query
    print("\nThis query returns the balance of the user corresponding to the user_id that has been inputted.\n")
 
        
if __name__ == '__main__': #main method
    try:
        db, user = 'venmo', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        show_balance()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))