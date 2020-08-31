import re

class IntentHandler():

	def __init__(self, app):
		self.app = app
		self.intent_patterns = {}
		self.intent_patterns['greeting'] = ['hi.*', 'hello.*']
		self.intent_patterns['ack_message'] = ['message .*']

		# Combine all the different keys above into a single response
		for intent, keys in self.intent_patterns.items():
			self.intent_patterns[intent] = re.compile('|'.join(keys))

	def __match_intent(self, message):
		self.app.logger.info(message)
		for intent, pattern in self.intent_patterns.items():
			if re.search(pattern, message):
				return intent

	def get_text_response(self, event_data):
		message = event_data["event"]["text"]
		intent = self.__match_intent(message)
		if intent == None:
			return "Sorry, I didn't understand that."
		elif intent == 'greeting':
			return "Hello <@%s>! :tada:" % event_data["event"]["user"]
		elif intent == 'ack_message':
			return "ACK"

	def get_emoji_response(self, event_data):
		emoji = emoji = event_data["event"]["reaction"]
		if emoji == '+1':
			return 'ACK'
		else: 
			return ':bear:'




		
