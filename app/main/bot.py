from flask import request, Response
from kik.messages import messages_from_json, TextMessage, PictureMessage

from . import main, kik

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
                kik.send_messages([
                PictureMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    pic_url="http://s17.postimg.org/k3nil5m3z/1445202676136.jpg"
                )
            ])
                
        return Response(status=200)
