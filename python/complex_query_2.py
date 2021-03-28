import psycopg2
import sys
import csv

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')
    #print description of the query
    print("This query prints the summary of all transactions of a given user.")
    print("Summary measures include sum, average, min and max of sent and received amounts.")
    #Giving cues for the inputs
    print("\nInput: evan-feder\n") 

def print_tuples(rows):
    #format the print so that it is easy to undertsand
    print("Total\tAverage\tMin\tMax")
    for row in rows:
        a, b, c, d = row
        print("%s\t%s\t%s\t%s"%(a,b,c,d))
    
def getSummary():
    heading("Summary of Transactions between Peers")
    uid = input("User ID: ")
    getSummaryHelper(uid)

def getSummaryHelper(uid):

    #This query returns the summary of sent amounts
    tmpl = '''
        SELECT sum(t.amount), avg(t.amount), min(t.amount), max(t.amount)
          FROM Users as u
          JOIN P2P_Transactions as pt
               ON u.user_id = pt.user_id_sender
          JOIN Transactions as t
               ON pt.transaction_id = t.transaction_id
         GROUP BY u.user_id
        HAVING u.user_id = %s --input_id
    '''

    #This query returns the summary of received amounts
    tmpltwo = '''
        SELECT sum(t.amount), avg(t.amount), min(t.amount), max(t.amount)
          FROM Users as u
          JOIN P2P_Transactions as pt
               ON u.user_id = pt.user_id_receiver
          JOIN Transactions as t
               ON pt.transaction_id = t.transaction_id
         GROUP BY u.user_id
        HAVING u.user_id = %s --input_id
         '''
    
    
    cmd = cur.mogrify(tmpl, [uid])
    cur.execute(cmd)
    rows = cur.fetchall()
    print(type(rows[0]))
    print("\nSummary of Sent Amounts")
    print_tuples(rows)


    cmd = cur.mogrify(tmpltwo, [uid])
    cur.execute(cmd)
    rows = cur.fetchall()
    print("\nSummary of Received Amounts")
    print_tuples(rows)

   

        
if __name__ == '__main__':
    try:
        db, user = 'venmo', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        getSummary()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))