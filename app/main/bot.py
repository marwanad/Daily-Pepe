from flask import request, Response
from kik.messages import messages_from_json, TextMessage

from . import main, kik

@main.route('/incoming', methods=['POST'])
def incoming():
    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])

    for message in messages:
        if isinstance(message, TextMessage):
            kik.send_messages([
                PictureMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    pic_url="http://s17.postimg.org/k3nil5m3z/1445202676136.jpg"
                )
            ])

        return Response(status=200)
