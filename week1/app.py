from flask import Flask,render_template,request
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('myForm.html')
@app.route('/submit',methods=['POST'])
def submit():
    uname=request.form['username']
    dob=request.form['dob']
    return render_template('greetings.html',name=uname,dob=dob)

app.run(debug=True)