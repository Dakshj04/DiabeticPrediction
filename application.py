from flask import Flask, render_template, request,Response
import pickle

application = Flask(__name__)
app=application
# Load the model
model = pickle.load(open('models/modelForPrediction.pkl', 'rb'))    
scaler=pickle.load(open('models/standardScaler.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

#route for single datapoint prediction
@app.route('/predictdata', methods=['GET','POST'])
def predictdata():
  if request.method=='POST':
        result=""

        features = [float(x) for x in request.form.values()]
        new_data=scaler.transform([features])
        prediction = model.predict(new_data)
        output = prediction[0]
        if output==1:
            result= 'Diabetic'
        else :
            result= 'Non-Diabetic' 

        return render_template('single_prediction.html', result=result)
  else:
     return render_template('index.html')
   

if __name__ == "__main__":
    app.run(host='0.0.0.0') 