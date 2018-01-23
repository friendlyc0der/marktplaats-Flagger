5import requests
import sys
from bs4 import BeautifulSoup
import json

flagDuration = 5

for x in range(0, flagDuration):
	session = requests.Session()
	itemId = sys.argv[1]
	flag_ad_get_url = 'https://www.marktplaats.nl/flag/flagAd.json?isFreeAd=true&itemId='+itemId
	flag_ad_post_url = 'https://www.marktplaats.nl/flag/flagAd.json?isFreeAd=true&itemId='+itemId
	fetch_xsrf_token = 'https://link.marktplaats.nl/'+itemId
	r = session.get(fetch_xsrf_token)
	soup = BeautifulSoup(r.text, "html5lib")
	xsrf = soup.find("input", {"name":"nl.marktplaats.xsrf.token"})['value']
	json_post_data = {"token":xsrf, "selectedReasonId":"8", "userMessage":"", "itemIds":[itemId] }
	json_post_data = json.dumps(json_post_data)
	print json_post_data
	#session.headers['Content-Type'] = 'application/json;charset=UTF-8'
	session.headers['x-mp-xsrf'] = xsrf
	#session.headers['Accept-Encoding'] = "gzip"
	session.headers['X-Requested-With'] = "XMLHttpRequest"
	#session.headers.update({"x-mp-xsrf":xsrf})
	headers = {'Content-type': 'application/json', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
	flag_ad = session.post(flag_ad_post_url, data=json_post_data, headers=headers)
	print flag_ad.status_code
	print flag_ad.text

