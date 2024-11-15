# forms.py
from django import forms
from .models import Property
from .models import ContactMessage
from .models import ChatMessage

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'price', 'location', 'area', 'bedrooms', 'bathrooms', 'features', 'category', 'image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['user_name', 'message']