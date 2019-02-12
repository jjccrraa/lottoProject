import json
import requests

FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v2.6/me/'

class Bot(object):
	def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
		self.access_token = access_token
		self.api_url = api_url

	def send_text_message(self, psid, message, messaging_type="RESPONSE"):
		headers = {
			'Content-Type': 'application/json'
		}

		data = {
			'messaging_type': messaging_type,
			'recipient': {'id': psid},
			'message': {'text': message}
		}

		params = {'access_token': self.access_token}
		self.api_url = self.api_url + 'messages'
		response = requests.post(self.api_url, headers=headers, params=params, data=json.dumps(data))
		print(response.content)

bot = Bot('EAAFtDP1VLrYBAOuPgbuaGJXbIhBOxBtnrZAB6EHgVhwsi5Tg7FtwwyDUdZAwKLh1gsmTxMuMpM1hZCGRh7zqD0FFzU7Se7JPUIg4etlbaOGVSMZCAuUJS1NeZCx0ytpZBlPd9sHO6A8MCfV2QDiIPzagPHXa8teyntnSkzWi41RwZDZD')
#bot.send_text_message(2045925488848914, 'Test 1')