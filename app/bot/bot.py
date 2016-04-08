from flask import Flask, request, Response

from kik.messages import messages_from_json, TextMessage

from . import main
import sys
from ..setup import kik, bot_config

@main.route('/incoming', methods=['POST'])
def incoming():
    print("incoming")
    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])
    print(messages)
    for message in messages:
        if isinstance(message, TextMessage):
            kik.send_messages([
                TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body=message.body
                )
            ])

        return Response(status=200)
