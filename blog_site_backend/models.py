from django.db import models
import os
from PIL import Image
import datetime
import hashlib

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




def resize_image(image, size):
    img = Image.open(image)
    img.thumbnail(size)
    return img

def generate_hashed_filename(image):
    # Generate a unique hash for the image file
    image_hash = hashlib.sha256(image.read()).hexdigest()
    return image_hash

def save_resized_images(image, filename):
    sizes = {
        "large": (800, 800),
        "middle": (400, 400),
        "small": (200, 200)
    }
    saved_files = {}
    date_folder = datetime.date.today().strftime('%Y/%m/%d')
    save_path = os.path.join('media', 'images', date_folder)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Generate hashed filename
    hashed_filename = generate_hashed_filename(image)

    for size_name, size in sizes.items():
        resized_img = resize_image(image, size)
        saved_filename = f"{hashed_filename}-{size_name}.png"
        saved_path = os.path.join(save_path, saved_filename)
        resized_img.save(saved_path)
        saved_files[size_name] = saved_filename

    # Delete original image after resizing
    image.seek(0)
    image.delete()

    return saved_files




class Categories(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children', null=True, blank=True)
    categoryable_type = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True, blank=True)
    
    image = models.ImageField(upload_to='images/')
    versions = models.JSONField(blank=True, null=True)

    # image_versions = models.JSONField(default=dict)
    
    # image = models.ImageField(upload_to='images', storage=HashedFileSystemStorage())

    # image = models.ImageField(upload_to='images/', null=True, blank=True)
    # file = models.FileField(upload_to='specific_folder/')
    # image = models.ImageField(upload_to='images/')
    order = models.IntegerField(null=True, blank=True)
    status = models.SmallIntegerField(default=1)



    # def save(self, *args, **kwargs):
    #     if self.image:
    #         filename = self.image.name.split('.')[0]
    #         self.versions = save_resized_images(self.image, filename)
    #     super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        if self.image:
            filename = self.image.name.split('.')[0]
            self.versions = save_resized_images(self.image, filename)
            # Clear the original image field after saving versions
            self.image = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.image.name


    def __str__(self):
        if self.parent:
            return f"{self.parent.name} - {self.name}"
        else:
            return f"{self.name}"