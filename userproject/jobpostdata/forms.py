from django import forms
from jobpostdata.models import applyjobs


class applyuser(forms.ModelForm):
    class Meta:
        model = applyjobs
        fields = ["jobtitle","first_name","last_name","email","phone","pg","degree","PU","school","resume"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply a black border to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({'style': 'border: 2px solid grey;'})
