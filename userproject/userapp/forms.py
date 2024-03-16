from django import forms
from django.contrib.auth.models import User
from userapp.models import userdetails,blogpost,comments,subscribe
from jobpostdata.models import applyjobs

class usrform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password"]
    

class userprofile(forms.ModelForm):
    class Meta:
        model = userdetails
        fields = ["user_img","address"]


class usr_update(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username","email","first_name","last_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply a black border to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({'style': 'border: 2px solid grey;'})

    

class usr_img(forms.ModelForm):
    class Meta:
        model = userdetails
        fields = ["user_img","address","linkedin","facebook","instagram","twitter"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply a black border to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({'style': 'border: 2px solid grey;'})

class blogpostform(forms.ModelForm):
    post_type = forms.CharField(widget=forms.TextInput(attrs={'style': 'border: 2px solid black;'}))
    class Meta:
        model = blogpost
        fields = ["post_type","post_title","sub_title","description","image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply a black border to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({'style': 'border: 2px solid grey;'})
        
    
        

class commentform(forms.ModelForm):
    parent_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = comments
        fields = ["content","parent"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply a black border to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({'style': 'border: 2px solid grey;'})

class subscribeform(forms.ModelForm):
    class Meta:
        model = subscribe
        fields = ["email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply a black border to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({'style': 'border: 2px solid grey;'})

class subscribeform1(forms.ModelForm):
    class Meta:
        model = subscribe
        fields = ["email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply a black border to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({'style': 'border: 2px solid grey;'})

