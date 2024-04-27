#Assignment - Using the URL below
# https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
# Write a python program called currentweather.py that will print out the current temperature on the console 

# import required modules
import requests 
import json
 
# base_url variable to store url
url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
 
# get method of requests module
# return response object
response = requests.get(url)
#print (response.json())
# json method of response object 
# convert json format data into
# python format data
data = response.json()
#print(data)
current =  data ["current"]
#print (currenttemp)
currenttemp = current ['temperature_2m']
print (currenttemp)