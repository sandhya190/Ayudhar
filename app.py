from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rojelin')
def rojelin():
    return render_template('rojelin.html')

@app.route('/receiver')
def receiver():
    return render_template('receiver.html')

@app.route('/receiveform')
def receiveform():
    return render_template('receiveform.html')

@app.route('/bbcenterindex')
def bbcenterindex():
    return render_template('bbcenterindex.html')

def create_connection():
    conn=sqlite3.connect('ayudhar_db.db')
    return conn

def  create_table():
    conn=create_connection()
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS donor_info(
                          Firstname TEXT NOT NULL,
                          Lastname TEXT NOT NULL,
                          Age INTEGER,
                          Gender TEXT NOT NULL,
                          BloodGroup TEXT NOT NULL,
                          AnyHealthIssue TEXT NOT NULL,
                          DoYouSmoke TEXT NOT NULL,
                          DoYouDrink TEXT NOT NULL,
                          Username TEXT NOT NULL,
                          City TEXT NOT NULL,
                          Pincode INTEGER)''')
    conn.commit()
    conn.close()




@app.route('/donateform',methods=['POST','GET'])
def donateform():
    if request.method == 'POST':
       Firstname=request.form['First_name']
       Lastname=request.form['Last_name']
       Age=request.form['Age']
       Gender=request.form['Gender']
       BloodGroup=request.form['BloodGroup']
       AnyHealthIssue=request.form['AnyHealthIssue']
       DoYouSmoke=request.form['DoYouSmoke']
       DoYouDrink=request.form['DoYouDrink']
       Username=request.form['Username']
       City=request.form['City']
       Pincode=request.form['Pincode']
       conn=create_connection()
       conn.cursor().execute('''INSERT INTO donor_info('Firstname','Lastname','Age','Gender','BloodGroup','AnyHealthIssue','DoYouSmoke','DoYouDrink','Username','City','Pincode')VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(Firstname,Lastname,Age,Gender,BloodGroup,AnyHealthIssue,DoYouSmoke,DoYouDrink,Username,City,Pincode))

       conn.commit()
       conn.close()
    return render_template('donateform.html')

def  create_r_table():
    conn=create_connection()
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS receiver_info(
                          Firstname TEXT NOT NULL,
                          Lastname TEXT NOT NULL,
                          Age INTEGER,
                          Gender TEXT NOT NULL,
                          BloodGroup TEXT NOT NULL,
                          Username TEXT NOT NULL,
                          City TEXT NOT NULL,
                          Pincode INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/receiveform',methods=['POST','GET'])
def receiveform():

    if request.method == 'POST':
       Firstname=request.form['First_name']
       print(Firstname)
       Lastname=request.form['Last_name']
       Age=request.form['Age']
       Gender=request.form['Gender']
       BloodGroup=request.form['BloodGroup']
       Username=request.form['Username']
       City=request.form['City']
       Pincode=request.form['Pincode']
       conn=create_connection()
       conn.cursor().execute('''INSERT INTO receiver_info('Firstname','Lastname','Age','Gender','BloodGroup','Username','City','Pincode')VALUES(?,?,?,?,?,?,?,?,?)''',(Firstname,Lastname,Age,Gender,BloodGroup,Username,City,Pincode))

       conn.commit()
       conn.close()
    return render_template('receiveform.html')


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/rojelin')
# def rojelin():
#     return render_template('rojelin.html')

# @app.route('/receiver')
# def receiver():
#     return render_template('receiver.html')

# # @app.route('/receiveform')
# # def receiverform():
# #     return render_template('receiveform.html')

# @app.route('/bbcenterindex')
# def bbcenterindex():
#     return render_template('bbcenterindex.html')








if __name__ == '__main__':
    create_table()
    app.run(debug=True)