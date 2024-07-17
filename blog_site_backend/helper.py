import os
import hashlib
from datetime import datetime
from django.core.files.storage import FileSystemStorage

class HashedFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        hash_name = hashlib.md5(name.encode('utf-8')).hexdigest()
        ext = name.split('.')[-1]
        name = f"{hash_name}.{ext}"
        return super().get_available_name(name, max_length)

    def _save(self, name, content):
        today = datetime.now().strftime('%Y/%m/%d')
        name = os.path.join('images', today, name)
        return super()._save(name, content)


def resize_image(image, size):
    img = Image.open(image)
    img = img.convert("RGB")
    img.thumbnail(size, Image.ANTIALIAS)

    # Save the resized image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, format='JPEG', quality=90)
    img_content = ContentFile(img_io.getvalue(), image.name)
    
    return img_content