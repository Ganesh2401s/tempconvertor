#Temperature convertor for Celsius, Kelvin and Fahrenheit 

temp = float(input("Enter the temperature: "))
unit = input("Enter the valid temperature unit like C K F : ")

# Degre celsius conversions to others.
if unit == "C": 
    kelvin = temp + 273.15 
    fahrenheit = 9/5 * temp + 32
    conversion_temp_unit = input("Enter the temp unit in which you want to convert (K or F): ")
    if conversion_temp_unit == "K":
        print(f"Converted the temp to Kelvin from Celsius : {kelvin} K")
    if conversion_temp_unit == "F":
        print(f"Converted the temp to Fahrenheit from Celsius :{fahrenheit} °F")
 
    
       
#Kelvin conversion to other units
elif unit == "K":
    celsius = temp - 273.15
    fahrenheit = (temp - 273.15)* 9/5 + 32 
    conversion_temp_unit = input("Enter the temp unit in which you want to convert (C or F): ")
    if conversion_temp_unit == "C":
        print(f"Converted the temp. to celsius from Kelvin : {celsius} °C")
    elif conversion_temp_unit == "F":
        print(f"Converted the temp. to fahrenheit from Kelvin : {fahrenheit} °F")
# elif:
#     print(f"{temp} is not a valid temperature unit.") 
    
           
#Fahrenheit conversion to others 
elif unit == "F":
    celsius = (temp - 32)* 5/9
    kelvin = (temp - 32) *5/9 + 273.15 
    conversion_temp_unit = input("Enter the temp unit in which you want to convert (C or K): ")
    if conversion_temp_unit == "C":
        print(f"Converted the temp to celsius from fahrenheit: {celsius} °C")
    elif conversion_temp_unit == "K":
        print(f"Converted the temp to Kelvin from fahrenheit: {kelvin} K")    
# elif:
#     print(f"{temp} is not a valid temperature unit.")    
    
else:
    print(f"{unit} is not a valid temperature unit.")         
        