import datetime
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
import iso8601
import pytz

def getZone(uni):
	zone  = {
	'University of California--Davis' : "America/Los_Angeles",
	 'Southwestern University': "America/Chicago",
	  'Rensselaer Polytechnic Institute' : "America/New_York", 
	  'Brown University' : "America/New_York", 
	  'New York University' : "America/New_York", 
	  'Rutgers, the State University of NJ' :"America/New_York" ,
	  'Syracuse University' : "America/New_York",
	  'UCLA' : "America/Los_Angeles",
	  'Purdue University--West Lafayette' : "America/New_York",
	  'Kenyon College' : "America/New_York",
	  'Colorado College': "America/Phoenix",
	  'Colorado School of Mines': "America/Phoenix",
	  'Cornell University':  "America/New_York",
	  'Trinity College' : "America/Chicago",
	  'Middlebury College' : "America/New_York",
	  'University of Alabama' : "America/Chicago",
	  'Emory U' : "America/New_York",
	  'Columbia': "America/New_York",
	  'Haverford College' : "America/New_York",
	  'University of California--Santa Barbara' : "America/Los_Angeles",
	  'Lafayette College' : "America/New_York",
	  'Lawrence University': "America/Chicago",
	  'Princeton' : "America/New_York",
	  'Georgetown University' : "America/New_York",
	  'Harvard' : "America/New_York",
	  'Worcester Polytechnic Institute' : "America/New_York",
	  'University of Southern California' : "America/Los_Angeles",
	  'University of Wisconsin--Madison' : "America/Chicago",
	  'Auburn University' : "America/Chicago",
	  'Northwestern Univeristy' : "America/Chicago",
	  'Rhodes College' : "America/Chicago",
	  'Florida State University' : "America/New_York",
	  'University of Miami' : "America/New_York",
	  'University of Chicago' : "America/Chicago",
	  'Miami University--Oxford' : "America/New_York",
	  'DePauw University' : "America/New_York",
	  'California Insititute of Technology' :"America/Los_Angeles",
	  'University of New Hampshire' : "America/New_York", 
	  'Smith College' : "America/New_York", 
	  'Bard College' : "America/New_York", 
	  'Texas A&M University--College Station' : "America/Chicago", 
	  'Grinnell College' : "America/Chicago", 
	  'Lewis & Clark College' : "America/Los_Angeles", 
	  'Wake Forest University' : "America/New_York",
	   'University of Denver' : "America/Phoenix",
	   'Brigham Young University--Provo' : "America/Phoenix",
	    'Indiana University' : "America/New_York",
	     'Rice University' : "America/Chicago",
	      'Pennsylvania State University--University Park' : "America/New_York",
	       'Ohio State University--Columbus' : "America/New_York",
	        'Clemson University': "America/New_York",
	         'Northeastern University' : "America/New_York",
	          'St. Lawrence University' : "America/New_York",
	           'Pepperdine University' : "America/Los_Angeles",
	            'Stanford' :"America/Los_Angeles"
	            }
	return zone[uni]
	
def timeSlot(hour):

	if hour>= 6 and hour<9:
		return "earlyMorning"
	elif hour >=9 and hour<12:
		return "lateMorning"
	elif hour >=12 and hour<15:
		return "earlyAfternoon"
	elif hour >=15 and hour <18:
		return "lateAfternoon"
	elif hour >=18 and hour <21:
		return "evening"
	elif hour >=21 and hour <=24:
		return "night"
	elif hour >= 0 and hour<3:
		return "lateNight"
	elif hour >=3 and hour <6:
		return "beforeSunRise"
	else:
		return "other"

def timeOfWeek(dayOfWeek):
	if dayOfWeek == "Saturday" or dayOfWeek == "Sunday":
		return "weekend"
	else:
		return "weekday"


def adjustTimezone(timestamp, uni):
	
	if uni == None:
		print None
		return timestamp

	zone = pytz.timezone(getZone(uni))
	isotime = iso8601.parse_date(timestamp)
	return isotime.astimezone(zone).isoformat()

def myTime(timestamp, uni = None):

	dct = {}
	timestamp = timestamp.strip('"')
	timestamp = adjustTimezone(timestamp, uni)
	date, rest = timestamp.split("T")
	if "+" in rest:
		hour = rest.split("+")[0]
	elif "-" in rest:
		hour = rest.split("-")[0]

	yyyy, mm, dd = date.split("-")
	hour, minute, second = hour.split(":") 
	
	dct["date"] = date
	
	dct["yyyy"] = int(yyyy)
	dct["mm"] = int(mm)
	dct["dd"] = int(dd)

	dct["hour"] = int(hour) 
	dct["minute"] = int(minute)
	dct["second"] = int(second)

	dct["DOW"] = (datetime.date(dct["yyyy"], dct["mm"],dct["dd"])).strftime("%A")
	dct["MOY"] = (datetime.date(dct["yyyy"], dct["mm"],dct["dd"])).strftime("%B")
	dct["TOD"] = timeSlot(dct["hour"])
	dct["TOW"] = timeOfWeek(dct["DOW"])
	dct["TODW"] = str(dct["TOD"])+str(dct["DOW"])

	return dct
	
def getTime(posts, uni, DOW, HOD, MOY, TOD, TOW, TODW):

	for post in posts[uni]:
		time = myTime(post["time"], uni)

		
		DOW += [time["DOW"]]
		HOD += [time["hour"]]
		MOY += [time["MOY"]]
		TOD += [time["TOD"]]
		TOW += [time["TOW"]]
		TODW += [time["TODW"]]
		
	return DOW, HOD, MOY, TOD, TOW, TODW

def splitTime(dateString):
	date, rest = dateString.split("T")
	hour = rest.split("+")[0]
	return date, hour


