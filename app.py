from flask import *
import pymongo as p
from pymongo.errors import OperationFailure, DuplicateKeyError

app = Flask(__name__)

url = 'mongodb+srv://favasmonu555:9961133007@flaskcluster.hejambc.mongodb.net/?retryWrites=true&w=majority'
cluster = p.MongoClient(url,connect=False)
db = cluster['database']
tbl = db['user']

@app.route('/')
def home():
    return render_template('home.html',a = ['',''])

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/loginn', methods=['POST'])
def loginn():
    usr = request.form['usr']
    pas = request.form['pas']
 
    data = tbl.find()
    for x in data:
        if(x['_id']==usr) and (x['password']==pas):
            return render_template('welcome.html',s = [usr,pas])
            break
    else:
        flash('Username or password is incorrect')
        flash('red')
        return redirect('/')

@app.route('/signupp', methods=['POST','GET'])
def signupp():
    usr = request.form['usr']
    pas = request.form['pas']
     
    try:
        tbl.insert_one({'_id': usr, 'password': pas}) 
    except DuplicateKeyError:
        flash('username already exist!')
        return redirect(request.referrer)
    except:
        flash('Something went wrong! try again')
        return redirect(request.referrer)

    flash('signup succesfull')
    flash('green')
    return render_template('home.html', a = [usr,pas])
    #return redirect( url_for('home'))



if __name__ == '__main__':
    app.secret_key = "something"
    app.run(debug=True)