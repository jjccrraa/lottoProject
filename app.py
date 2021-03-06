import json
from flask import Flask, request
from bot import Bot
import scrape

PAGE_ACCESS_TOKEN = 'EAAFtDP1VLrYBAOuPgbuaGJXbIhBOxBtnrZAB6EHgVhwsi5Tg7FtwwyDUdZAwKLh1gsmTxMuMpM1hZCGRh7zqD0FFzU7Se7JPUIg4etlbaOGVSMZCAuUJS1NeZCx0ytpZBlPd9sHO6A8MCfV2QDiIPzagPHXa8teyntnSkzWi41RwZDZD'

url = 'https://www.pcso.gov.ph/SearchLottoResult.aspx'


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
	if request.method == 'GET':
		token = request.args.get('hub.verify_token')
		challenge = request.args.get('hub.challenge')
		if token == 'secreto':
			return str(challenge)
		return '400'

	else:
		print(request.data)
		data = json.loads(request.data.decode('utf-8'))
		messaging_events = data['entry'][0]['messaging']
		bot = Bot(PAGE_ACCESS_TOKEN)
		for message in messaging_events:
			user_id = message['sender']['id']
			text_input = message['message'].get('text')
			
			#print('Message from user ID {} - {}'.format(user_id, text_input))
			#bot.send_text_message(user_id, 'Yo waddup!')
			#bot.send_text_message(user_id, 'Yoyo!')

			table = scrape.get_contents(url)
			td = scrape.relevant_results(table)
			grouped = scrape.grouper(td)
			lotto_game = scrape.game_select(text_input, grouped)

			message = "Lotto Game: \n"+ lotto_game[0] + "\n\n" + "Winning Combination: \n"+ lotto_game[1] + "\n\n" + "Date: \n"+ lotto_game[2] + "\n\n" + "Prize: \n"+ lotto_game[3] + "\n\n" + "Winners: \n"+ lotto_game[4]

			bot.send_text_message(user_id, message)
			
		return '200'

if __name__ == '__main__':
	app.run(debug=True)