import psycopg2
import sys
import csv

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')    
    #Giving cues for the inputs
    
    #print description of the query
    
    print("This query displays summary statistics of a Store")
    
    print("It shows the min, max, average of the amount of each transactions, frequency of purchase, and items bought and the age statistics of a customer")
    print("\nExample input = Store Id: snek \n")
def print_rows(rows):
    for row in rows:
        print(row)
    
def showSummaryStatistics():
    #main function
    heading("Show a summary of statistics of my customers")
    print()
    sid = input("Store ID: ")
    showSummaryStatisticsHelper(sid)

def showSummaryStatisticsHelper(sid):
    #executing the query itself
    tmpl = '''
    SELECT count(*), avg(t.amount::numeric), min(t.amount), max(t.amount)
      FROM Business_Users as b
      JOIN P2B_Transactions as pb
        ON b.user_id = pb.user_id_business
      JOIN Transactions as t
        ON pb.transaction_id = t.transaction_id
     WHERE b.user_id = %s
    '''
    
    tmpltwo = '''
    SELECT avg(p.age), min(p.age), max(p.age)
      FROM Business_Users as b
      JOIN P2B_Transactions as pb
        ON b.user_id = pb.user_id_business
      JOIN Personal_Users as p
        ON pb.user_id_personal = p.user_id
     WHERE b.user_id = %s
     '''
     
    tmplthree = '''
    SELECT gs.name, sum(b.quantity)
      FROM Goods_Services as gs
      JOIN Bought as b
        ON gs.item_id = b.item_id
      JOIN P2B_Transactions as pb
        ON b.transaction_id = pb.transaction_id
      JOIN Business_Users as bu
        ON pb.user_id_business = bu.user_id 
     WHERE bu.user_id = %s
     GROUP BY gs.item_id, gs.name 
     '''
     
     #print results
    cmd = cur.mogrify(tmpl, [sid])
    cur.execute(cmd)
    
    rows = cur.fetchall()
    print()
    print("AMOUNT STATISTICS")
    for row in rows:
        count, average, min, max = row
        print("Count: \t\t%s" % count)
        print("Average: \t%s" % average)
        print("Min: \t\t%s" % min)
        print("Max: \t\t%s\n" % max)
        
        
    cmd = cur.mogrify(tmpltwo, [sid])
    cur.execute(cmd)
    
    rows = cur.fetchall()

    print("AGE STATISTICS")
    for row in rows:
        average, min, max = row
        print("Average: \t%s" % (average))
        print("Min: \t\t%s" % (min))
        print("Max: \t\t%s\n" % (max))
        
        
    cmd = cur.mogrify(tmplthree, [sid])
    cur.execute(cmd)
    
    rows = cur.fetchall()

    print("ITEM STATISTICS")
    print("name\t|quantity")
    print("---------------------")
    for row in rows:
        name,q = row
        print("%s\t|%s" % (name, q))
    
    print()
    print("Done!")
        
        
if __name__ == '__main__':
    try:
        db, user = 'venmo', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        showSummaryStatistics()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))