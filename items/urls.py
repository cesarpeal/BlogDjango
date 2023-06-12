from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('create-item/', views.create_item, name="crear_item"),
	path('item/<int:item_id>', views.show_item, name="item"),
	path('comment/<int:item_id>/<int:user_id>', views.comment, name="comment")
]

# Ruta de imágenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)