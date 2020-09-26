from io import BytesIO
from PIL import Image, ImageDraw


class ImageInfo:
    def __init__(self, request):
        self.request = request

    def image_size(self):
        image = Image.open(BytesIO(self.request.content))
        return {
            "width": image.size[0],
            "height": image.size[1],
            "ext": image.format,
            "size": str(round(int(self.request.headers['content-length']) / 1024, 2)) + " kB",
            "filename": image.filename
            }
