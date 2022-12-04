from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=150, label="Full Name")
    email = forms.EmailField(label="Email")
    subject = forms.CharField(max_length=150, label="subject")
    message = forms.CharField(widget=forms.Textarea,label="message")

    full_name.widget.attrs.update({'class':'form-control'})
    email.widget.attrs.update({'class':'form-control'})
    subject.widget.attrs.update({'class':'form-control'})
    message.widget.attrs.update({'class':'form-control'})
    
