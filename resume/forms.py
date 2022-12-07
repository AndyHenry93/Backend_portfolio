from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    subject = forms.CharField(max_length=150, label="subject")
    message = forms.CharField(widget=forms.Textarea,label="message")

    email.widget.attrs.update({'class':'form-control'})
    subject.widget.attrs.update({'class':'form-control'})
    message.widget.attrs.update({'class':'form-control'})
    
