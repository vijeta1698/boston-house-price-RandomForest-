from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
    return render_template('home.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    CRIM = request.form['CRIM']
    NOX= request.form['NOX']
    RM = request.form['RM']
    DIS= request.form['DIS']
    LSTAT = request.form['LSTAT']

    model = pickle.load(open('rf.pkl','rb'))
    price = model.predict([[CRIM,NOX,RM,DIS,LSTAT]])

    return render_template('home.html',price=round(price[0],2))


if __name__ =='__main__':
    app.run()