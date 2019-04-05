from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Comment(models.Model):
	content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	text = RichTextUploadingField()
	comment_time = models.DateTimeField(auto_now_add=True)
	user = models.CharField(max_length=100)
	class Meta:
		ordering=['-comment_time']

	

    
    

