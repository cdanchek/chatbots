import aiml
import os
import json
import requests

def get_weather(args):
	#print args
	#print str(args)

	#inp=json.loads(args)
	#zip=inp['PLACE']
	zip=args["PLACE"]
	if len(str(zip))<>5 :
		return "You sure this place is on planet Earth?" 
	#print zip
	url="http://api.openweathermap.org/data/2.5/weather?zip="+zip+",us&APPID=<key>&units=imperial"

	response=requests.post(url)

	resp=json.loads(response.text)

	#print resp
	ux=str(resp["weather"][0]["description"])+ " at "+ str(resp["name"])
	ux=ux+","+ "Current temperature is "+str(resp["main"]["temp"])+ " Farenheit"
	ux=ux+","+ "Pressure "+str(resp["main"]["pressure"])+" hpa"
	ux=ux+","+ "Humidity "+str(resp["main"]["humidity"])+"%"
	ux=ux+","+ "Temperature from "+ str(resp["main"]["temp_min"])+ " to "+ str(resp["main"]["temp_max"])+ " Farenheit"
	return ux



# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")


#if os.path.isfile("bot_brain.brn"):
#    kernel.bootstrap(brainFile = "bot_brain.brn")
#else:
#    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
#    #kernel.saveBrain("bot_brain.brn")

# Press CTRL-C to break this loop
while True:
    message = raw_input("Enter your message to the bot: ")
    #message ="WHAT IS WEATHER IN 94582" 
	
    if message == "q:":
        exit()
#    elif message == "save":
#        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
	#print bot_response
        # Do something with bot_response
	if bot_response.find("WEB_SERVICE")!=-1:
		#print "Found Web service!"
		#print bot_response
		resp=json.loads(bot_response)
		#print resp["WEB_SERVICE"]
		ws=resp["WEB_SERVICE"]
		args=resp["ARGS"]
		if ws=="WEATHER":
			ux=get_weather(args)
		print ux
	else:		
		print bot_response
