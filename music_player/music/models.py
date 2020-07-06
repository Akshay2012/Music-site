from django.db import models

# Create your models here.

#SUPERUSER
#username=aks and pass - 12345

class album(models.Model):
    artist=models.CharField(max_length=330)
    genre=models.CharField(max_length=400)
    album_title=models.CharField(max_length=450)
    album_image=models.CharField(max_length=1000)


    def __str__(self):
        return self.artist+"'s "+self.album_title

class song(models.Model):
    album=models.ForeignKey(album,on_delete=models.CASCADE)  #When Album is deleted,all songs are deleted associated with it.
    file_type=models.CharField(max_length=100)
    song_title=models.CharField(max_length=300)
      

    