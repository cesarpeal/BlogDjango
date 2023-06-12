from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import uuid
import os

# Create your models here.

class Theme(models.Model):
	def get_file_path(instance, filename):
		ext = filename.split('.')[-1]
		filename = "%s.%s" % (uuid.uuid4(), ext)
		return os.path.join('theme images/', filename)

	name = models.CharField(max_length=100, verbose_name='Nombre')
	image = models.ImageField(upload_to=get_file_path, verbose_name='Imagen tema')

	class Meta:
		verbose_name = 'Tema'
		verbose_name_plural = 'Temas'

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nombre')
	description = models.TextField(verbose_name='Descripcion')
	category = models.CharField(max_length=100,verbose_name='Categoria')
	theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Item'
		verbose_name_plural = 'Items'

	def __str__(self):
		return self.name

class Commentary(models.Model):
	content = models.CharField(max_length=255, verbose_name="contenido")
	item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
	def get_file_path(instance, filename):
		ext = filename.split('.')[-1]
		filename = "%s.%s" % (uuid.uuid4(), ext)
		return os.path.join('images/', filename)

	image = models.ImageField(upload_to=get_file_path, verbose_name='Imagen')
	image_item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'Imagen'
		verbose_name_plural = 'Imagenes'

	def image_tag(self):
		if self.image:
			return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
		else:
			return 'No Image Found'
	image_tag.short_description = 'Image'

class File(models.Model):
	def get_file_path(instance, filename):
		ext = filename.split('.')[-1]
		filename = "%s.%s" % (uuid.uuid4(), ext)
		return os.path.join('files/', filename)

	filename = models.FileField(upload_to=get_file_path, verbose_name='Archivo')
	file_item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'File'
		verbose_name_plural = 'Files'