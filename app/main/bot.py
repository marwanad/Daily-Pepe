from flask import request, Response, jsonify
from kik.messages import messages_from_json, TextMessage, PictureMessage
import requests, requests_cache
import random
from . import main, kik
from setup import IMGUR_CLIENT_ID as imgur_client
from setup import pepe_url

requests_cache.install_cache('pepe_cache', backend='sqlite', expire_after=86400)

@main.route('/incoming', methods=['POST'])
def incoming():

    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])

    for message in messages:
        if isinstance(message, TextMessage):
            body_lower = message.body.lower()
            if body_lower == "another one":
                kik.send_messages([
                PictureMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    pic_url="http://40.media.tumblr.com/108878995b5b74bb89618dab799ded58/tumblr_nzwkikqhcH1titub2o1_1280.jpg"
                )
            ])
            elif body_lower == "ayy lmao":
                kik.send_messages([
                TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body=message.body
                )
            ])
            else:
                pepe_dict = requests.get(pepe_url, headers={'Authorization' : 'Client-ID %s' %imgur_client}).json()

                pepe_data = pepe_dict['data']['images']

                pimage_list = [pepe['link'] for pepe in pepe_data if pepe['type'] == 'image/jpeg' and pepe['nsfw'] is None]
                
                kik.send_messages([
                PictureMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    pic_url=random.choice(pimage_list)
                )
            ])
                
        return Response(status=200)
