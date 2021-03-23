from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

filename = 'modelwith5classifiers.pkl'
pipe = joblib.load(filename)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    arr = []
    
    if request.method == 'POST':
        Age = int(request.form['Age'])
        
        Distance_From_Home = int(request.form['DistanceFromHome'])

        Department = request.form['Department']

        Environment_Satisfaction = int(request.form['EnvironmentSatisfaction'])  

        Job_Involvement = int(request.form['JobInvolvement'])

        Job_Level = int(request.form['JobLevel'])

        Job_Satisfaction = int(request.form['JobSatisfaction'])

        Job_Role = request.form['JobRole']

        Marital_Status = request.form['MaritalStatus']

        Overtime = request.form['OverTime']
        
        Years_At_Company = int(request.form['YearsAtCompany'])
 
        Total_Working_Years = int(request.form['TotalWorkingYears'])

        Stock_options = int(request.form['StockOptionLevel'])

        Work_Life_Balance = int(request.form['WorkLifeBalance'])

        Years_in_Current_Role = int(request.form['YearsInCurrentRole'])

        Years_with_Current_Manager = int(request.form['YearsWithCurrManager'])

        Monthly_Income = int(request.form['MonthlyIncome']) // 75.20

        
        if (Department == "Sales"):
            Department = 2
        elif (Department == "Research & Development"):
            Department = 1
        else:
            Department = 0

            
        if (Job_Role == "Manufacturing Director"):
             Job_Role = 4
        elif (Job_Role == "Laboratory Technician"):
            Job_Role = 2
        elif (Job_Role == "Research Scientist Manager"):
            Job_Role = 6
        elif (Job_Role == "Sales Representative"):
            Job_Role = 8
        elif (Job_Role == "Human Resources"):
            Job_Role = 1
        elif (Job_Role == "Research Director"):
            Job_Role = 5
        elif (Job_Role == "Healthcare Representative"):
            Job_Role = 0
        elif (Job_Role == "Sales Executive"):
            Job_Role = 7
        else:
           Job_Role = 3

           
        if (Marital_Status == "Single"):
            Marital_Status = 2
        elif (Marital_Status == "Married"):
            Marital_Status = 1
        else:
            Marital_Status = 0

            
        if (Overtime == "Yes"):
            Overtime = 1
        else:
            Overtime = 0
        """

        if(Job_Role =="Laboratory Technician" or Job_Role=="Sales Representative"):
            Job_Level=1
        elif(Job_Role =="Human Resources" or Job_Role=="Healthcare Representative"):
            Job_Level=2
        elif(Job_Role =="Manufacturing Director" or Job_Role=="Sales Executive"):
            Job_Level=3
        else:
            Job_Level=4

        if(Job_Role =="Laboratory Technician" or Job_Role=="Sales Representative" or Job_Role =="Human Resources"):
            Job_Involvement=1
        elif(Job_Role=="Healthcare Representative" or Job_Role =="Manufacturing Director" or Job_Role=="Sales Executive"):
            Job_Involvement=2
        else:
            Job_Involvement=3

        """ 
        arr = [[Age, Department, Distance_From_Home, Environment_Satisfaction, Job_Involvement, Job_Level, Job_Role, Job_Satisfaction,
                Marital_Status, Monthly_Income, Overtime, Stock_options, Total_Working_Years, Work_Life_Balance, Years_At_Company,  Years_in_Current_Role,
                Years_with_Current_Manager ]]
        
        X_test = pd.DataFrame(arr,columns=['Age', 'Department','Distance From Home', 'Environment Satisfaction', 'Job Involvement', 'Job Level', 'Job Role', 'Job Satisfaction',
                                           'Marital Status', 'Monthly Income', 'Overtime', 'Stock options', 'Total Working Years', 'Work Life Balance','Years At Company', 
                                           'Years in Current Role', 'Years with Current Manager'])
        pred = pipe.predict(X_test)
        
        
        if pred == 1:
            print("%d", pred)
            pred_text = "It's time to look for new opportunities. According to past data, your job offer is likely to be revoked."
        if pred == 0:
            print("%d", pred)
            pred_text = "Your Job is secure. Good luck for future endeavours!"
        
    return render_template('results.html',pred_text=pred_text)

if __name__ == '__main__':
    app.run()
