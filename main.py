from re import A
from flask import Flask, render_template, request, session
import flask
from flask_mysqldb import MySQL
import mysql.connector
from flask_session import Session
from werkzeug.utils import redirect

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# myconn = mysql.connector.connect(host="localhost", user="root", passwd="@Bhakauhet92", database="healthcare",
#                                  buffered=True)

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "200001044mysql",database="healthcare_portal", buffered=True)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')


@app.route('/hospRegisterInitial',methods=['GET','POST'])
def register_page_init():
    if request.method=='POST':
        hospDetails = request.form
        hospName = hospDetails['hospName']
        hosp_ID = hospDetails['hospID']
        hospPassword = hospDetails['hospPassword']
        cur = myconn.cursor()
        try:
            cur.execute("INSERT INTO Hospital(hosp_ID,hospName,hospPassword) VALUES(%s,%s,%s)",(int(hosp_ID),hospName,hospPassword))
            myconn.commit()
            cur.close()
            return redirect('/')
        except:
            print("ERROR!!!!")
            return render_template('hospital_reg_init.html')
    return render_template('hospital_reg_init.html')

@app.route('/hospRegisterUpdate',methods=['GET','POST'])
def register_page_update():
    if request.method=='POST':
        hosp_ID = session["hosp_ID"]
        hospDetails = request.form
        hospName = hospDetails['hospName']
        hospEmail = hospDetails['hospEmail']
        hospAddress = hospDetails['hospAddress']

        if len(hospName)>=1:
            hospName = hospDetails['hospName']
            update_query = "UPDATE hospital SET hospName='%s' WHERE hosp_ID='%s'"%(hospName,hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        if len(hospEmail)>=1:
            update_query = "UPDATE hospital SET hospEmail='%s' WHERE hosp_ID='%s'"%(hospEmail,hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()

        try:
            hospPhone = hospDetails['hospPhone']
            update_query = "UPDATE hospital SET hospPhone='%s' WHERE hosp_ID='%s'"%(hospPhone,hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        except:
            print("No Phone")

        if len(hospAddress)>=1:
            update_query = "UPDATE hospital SET hospAddress='%s' WHERE hosp_ID='%s'"%(hospAddress,hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        
    hosp_ID = session["hosp_ID"]
    sql_query = "SELECT * FROM hospital WHERE hosp_ID ='%s'" % (int(hosp_ID))
    cur = myconn.cursor()
    cur.execute(sql_query)
    hospDetails = cur.fetchall()
    
    return render_template('hospital_reg_update.html',hospDetails=hospDetails,hospName = session["hospName"]) 


@app.route('/hospLogin', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        hospDetails = request.form
        hosp_ID = hospDetails['hospID']
        hospPassword = hospDetails['hospPassword']

        sql_query = "SELECT * FROM Hospital WHERE hosp_ID ='%s' AND hospPassword ='%s'" % (int(hosp_ID), hospPassword)

        cur = myconn.cursor()
        cur.execute(sql_query)
        hospDetails = cur.fetchall()
        i = 0
        for row in hospDetails:
            i = i + 1
        myconn.commit()
        cur.close()

        if i == 1:
            session["hosp_ID"] = hospDetails[0][0]
            session["hospName"] = hospDetails[0][1]
            flask.flash("Successful Login")
            return render_template('hospital_after_login.html', hospName=session["hospName"])
        else:
            return render_template('hospital_login.html')
    return render_template('hospital_login.html')


@app.route('/hospAfterLogin', methods=['GET', 'POST'])
def hospital_homepage():
    return render_template('hospital_after_login.html', hospName=session["hospName"])


@app.route('/updateVaccine', methods=['GET', 'POST'])
def update_vaccine_details():
    if request.method == 'POST':
        newVaccDetails = request.form
        hosp_ID = session["hosp_ID"]
        try:
            new_v1 = int(newVaccDetails['v1'])
            update_query = "UPDATE VaccineDetails SET v1_quant='%s' WHERE hosp_ID='%s'" % (new_v1, hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        except:
            new_v1 = -1
        try:
            new_v2 = int(newVaccDetails['v2'])
            update_query = "UPDATE VaccineDetails SET v2_quant='%s' WHERE hosp_ID='%s'" % (new_v2, hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        except:
            new_v2 = -1
        try:
            new_v3 = int(newVaccDetails['v3'])
            update_query = "UPDATE VaccineDetails SET v3_quant='%s' WHERE hosp_ID='%s'" % (new_v3, hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        except:
            new_v3 = -1

    hosp_ID = session["hosp_ID"]
    sql_query = "SELECT * FROM VaccineDetails WHERE hosp_ID ='%s'" % (int(hosp_ID))
    cur = myconn.cursor()
    cur.execute(sql_query)
    hospVaccineDetails = cur.fetchall()

    return render_template('update_vaccine.html', hospVaccineDetails=hospVaccineDetails,
                           hospName=session["hospName"])  # Pass all vaccine details


@app.route('/addVaccine', methods=['GET', 'POST'])
def add_vaccine_details():
    if request.method == 'POST':
        cur = myconn.cursor()
        hosp_ID = session["hosp_ID"]
        cur.execute("INSERT INTO VaccineDetails(hosp_ID,v1_quant,v2_quant,v3_quant) VALUES(%s,%s,%s,%s)",
                    (int(hosp_ID), int(0), int(0), int(0)))
        myconn.commit()
        cur.close()
    return redirect('/updateVaccine')


@app.route('/updateOxygen', methods=['GET', 'POST'])
def update_oxygen_details():
    if request.method == 'POST':
        newOxyDetails = request.form
        hosp_ID = session["hosp_ID"]
        try:
            new_avail = int(newOxyDetails['lit_avail'])
            update_query = "UPDATE OxygenDetails SET litres_available='%s' WHERE hosp_ID='%s'" % (new_avail, hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        except:
            new_avail = -1
        try:
            new_supply = int(newOxyDetails['hourly_suppl'])
            update_query = "UPDATE OxygenDetails SET supply_per_hour='%s' WHERE hosp_ID='%s'" % (new_supply, hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        except:
            new_supply = -1
        try:
            new_price = int(newOxyDetails['price_pl'])
            update_query = "UPDATE OxygenDetails SET price_per_litre='%s' WHERE hosp_ID='%s'" % (new_price, hosp_ID)
            cur = myconn.cursor()
            cur.execute(update_query)
            myconn.commit()
            cur.close()
        except:
            new_price = -1

    hosp_ID = session["hosp_ID"]
    sql_query = "SELECT * FROM OxygenDetails WHERE hosp_ID ='%s'" % (int(hosp_ID))
    cur = myconn.cursor()
    cur.execute(sql_query)
    hospOxygenDetails = cur.fetchall()

    return render_template('update_oxygen.html', hospOxygenDetails=hospOxygenDetails,
                           hospName=session["hospName"])  # Pass all oxygen details


@app.route('/addOxygen', methods=['GET', 'POST'])
def add_oxygen_details():
    if request.method == 'POST':
        cur = myconn.cursor()
        hosp_ID = session["hosp_ID"]
        cur.execute(
            "INSERT INTO OxygenDetails(hosp_ID,litres_available,supply_per_hour,price_per_litre) VALUES(%s,%s,%s,%s)",
            (int(hosp_ID), int(0), int(0), int(0)))
        myconn.commit()
        cur.close()
    return redirect('/updateOxygen')


@app.route('/updateSurgery', methods=['GET', 'POST'])
def update_surgery_details():
    if request.method == 'POST':
        hosp_ID = session["hosp_ID"]
        newSurgeryDetails = request.form
        s1 = s2 = s3 = 0
        try:
            var1 = newSurgeryDetails["heart"]
            s1 = 1
        except:
            s1 = 0
        try:
            var2 = newSurgeryDetails["joint"]
            s2 = 1
        except:
            s2 = 0
        try:
            var3 = newSurgeryDetails["abdominal"]
            s3 = 1
        except:
            s3 = 0

        update_query = "UPDATE SurgeryDetails SET heart='%s',joint='%s',abdominal='%s' WHERE hosp_ID='%s'" % (
        s1, s2, s3, hosp_ID)
        cur = myconn.cursor()
        cur.execute(update_query)
        myconn.commit()
        cur.close()

    hosp_ID = session["hosp_ID"]
    sql_query = "SELECT * FROM SurgeryDetails WHERE hosp_ID ='%s'" % (int(hosp_ID))
    cur = myconn.cursor()
    cur.execute(sql_query)
    hospSurgeryDetails = cur.fetchall()

    return render_template('update_surgery.html', hospSurgeryDetails=hospSurgeryDetails,
                           hospName=session["hospName"])  # Pass all surgery details


@app.route('/addSurgery', methods=['GET', 'POST'])
def add_surgery_details():
    if request.method == 'POST':
        cur = myconn.cursor()
        hosp_ID = session["hosp_ID"]
        cur.execute("INSERT INTO SurgeryDetails(hosp_ID,heart,joint,abdominal) VALUES(%s,%s,%s,%s)",
                    (int(hosp_ID), int(0), int(0), int(0)))
        myconn.commit()
        cur.close()
    return redirect('/updateSurgery')


@app.route('/updateBeds', methods=['GET', 'POST'])
def update_beds():
    if request.method == 'POST':
        nbeds = request.form['bed']
        hosp_ID = session["hosp_ID"]
        cur = myconn.cursor()
        cur.execute('UPDATE BedsDetails SET BedsQuantity=%s WHERE hosp_id=%s', (nbeds, hosp_ID))
        myconn.commit()
        cur.close()

    hosp_ID = session["hosp_ID"]
    sql_query = "SELECT * FROM BedsDetails WHERE hosp_ID ='%s'" % (int(hosp_ID))
    cur = myconn.cursor()
    cur.execute(sql_query)
    hospBedsDetails = cur.fetchall()
    return render_template('update_beds.html', hospBedsDetails=hospBedsDetails,hospName=session["hospName"])  # Pass all bed details

@app.route('/addBeds', methods=['GET', 'POST'])
def add_bed_details():
    if request.method == 'POST':
        cur = myconn.cursor()
        hosp_ID = session["hosp_ID"]
        cur.execute("INSERT INTO BedsDetails(hosp_ID,BedsQuantity) VALUES(%s,%s)",(int(hosp_ID), int(0)))
        myconn.commit()
        cur.close()
    return redirect('/updateBeds')

#  cur.execute(
#                 'UPDATE blood SET AP_Quantity=%s, AN_Quantity=%s, BP_Quantity=%s, BN_Quantity=%s, OP_Quantity=%s, ON_Quantity=%s, ABP_Quantity=%s, ABN_Quantity=%s WHERE hosp_id=%s',
#                 (ap, an, bp, bn, op, on, abp, abn, hid))
#             myconn.commit()

@app.route('/updateBlood', methods=['GET', 'POST'])
def update_blood():
    if request.method == 'POST':
        hosp_ID = session["hosp_ID"]
        x = 0
        try:
            cur = myconn.cursor()
            ap = request.form['ap']
            cur.execute('UPDATE BloodDetails SET AP_Quantity=%s WHERE hosp_id=%s',(ap,hosp_ID))
            myconn.commit()
            cur.close()
        except Exception as e:
            print(e)
            x = 1
        try:
            cur = myconn.cursor()
            an = request.form['an']
            cur.execute('UPDATE BloodDetails SET AN_Quantity=%s WHERE hosp_id=%s',(an,hosp_ID))
            myconn.commit()
            cur.close()
        except Exception as e:
            print(e)
            x = 1
        try:
            cur = myconn.cursor()
            bp = request.form['bp']
            cur.execute('UPDATE BloodDetails SET BP_Quantity=%s WHERE hosp_id=%s',(bp,hosp_ID))
            myconn.commit()
            cur.close()
        except Exception as e:
            print(e)
            x = 1
        try:
            cur = myconn.cursor()
            bn = request.form['bn']
            cur.execute('UPDATE BloodDetails SET BN_Quantity=%s WHERE hosp_id=%s',(bn,hosp_ID))
            myconn.commit()
            cur.close()
        except Exception as e:
            print(e)
            x = 1
        try:    
            cur = myconn.cursor()
            abp = request.form['abp']
            cur.execute('UPDATE BloodDetails SET ABP_Quantity=%s WHERE hosp_id=%s',(abp,hosp_ID))
            myconn.commit()
            cur.close()
        except Exception as e:
            print(e)
            x = 1
        try:
            cur = myconn.cursor()
            abn = request.form['abn']
            cur.execute('UPDATE BloodDetails SET ABN_Quantity=%s WHERE hosp_id=%s',(abn,hosp_ID))
            myconn.commit()
            cur.close()
        except Exception as e:
            print(e)
            x = 1
        try:
            cur = myconn.cursor()
            op = request.form['op']
            cur.execute('UPDATE BloodDetails SET OP_Quantity=%s WHERE hosp_id=%s',(op,hosp_ID))
            myconn.commit()
            cur.close()
        except Exception as e:
            print(e)
            x = 1
        try:
            cur = myconn.cursor()
            on = request.form['on']
            cur.execute('UPDATE BloodDetails SET ON_Quantity=%s WHERE hosp_id=%s',(on,hosp_ID))
            myconn.commit()
            cur.close()
        except Exception as e:
            print(e)
            x = 1
        cur.close()

    hosp_ID = session["hosp_ID"]
    sql_query = "SELECT * FROM BloodDetails WHERE hosp_ID ='%s'" % (int(hosp_ID))
    cur = myconn.cursor()
    cur.execute(sql_query)
    hospBloodDetails = cur.fetchall()
    return render_template('update_blood.html', hospBloodDetails=hospBloodDetails,hospName=session["hospName"])  # Pass all bed details

@app.route('/addBlood', methods=['GET', 'POST'])
def add_blood_details():
    if request.method == 'POST':
        cur = myconn.cursor()
        hosp_ID = session["hosp_ID"]
        cur.execute('INSERT INTO  BloodDetails(hosp_id,AP_Quantity,AN_Quantity,BP_Quantity,BN_Quantity,OP_Quantity,ON_Quantity,ABP_Quantity,ABN_Quantity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (int(hosp_ID), int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0)))
        myconn.commit()
        cur.close()
        return redirect('/updateBlood')




@app.route('/updateAmbulance', methods=['GET', 'POST'])
def update_ambulance():
    if request.method == 'POST':
        try:
            namb = request.form['amb']
            cur = myconn.cursor()
            hosp_ID = session["hosp_ID"]
            cur = myconn.cursor()
            cur.execute('UPDATE AmbulanceDetails SET AmbulanceQuantity=%s WHERE hosp_id=%s', (namb, hosp_ID))
            myconn.commit()
            cur.close()
        except:
            print("Ambulance Error")

    hosp_ID = session["hosp_ID"]
    sql_query = "SELECT * FROM AmbulanceDetails WHERE hosp_ID ='%s'" % (int(hosp_ID))
    cur = myconn.cursor()
    cur.execute(sql_query)
    hospAmbulanceDetails = cur.fetchall()
    if(len(hospAmbulanceDetails)) == 0 :
        return redirect('/addAmbulance')
    return render_template('update_ambulance.html', hospAmbulanceDetails=hospAmbulanceDetails,hospName=session["hospName"])  # Pass all bed details

@app.route('/addAmbulance', methods=['GET', 'POST'])
def add_ambulance():
    hosp_ID = session["hosp_ID"]
    cur = myconn.cursor()
    cur.execute('INSERT INTO AmbulanceDetails(hosp_id,AmbulanceQuantity) VALUES(%s,%s)', (hosp_ID, int(0)))
    myconn.commit()
    cur.close()
    return redirect('/updateAmbulance')

@app.route('/doctor_reg', methods=['GET', 'POST'])
def doctor_reg():
    if request.method == 'POST':
        # print('hello')
        doc_id = request.form['docUserName']
        hosp_id = request.form['hosp_id']
        docSpeciality = request.form['docSpeciality']
        docName = request.form.get('docName')
        docEmail = request.form['docEmail']
        docPhone = request.form['docPhone']
        docAddress = request.form['docAddress']
        docPassword = request.form['docPassword']
        cur = myconn.cursor()
        cur.execute('SELECT * FROM doctor WHERE doc_id=%s', (doc_id,))

        account = cur.fetchone()
        if account:
            return "doc_id exists already"
        else:
            cur.execute('INSERT INTO doctor VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
                        (doc_id, hosp_id, docSpeciality, docName, docEmail, docPhone, docAddress, docPassword,))
            myconn.commit()
            return render_template('doctor_login.html')
    return render_template('doctor_reg.html')


@app.route('/doctor_login', methods=['GET', "POST"])
def doctor_login():
    if request.method == 'POST':
        doc_id = request.form['docUserName']
        docPassword = request.form['docPassword']
        cur = myconn.cursor()
        cur.execute('SELECT * FROM doctor WHERE doc_id=%s AND docPassword=%s', (doc_id, docPassword,))
        account = cur.fetchone()
        myconn.commit()
        if account:
            session['doc_id'] = doc_id
            return render_template('doctor_after_login.html')
        else:
            return "wrong id and password"
    return render_template('doctor_login.html')

@app.route('/update_doc_info', methods = ['GET', 'POST'])
def update_doc_info():
    if request.method == 'POST':
        # print(session['docEmail'])
        docName = request.form.get('docName')
        docSpeciality = request.form['docSpeciality']
        hosp_id = request.form['hosp_id']
        docPhone = request.form['docPhone']
        docAddress = request.form['docAddress']
        cursor = myconn.cursor()
        cursor.execute('UPDATE doctor SET docAddress=%s, docPhone=%s, hosp_id=%s, docSpeciality=%s, docName=%s WHERE doc_id=%s', (docAddress, docPhone, hosp_id,docSpeciality,docName ,session['doc_id'],))
        myconn.commit()
        return render_template('doctor_after_login.html')

    return render_template('doctor_after_login.html')

@app.route('/user')
def home():
    return render_template('user_home.html')

@app.route('/user_login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        passwd = request.form['passwd']
        cur = myconn.cursor()
        cur.execute('SELECT * FROM user WHERE UserId=%s AND UserPassword=%s', (userid, passwd))
        acc = cur.fetchone()
        if acc:
            session['loggedin'] = True
            session['UserId'] = userid
            session['Name'] = acc[1]
            session['Address'] = acc[3]
            session['Phone'] = acc[4]
            session['DOB'] = acc[5]
            return render_template('user_index.html')
        else:
            return 'User not found!!'

@app.route('/user_register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form['userid']
        name = request.form['name']
        passwd = request.form['passwd']
        cpasswd = request.form['cpasswd']
        cur = myconn.cursor()
        cur.execute('INSERT INTO user (UserId, UserName, UserPassword) VALUES (%s, %s, %s)', (userid, name, passwd))
        myconn.commit()
        cur.close()
        session['loggedin'] = True
        session['UserId'] = userid
        session['Name'] = name
        session['Address'] = ''
        session['Phone'] = ''
        session['DOB'] = ''
        return render_template('user_index.html')

    return render_template('register.html')

@app.route('/user_update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        add = request.form['add']
        phno = request.form['phno']
        dob = request.form['dob']
        session['Address'] = add
        session['Phone'] = phno
        session['DOB'] = dob
        cur = myconn.cursor()
        cur.execute('UPDATE user SET UserAddress=%s, UserPhone=%s, UserDOB=%s WHERE UserId=%s', (add, phno, dob, session['UserId']))
        myconn.commit()
        cur.close()

        return render_template('user_index.html')

@app.route('/user_logout')
def logout():
    session.pop('loggedin', None)
    session.pop('UserId', None)
    session.pop('Name', None)
    session.pop('Address', None)
    session.pop('Phone', None)
    session.pop('DOB', None)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

