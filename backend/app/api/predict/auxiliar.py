import base64
from PIL import Image
import io

def convert(msg):
    text_msg = msg.split('base64,')[1]
    msg_decode = base64.b64decode(text_msg)

    return Image.open(io.BytesIO(msg_decode))