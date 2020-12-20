from flask import Flask
from credit_card_generator.sql_conn_and_functions import get_sql_connection, admin_login, password_update, \
    admin_profile_update_block, new_cc_request, cards_status_details, pending_details, \
    generate_card, display_card
from flask import flash, request, redirect, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret key"
con = get_sql_connection()


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/Request_cc')
def Request_cc():
    return render_template('request_cc.html')


@app.route('/request_cc_service', methods=['GET', 'POST'])
def request_cc_service():
    details = request.form.to_dict()
    id = new_cc_request(details)
    if id != False:

        flash("Request submitted Successfully here it your ID :" + (id))
        return redirect('/home')
    else:
        flash("A Credit Card issued previously for this number")
        return redirect('/home')


@app.route('/admin_profile', methods=['GET', 'POST'])
def admin_profile():
    if request.method == 'POST':
        username = request.form.get('email')
        pwd = request.form.get('password')
        flag = admin_login(username, pwd)

        if flag != False:
            session['email'] = flag[2]
            session['id'] = flag[0]
            return render_template("admin_profile.html", admin_details=flag)
        else:
            flash("Enter Valid logins")
            return redirect('/login')
    else:
        try:
            flag = admin_login(session['email'])
            return render_template("admin_profile.html", admin_details=flag)
        except:
            flash("Please login First")
            return redirect('/login')


@app.route('/admin_profile_update', methods=['GET', 'POST'])
def admin_profile_update():
    user_id = request.form.get("user_id")
    adminname = request.form.get("adminname")
    inputEmail = request.form.get("inputEmail")
    Phonenumber = request.form.get("Phonenumber")

    admin_profile_update_block(user_id, adminname, inputEmail, Phonenumber)

    return redirect('/admin_profile')


@app.route('/admin_password_change')
def admin_password_change():
    try:
        if session['email']:
            return render_template('/password_change.html')
    except:
        flash("Please login")
        return redirect('/login')


@app.route('/update_user_password', methods=['GET', 'POST'])
def update_user_password():
    password = request.form.get("cnfpassword")
    password_update(password, session['id'])

    return redirect('/admin_profile')


@app.route('/dashboard')
def dashboard():
    try:
        if session['email']:
            card = cards_status_details()
            return render_template('/dashboard.html', stats=card)
    except:
        flash("Please login")
        return redirect('/login')


@app.route('/view_pending_stats')
def view_pending_stats():
    try:
        if session['email']:
            pending = pending_details()
            return render_template('/view_pending_requests.html', rows=pending)
    except:
        flash("Please login")
        return redirect('/login')


@app.route('/status_update', methods=['GET', 'POST'])
def status_update():
    status = request.form.to_dict()
    generate_card(status)
    return redirect('/view_pending_stats')


@app.route('/search_card', methods=['GET', 'POST'])
def search_card():
    number = request.form.get('searchcontent')
    card = display_card(number)
    if card != False:
        return render_template('/view_card.html', flag=True, card=card)
    else:
        card = "Request Rejected Contact Customer Service"
        return render_template('/view_card.html', flag=False, card=card)


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)

    return redirect('/')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
