import pickle 
from flask import Flask, request, Response 
import pandas as pd
from health_insurance.HealthInsurance import HealthInsurance

#loading the model 
path = ''
# path = '/home/daniel/repos/pa04_health_insurance_cross_sell/health_insurance_app/model/'
model = pickle.load(open(path + '/health_insurance_app/model/healthinsurance.pkl', 'rb'))

app = Flask ( __name__ )

@app.route ('/predict', methods = ['POST'])
def health_insurance_cross_sell ():
    test_json = request.get_json ()
    
    if test_json:
        if isinstance (test_json, dict):
            data_raw = pd.DataFrame (test_json, index=[0])
            
        else: 
            data_raw = pd.DataFrame (test_json, columns = test_json[0].keys())
            
        # Instantiate HealthInsurance
        pipeline = HealthInsurance()

        df1 = pipeline.data_cleaning (data_raw)

        df2 = pipeline.feature_engineering (df1)

        df3 = pipeline.data_preparation (df2)

        df_response = pipeline.prediction_proba (model, df3, data_raw)

        return df_response

    else:
        Response ('{}', status = 200, mimetype='application/json')
        
        
if __name__ == "__main__":
    app.run ('0.0.0.0')#,debug=True)

