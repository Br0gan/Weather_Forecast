#!/usr/bin/python

import argparse, datetime, json, urllib.request, sys


def pullInfo(cityId):
	print(cityId)
	data = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?id=%s' % cityId).read()
	jdata = json.loads(data.decode('utf8'))
	return(jdata)

class conversions: 
	def convertToFh(self,temp):
		self.fTemp = (temp - 273.15) * 1.8000 + 32
		self.fTemp = round(self.fTemp,2)
		return(self.fTemp)
	
	def convertToCel(self,temp):
		self.cTemp = temp - 273.15
		self.cTemp = round(self.cTemp,2)
		return(self.cTemp)
	
	def convertUnixTime(self,utime):
 	    self.strTime = datetime.datetime.fromtimestamp(int(utime)).strftime('%m-%d-%Y')
 	    return(self.strTime)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Weather forecast -default temp is in Fs add option -C for Cel')
	
	parser.add_argument('CityID',
			     metavar='numbers',
			     nargs='*',
			     type=str, 
			     help="Enter you city ID")

	parser.add_argument('-C',
			    '--Cel', 
			    dest='celCheck',
			    action='store_true',
			    default=False,
			    help='Changes temp to celcius')

	args = parser.parse_args()
	cityID = args.CityID[0]
	celcheck = args.celCheck

	rawData = pullInfo(cityID)
	city = rawData['city']['name']
	conv = conversions()
	
	while True:
		print(city)
		for info in rawData['list']:
			
			if celcheck == False:
				convTempHigh = conv.convertToFh(info['temp']['max'])
				convTempLow	= conv.convertToFh(info['temp']['min'])
			else:
				convTempHigh = conv.convertToCel(info['temp']['max'])
				convTempLow = conv.convertToCel(info['temp']['min'])
		
			convDate = conv.convertUnixTime(info['dt'])
			weather = info['weather'][0]['description']

			print(convDate, ' || High - ', convTempHigh, '- Low - ', convTempLow,  '|| Weather: ', weather, '\n')
			
