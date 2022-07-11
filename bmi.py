#! /usr/bin/python

def BodyMassIndex():
  weight = input() #What is your weight?
  weight = float(weight)
  height = input() #What is your height?
  height = float(height)
  
  sqrheight = height**2
  bmi = weight /sqrheight

  if bmi < 18.5:
    print("Underweight")
  elif bmi >= 18.5 and bmi < 25:
    print("Normal")
  elif bmi >= 25 and bmi < 30:
    print("Overweight")
  else:
    print("Obesity")
    
  return

BodyMassIndex ()
