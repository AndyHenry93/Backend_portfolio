from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea,label="message")

    email.widget.attrs.update({'class':'form-control'})
    message.widget.attrs.update({'class':'form-control'})
    
