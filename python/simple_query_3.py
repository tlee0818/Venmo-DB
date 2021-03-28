import psycopg2
import sys
import csv

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')
    #print description of the query
    print("This query changes the privacy of a given transaction.\n")
    #Giving cues for the inputs
    print("Input: 8, Private\n")
    
def changePrivacy():
    #asking user for user id to show input
    heading("Change Privacy")    
    tid = input("Transaction ID: ")
    p = input("New Privacy: ")
    changePrivacyHelper(p, tid)

def changePrivacyHelper(p, tid):
    #executing the query itself
    tmpl = '''
        UPDATE Transactions
               SET privacy = %s
         WHERE transaction_id = %s
    '''
    cmd = cur.mogrify(tmpl, [p, tid])
    cur.execute(cmd)

    print("\nDone! Privacy has been updated. :)\n")

 
        
if __name__ == '__main__': #main method
    try:
        db, user = 'venmo', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        changePrivacy()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))