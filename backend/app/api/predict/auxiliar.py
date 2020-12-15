import base64
from PIL import Image
import io

def convert(msg):
    msg_decode = base64.b64decode(msg)
    return Image.open(io.BytesIO(msg_decode))