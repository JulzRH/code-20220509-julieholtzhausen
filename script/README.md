To run main bmi program:
    `python bmi_calculator.py`
    
    * This opens a dialog that allows the user to select the json file they want to process
    * The script calculates the BMI and creates the 3 new columns requested, then creates a file called bmi_data_output.json
    * The count of overweight people is printed to the console
    
To run the unit tests:
    `python -m unittest test_bmi_calculator.py`
    

Further dev: 
* Better and more consistant error handling
* Add data provider to unit tests to handle all possible outputs
