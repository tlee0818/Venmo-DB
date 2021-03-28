import psycopg2
import sys
import csv

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')
    #print description of the query
    print("This query performs a transaction between two personal users")
    print("Thus, it changes the balance of the two users and adds a new row in Transactions and P2P_Transactions.")
    #Giving cues for the inputs
    print("Input: eileenmao, evan-feder, blocks, Private, 2017-12-07 11:59:00, 10.00 (in order)\n") 

def print_rows(rows):
    for row in rows:
        print(row)
    
def doTransaction():
    heading("Transaction between personal users")
    sid = input("Sender ID: ")
    rid = input("Receiver ID: ")
    d = input("Description of Transaction: ")
    p = input("Privacy(Private, Friends, Public): ")
    ts = input("Time(YYYY-MM-DD HH:TT:SS):")
    amt = input("Amount(##.##): ")
    doTransactionHelper(sid, rid, d, p, ts, amt)

def doTransactionHelper(sid, rid, d, p, ts, amt):
    tmpl = '''
        UPDATE Users
           SET balance = balance - %s
         WHERE user_id = %s
    '''
    
    tmpltwo = '''
        UPDATE Users
           SET balance = balance + %s
         WHERE user_id = %s
         '''
         
    tmplthree = '''
        INSERT INTO Transactions (amount, description, privacy, timestamp)
        VALUES (%s, %s, %s, %s);
'''

    tmplfour = '''
    INSERT INTO P2P_Transactions(transaction_id, user_id_sender, user_id_receiver)
    VALUES((SELECT max(transaction_id)
        FROM Transactions),  %s, %s);
        '''
    
    
    cmd = cur.mogrify(tmpl, [amt, sid])
    cur.execute(cmd)

    cmd = cur.mogrify(tmpltwo, [amt, rid])
    cur.execute(cmd)
    
    cmd = cur.mogrify(tmplthree, [amt, d, p, ts])
    cur.execute(cmd)
    
    cmd = cur.mogrify(tmplfour, [sid, rid])
    cur.execute(cmd)
    
    #There is nothing to print, as the query has no select statement, thus not returning anything
    print("\nDone! Everything has been updated. :)\n")
    #print description of the query
    print("This query performs a transaction between two personal users")
    print("Thus, it changes the balance of the two users and adds a new row in Transactions and P2P_Transactions.")

        
if __name__ == '__main__':
    try:
        db, user = 'venmo', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        doTransaction()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))