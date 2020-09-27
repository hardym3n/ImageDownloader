from io import BytesIO
from PIL import Image, ImageDraw, UnidentifiedImageError
import magic
import sys

class ImageInfo:
    def __init__(self, request):
        self.request = request

    def check_file_type(self):
        return magic.from_buffer(BytesIO(self.request.content).read(2048))

    def image_size(self):
        try:
            image = Image.open(BytesIO(self.request.content))
            return {
                "width": image.size[0],
                "height": image.size[1],
                "ext": image.format,
                "size": str(round(sys.getsizeof(self.request.content) / 1024, 2)) + " kB"
            }
        except UnidentifiedImageError:
            ext = self.check_file_type().split()[0]
            print("EXT", ext)
            return {
                "ext": ext,
                "size": str(round(sys.getsizeof(self.request.content) / 1024, 2)) + " kB"
            }

