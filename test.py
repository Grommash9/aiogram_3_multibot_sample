import random
import requests

# data = {'bot_token': '6035927404:AAHE41GHV5LoHTyMQdMqbMvIZ1XN7BpkEoo', 'message_text': 'A DA', 'target_chat': 5891826489}
# resp = requests.post('https://d4f6-159-224-193-190.eu.ngrok.io/send_notification', json=data)
# print(resp)
# print(resp.text)
#
#
# data = {'bot_token': '6035927404:AAHE41GHV5LoHTyMQdMqbMvIZ1XN7BpkEoo', 'message_text': str(random.randint(1,123124123125)), 'target_chat': 5891826489, 'message_id': 2}
# resp = requests.post('https://d4f6-159-224-193-190.eu.ngrok.io/edit_message', json=data)
# print(resp)
# print(resp.text)


# data = {'bot_token': '6035927404:AAFbFTWybBO0lLlK8jc-oADo-8Mr583xbLQ', 'new_owner_id': 5}
# resp = requests.post('https://d4f6-159-224-193-190.eu.ngrok.io/add_new_bot', json=data)
# print(resp)
# print(resp.text)


numbers_list = [1, 2, 3, 4, 5]

x = 9

for first_number in numbers_list:
    for second_number in numbers_list:
        if second_number + first_number == 9:
            print(first_number, second_number)
