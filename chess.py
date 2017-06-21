from flask import Flask, redirect, url_for
from flask import jsonify
from pymongo import MongoClient
import pprint
app = Flask(__name__)

client=MongoClient('mongo://localhost:2707/')

db=client.data


@app.route('/')
def layout():
   return render_template('layout.html')

@app.route('/rate',methods = ['POST', 'GET'])
def rate():
   if request.method == 'POST':
      user = request.form['nm']
      identity=request.form['id']
      return redirect(url_for('hello_guest',guest = user,no=identity)



#@app.route('/admin')
#def hello_admin():
 #  return 'Hello Admin'

@app.route('/guest/<guest>,<no>')
def hello_guest(guest,no):
    cal=db.detail.find({"name":guest,"idd":no},{_id:0,"name":1,"score":1}).count()
    print('Hello %s player' % guest)
    if(cal==0):
        db.detail.insert({"name":guest,"idd":no,"score":1})
    else:
        chess1=db.detail.find({"name":guest,"idd":no},{_id:0,"name":0,"score":1,"idd":0})
        chess2=db.detail.find({"name":guest,"idd":no},{_id:0,"name":1,"score":0,"idd":0})
        chess3=db.detail.find({"name":guest,"idd":no},{_id:0,"name":0,"score":0,"idd":1})
        return jsonify(sco=chess1,nam=chess2,idd=chess3)

#2nd method
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      chess=db.detail.find({"name":guest,"idd":no},{_id:0,"name":1,"score":1})
      return render_template("result.html",result = chess)

@app.route('/update',methods=['POST','GET'])
def update():
   if request.method=='POST':
      user=request.form['nm']
      identity=request.form['id']
      cal=db.detail.find({"name":guest,"idd":no},{_id:0,"name":1,"score":1}).count()
    if(cal==0):
        db.detail.insert({"name":guest,"idd":no,"score":1})
    else:
        db.detail.update({"name":guest,"idd":no},{$inc:{"score":1}})
         
        return redirect(url_for('hello_guest',guest = user,no=idntity))
        #s=db.detail.find({"name":guest,"idd":no},{_id:0,"name":1,"score":1})          #value of score
        

#@app.route('/user/<name>')
#def hello_user(name):
 #  if name =='admin':
  #    return redirect(url_for('hello_admin'))
   #else:
    #  return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)




@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

