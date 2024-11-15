from django.contrib import admin
from django.urls import path
from listings import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('property/<int:id>/', views.property_details, name='property_details'),
    path('buy/', views.buy_properties, name='buy_properties'),
    path('sell/', views.sell_properties, name='sell_properties'),  # Keep this
    path('rent/', views.rent_properties, name='rent_properties'),
    path('contact/', views.contact, name='contact'),
    path('live-stream/', views.live_stream, name='live_stream'),
    path('contact/', views.contact_us, name='contact_us'),
    path('live-streaming/', views.live_stream, name='live-stream'),
    path('get-new-messages/', views.get_new_messages, name='get-new-messages'),
    path('clear-chat/', views.clear_chat, name='clear-chat'),
    path('property/edit/<int:id>/', views.edit_property, name='edit_property'),
    path('property/delete/<int:id>/', views.delete_property, name='delete_property'),
    path('delete-property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('edit/<int:property_id>/', views.edit_property, name='edit_property'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
