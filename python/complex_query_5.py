import psycopg2
import sys
import csv

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')
    #print description of the query
    print("This query returns the feedback of the given fid to an employee.")
    print("It also inserts into the Review relation, to keep track of who viewed which feedback.")
    #Giving cues for the inputs
    print("\nInput: 5, 4\n")
    
def viewFeedback():
    #asking user for user id to show input
    heading("View Feedback")    
    fid = input("Feedback ID: ")
    eid = input("Employee ID: ")
    viewFeedbackHelper(fid, eid)

def viewFeedbackHelper(fid, eid):
    #executing the query itself
    tmpl = '''
        INSERT INTO Review(feedback_id, employee_id)
            VALUES(%s, %s)
    '''
    

    tmpl2 = '''
        SELECT comment
          FROM Feedbacks
         WHERE feedback_id = %s
    '''

    cmd = cur.mogrify(tmpl, [fid, eid])
    cur.execute(cmd)
    #nothing to print for tmpl

    cmd = cur.mogrify(tmpl2, [fid])
    cur.execute(cmd)
    rows = cur.fetchall()
    #print feedback
    for row in rows:
        print("\nFeedback: %s" % (row))
 
        
if __name__ == '__main__': #main method
    try:
        db, user = 'venmo', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        viewFeedback()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))