import os
from django.db import models

from picasa import  PicasaField

def albums():
    from picasa import PicasaStorage
    storage= PicasaStorage()
    return [(a.title.text,a.title.text) for a in storage.albumsFromUser()]
    
def tags():
    from picasa import PicasaStorage
    storage= PicasaStorage()
    return [(a.title.text,a.title.text) for a in storage.albumsFromUser()]
    
def get_Album(instance, filename):
    album = instance.album.name
    return os.path.join(album, filename)
    
    
class Album(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name
        
class Image(models.Model):
    title = models.CharField(max_length=128)
    tags = models.CharField(max_length=50, choices = tags())
    mediaPhoto = PicasaField(upload_to=get_Album, blank=True)
    dropBoxPhoto = PicasaField(blank=True)
    album = models.ForeignKey(Album)
    
    def __unicode__(self):
        return self.dropBoxPhoto.url


	
		
	
