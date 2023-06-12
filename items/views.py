from django.shortcuts import render, HttpResponse, redirect
from items.models import Item, Image, File, Commentary
from items.forms import CreateItemForm

# Create your views here.
def create_item(request):
	if request.method == 'POST':
		create_item_form = CreateItemForm(request.POST, request.FILES)
		if create_item_form.is_valid():
			data_form = create_item_form.cleaned_data

			name = data_form['name']
			description = data_form['description']
			category = data_form['category']
			theme = data_form['theme']

			item = Item(
				name = name,
				description = description,
				category = category,
				theme = theme
			)

			item.save()

			if data_form['images']:
				c=0
				while c < len(request.FILES.getlist('images')):
					image = Image(
						image_item_id = item.id,
						image = request.FILES.getlist('images')[c]
					)

					image.save()
					c+=1

			if data_form['files']:
				c=0
				while c < len(request.FILES.getlist('files')):
					file = File(
						file_item_id = item.id,
						filename = request.FILES.getlist('files')[c]
					)

					file.save()
					c+=1
	else:
		create_item_form = CreateItemForm()

	return render(request, 'create_item.html', {
		'item_form':create_item_form
	})

def show_item(request, item_id=0):
	item = Item.objects.filter(id=item_id).first()
	images = Image.objects.filter(image_item_id=item_id)
	files = File.objects.filter(file_item_id=item_id)
	commentaries = Commentary.objects.filter(item_id=item_id).order_by('-created_at')

	return render(request, 'item.html', {
		'item':item,
		'images':images,
		'files':files,
		'commentaries':commentaries
	})

def comment(request, item_id=0, user_id=0):
	if request.method == 'POST':
		commentary = Commentary(
			content = request.POST['content'],
			item_id = item_id,
			user_id = user_id
		)

		commentary.save()

		return redirect('item', item_id=item_id)