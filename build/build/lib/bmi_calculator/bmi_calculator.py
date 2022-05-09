import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Calculate BMI from provided weight and height
def bmi(weight,height_cm):
    try:
        return weight/((height_cm/100)**2)
    except:
        return 'Undefined'

# Categorise bmi data into bmiCategory and healthRisk
def bmiCategory(bmi):
    try:
        if bmi <= 18.4:
            bmiCategory = 'Underweight'
            healthRisk = 'Malnutrition risk'
        elif bmi > 18.4 and bmi < 25:
            bmiCategory = 'Normal weight'
            healthRisk = 'Low risk'
        elif bmi >= 25 and bmi < 30:
            bmiCategory = 'Overweight'
            healthRisk = 'Enhanced risk'
        elif bmi >= 30 and bmi < 35:
            bmiCategory = 'Moderately obese'
            healthRisk = 'Medium risk'
        elif bmi >= 35 and bmi < 40:
            bmiCategory = 'Severely obese'
            healthRisk = 'High risk'
        else:
            bmiCategory = 'Very severely obese'
            healthRisk = 'Very high risk'
    except:
        bmiCategory = 'Undefined'
        healthRisk = 'Undefined'
    
    return bmiCategory, healthRisk

def run():
    # Open file dialog to allow user to choose data file
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
   
    # for testing, comment above lines and uncomment the following: 
    # filename = 'data.json'
    
    # Open file and load into pandas dataframe
    json_file = open(filename)
    json_data = json.load(json_file)
    data =pd.DataFrame(json_data)
    
    # Create 3 new columns in dataframe: bmi, bmiCategory, healthRisk, and output in json format
    data['bmi']=data.apply(lambda x: bmi(x['WeightKg'], x['HeightCm']), axis=1)
    data['bmiCategory'], data['healthRisk'] = zip(*data['bmi'].apply(bmiCategory))
    data.to_json("bmi_data_output.json", orient='records')
    
    # Count and output number of overweight people in dataset
    # Observation: No unique identifier in dataset - could have duplicates
    count = data.groupby('bmiCategory')['Gender'].count()['Overweight'];
    print('Count of overweight people: ' , count)
    

if __name__ == "__main__":
    run()
