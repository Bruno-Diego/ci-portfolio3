import requests 
import json

url = "https://random-words5.p.rapidapi.com/getMultipleRandom"

querystring = {"count":"2","minLength":"6","maxLength":"10"}

headers = {
	"X-RapidAPI-Key": os.environ.RAPID_API_KEY,
	"X-RapidAPI-Host": "random-words5.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
def getWord():
	return json.loads(response.text)[0]

getWord()