import pickle
import pandas as pd 


class HealthInsurance: 
    
    def __init__(self):
        
        # project home_path
        self.home_path = ''
        # self.home_path = '/home/daniel/repos/pa04_health_insurance_cross_sell/'
        
        # load scalers and encoders from pickle
        self.annual_premium_scaler = pickle.load (open (self.home_path + 'features/annual_premium_scaler.pkl','rb'))
#         self.annual_premium_scaler = pickle.load (open (self.home_path + 'health_insurance_app/features/annual_premium_scaler.pkl','rb'))
        
        self.age_scaler =  pickle.load (open (self.home_path + 'features/age_scaler.pkl','rb'))
#         self.age_scaler =  pickle.load (open (self.home_path + 'health_insurance_app/features/age_scaler.pkl','rb'))
        
        self.vintage_scaler = pickle.load (open (self.home_path + 'features/vintage_scaler.pkl','rb'))
#         self.vintage_scaler = pickle.load (open (self.home_path + 'health_insurance_app/features/vintage_scaler.pkl','rb'))
        
        self.region_code_scaler = pickle.load (open (self.home_path + 'features/region_code_scaler.pkl','rb'))
#         self.region_code_scaler = pickle.load (open (self.home_path + 'health_insurance_app/features/region_code_scaler.pkl','rb'))
        
        self.policy_sales_channel_scaler = pickle.load (open (self.home_path + 'features/policy_sales_channel_scaler.pkl','rb'))
        
        self.vehicle_age_scaler = pickle.load (open (self.home_path + 'features/vehicle_age_scaler.pkl','rb'))
        
        
        
    def data_cleaning ( self, data ): 
        
        # change dtypes
        data['region_code'] = data['region_code'].astype('int64')
        data['policy_sales_channel'] = data['policy_sales_channel'].astype('int64')    

        return data

    
    
    def feature_engineering (self,  data ):
    
        data['vehicle_damage'] = data['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        
        return data

    
    
    def data_preparation ( self, data): 
        
        # Standard Scaler
        data['annual_premium'] = self.annual_premium_scaler.transform(data[['annual_premium']].values)
        
        
        # MinMaxScaler
        # 'age'
        data[['age']] = self.age_scaler.transform (data[['age']].values)

        # 'vintage'
        data[['vintage']] = self.vintage_scaler.transform (data[['vintage']].values)
        
        
        # One Hot Encoder
        # 'gender'
        data = pd.get_dummies(data=data, columns = ['gender'], prefix='gender')

        # Target Encoder 
        # 'region_code'
        data.loc[:,'region_code'] = data['region_code'].map(self.region_code_scaler)

        # 'policy_sales_channel'
        data.loc[:,'policy_sales_channel'] = data['policy_sales_channel'].map(self.policy_sales_channel_scaler)

        # 'vehicle_age'
        data.loc[:,'vehicle_age'] = data['vehicle_age'].map(self.vehicle_age_scaler)


        # Feature Selection
        cols_selected = ['vintage',   
                         'annual_premium',
                         'age',   
                         'policy_sales_channel',   
                         'region_code',    
                         'vehicle_damage',
                         'previously_insured',   
                        ]
        
        return data[cols_selected]
        
        
        
    def prediction_proba ( self, model, data, data_raw):        

        # Predict Proba
        score = model.predict_proba (data)

        # add predictions to data_raw
        data_raw['score'] = score[:,1].tolist()
        
        return data_raw.to_json (orient = 'records')

       
