import json
import csv 

data=json.load(open('/home/deadman/pythonprojects/allprojects-main/code202016/data.json','r')) #json data location to load json data

ls=[] #empty list to store the overwieght data
new_dict={}  #empty dictionary to store calculated data

#iterate through the loaded json data and calculate the BMI 
for person in data['User Details']:
    bmi=(person['WeightKg'])/((person["HeightCm"]/100)**2)

#condition to check bmi and other factors
    if bmi <= 18.4:
        new_dict['BMI']=bmi
        new_dict['Gender']=person["Gender"]
        new_dict['BMI Category']="Underweight"
        new_dict['Health risk']="Malnutrition risk"   
    
    elif bmi > 18.5 and bmi < 24.9:
        new_dict['BMI']=bmi
        new_dict['Gender']=person["Gender"]
        new_dict['BMI Category']="Normal weight"
        new_dict['Health risk']="Low risk"        
    
    elif bmi > 25 and bmi < 29.9:
        new_dict['BMI']=bmi
        new_dict['Gender']=person["Gender"]
        new_dict['BMI Category']="OverWeight"
        new_dict['Health risk']="Enhanced risk"    
    
    elif bmi > 30 and bmi < 34.9:
        new_dict['BMI']=bmi
        new_dict['Gender']=person["Gender"]
        new_dict['BMI Category']="Moderately Obese"
        new_dict['Health risk']="Medium risk"    
    
    elif bmi > 35 and bmi < 39.9:
        new_dict['BMI']=bmi
        new_dict['Gender']=person["Gender"]
        new_dict['BMI Category']="Severly Obese"
        new_dict['Health risk']="High risk"
    
    elif bmi > 40:
        new_dict['BMI']=bmi
        new_dict['Gender']=person["Gender"]
        new_dict['BMI Category']="Very Severly Obese"
        new_dict['Health risk']="Very high risk"

    #convert dictionary to json.
    json_object = json.dumps(new_dict,indent=2)      
    print(json_object)

#iterarate to find out the overweights in the json data

for person in data['User Details']:
    bmi=(person['WeightKg'])/(person["HeightCm"]/100)
    if (bmi > 25.0) and (bmi < 29.9):
        ls.append(bmi)
print("Number of People Overwaight = ",len(ls))


