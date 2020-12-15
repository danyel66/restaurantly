from django import forms


class ContactForm(forms.Form):
    Name = forms.CharField(required=True, widget=forms.TextInput(attrs=
                        {
                            'name': 'name',
                            'type': 'text',
                            'id': 'name',
                            'class': 'form-control',
                            'placeholder': 'Your Name'
                        }))


    Email = forms.EmailField(required=True, widget=forms.TextInput(attrs=
                        {
                            'name': 'email',
                            'type': 'email',
                            'id': 'email',
                            'class': 'form-control',
                            'placeholder': 'Your Email'
                        }))

    Subject = forms.CharField(required=True, widget=forms.TextInput(attrs=
                            {
                                'name': 'subject',
                                'type': 'text',
                                'id': 'subject',
                                'class': 'form-control',
                                'placeholder': 'Subject'
                            }))

    Message = forms.CharField(required=True, widget=forms.Textarea(attrs=
                            {
                                'name': 'message',
                                'type': 'text',
                                'id': 'message',
                                'class': 'form-control',
                                'placeholder': 'Write your Message here...',
                                'col': '30',
                                'row': '8'
                            }))