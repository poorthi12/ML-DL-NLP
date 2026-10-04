from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Hi This Is your First HTML Page Using Flask</h1></html>"
@app.route("/index")
def another_page():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        ame = request.form['name']
        mail = request.form['email']
        return f"hello {ame} and this is your g mail{mail}"
    return render_template("form.html")
##variable rule 
@app.route("/v-rule/<int:score>")
def variable(score):
    return "THIS IS YOUR SCORE: " + str(score)
##dynamic
@app.route("/new/<int:marks>")
def marks(marks):
    result = ""
    if marks >= 50:
        result="PASSED"
    else:
        result="FAILED  "
    return render_template("marks_sheet.html",result=result)
@app.route('/marks/<int:value>')
##expression -- for condition
def mark(value):
    result=''
    if value > 50:
        result = "PASSED"
    else:
        result="FAILED"
    exep = {'value':value,'result':result}
    return render_template('expression.html',result=exep)
## if condition
@app.route('/if/<int:result>')
def ifstate(result):     
    return render_template("ifstate.html",result=result)
##redirecting and                   
@app.route("/redir",methods=['GET','POST'])
def redir():
    value=5
    return redirect(url_for('ifstate',result=value))

if __name__=="__main__":
    app.run(debug=True)         