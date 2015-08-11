__author__ = 'derek'

from mezzanine.galleries.models import GalleryImage
from mezzanine.galleries.models import Gallery
import random

RECENT_GALLERY_IMAGES_TO_SHOW = 10

def all_gallery_images(request):
    gallery_images = GalleryImage.objects.all().order_by('?')[:RECENT_GALLERY_IMAGES_TO_SHOW]
    #gallery_images = GalleryImage.objects.order_by('created')[:RECENT_GALLERY_IMAGES_TO_SHOW]

    return {"all_gallery_images": gallery_images}
