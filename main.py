from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from search_csv import record_search


app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)





@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
      num = request.form['key']
      search_data = record_search(num)
      assignee = search_data['assignee']
      reporter = search_data['reporter']
      account_id = search_data['account_id']
      summary = search_data['summary']
      flash('Record Found')
    else:
        search_data = record_search(num='4000')
        assignee = search_data['assignee']
        reporter = search_data['reporter']
        account_id = search_data['account_id']
        summary = search_data['summary']
        
    return render_template('index.html', assignee=assignee, reporter=reporter, account_id=account_id, summary=summary)





@app.route('/user')
def user():
    if 'user' in session:
        user = session["user"]
        return render_template('user.html', user=user)
    else:
        flash('You are not logged in')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    flash(f'You have been logged out', "info")
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         session.permanent = True
#         user = request.form['nm']
#         session["user"] = user
#         flash('Login Successful')
#         return redirect(url_for('user'))
#     else:
#         if "user" in session:
#             flash("Already Logged In")
#             return redirect(url_for("user"))
#         return render_template('login.html')