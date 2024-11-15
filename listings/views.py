from .models import Property
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .forms import PropertyForm
from django.contrib import messages
from django.urls import reverse  # Import reverse for URL redirection
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm
from django.http import JsonResponse
from .models import ChatMessage
from .forms import ChatMessageForm

# Home View - Display all properties
def home(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {'properties': properties})

# Property Details View - Show detailed view of a specific property
def property_details(request, id):
    property = Property.objects.get(id=id)
    return render(request, 'property_details.html', {'property': property})

# View for Buy Properties page
def buy_properties(request):
    # Fetch properties where category is 'SELL'
    properties = Property.objects.filter(category='SELL')
    
    return render(request, 'buy.html', {'properties': properties})

# View for Sell Properties page

def sell_properties(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Property posted successfully!')
            return redirect('sell_properties')  # Redirect after successful submission
        else:
            messages.error(request, 'There was an error posting the property.')
    else:
        form = PropertyForm()

    return render(request, 'sell.html', {'form': form})
# View for Rent Properties page
from django.shortcuts import render
from .models import Property

def rent_properties(request):
    # Fetch properties where category is 'RENT'
    properties = Property.objects.filter(category='RENT')
    
    return render(request, 'rent.html', {'properties': properties})


# View for Property Post page
def post_property(request):
    # Logic for handling property post (form submission, etc.)
    return render(request, 'post_property.html')  # Render the property posting page

# Contact View - For contact form submission
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send an email or save to the database
        send_mail(
            f"Message from {name}",
            message,
            email,
            [settings.CONTACT_EMAIL],  # Email where you want to receive messages
        )

        return HttpResponse('Message Sent Successfully!')

    return render(request, 'contact.html')

# Live Stream View - Render the live streaming page
def live_stream(request):
    return render(request, 'live_stream.html')


# View for displaying and processing the contact form
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to the database
            contact_message = form.save()

            # Show success message
            messages.success(request, "Thank you for your message. We will get back to you soon.")
            return redirect('contact_us')  # Redirect to the contact page

        else:
            messages.error(request, "There was an error with your submission. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})

def live_stream(request):
    # Get all chat messages from the database
    messages = ChatMessage.objects.all().order_by('-timestamp')
    form = ChatMessageForm()

    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('live-stream')  # Refresh to see the new message

    return render(request, 'live_stream.html', {'messages': messages, 'form': form})

def get_new_messages(request):
    # Get new messages (since the last one seen by the client)
    last_message_id = request.GET.get('last_message_id', None)
    if last_message_id:
        new_messages = ChatMessage.objects.filter(id__gt=last_message_id).order_by('timestamp')
    else:
        new_messages = ChatMessage.objects.all().order_by('timestamp')

    messages_data = [{
        'user_name': msg.user_name,
        'message': msg.message,
        'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    } for msg in new_messages]

    return JsonResponse({'new_messages': messages_data})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage  # Assuming you have a ChatMessage model

@csrf_exempt
def clear_chat(request):
    if request.method == 'POST':
        ChatMessage.objects.all().delete()  # Delete all chat messages
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)

from django.shortcuts import get_object_or_404
from .models import Property
from .forms import PropertyForm
import os
# Edit Property View
def edit_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('buy_properties')  # Redirect to the list or detail view after saving
    else:
        form = PropertyForm(instance=property)
    return render(request, 'edit_property.html', {'form': form, 'property': property})

# Delete Property View
def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    # Delete the associated image file from media
    if property.image:
        if os.path.isfile(property.image.path):
            os.remove(property.image.path)
    # Delete the property from the database
    property.delete()
    messages.success(request, "Property deleted successfully!")
    return redirect('buy_properties')  # Redirect to the properties list or desired page