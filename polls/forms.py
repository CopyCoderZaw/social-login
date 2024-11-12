from django.forms import ModelForm,TextInput ### modelform, widgets
from .models import CustomUser, City,Year,Photo### customuser model
from django import forms
from django.contrib.auth.forms import UserCreationForm

### CustomUserForm
class MyCustomForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

##### Profile Form
class ProForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile']
    
#### Weather
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {"name" : TextInput(attrs = {"class" : "form-control", "placeholder" : " Enter your choose city "})}
        
#### Year
class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ['name']
        widgets = {"name" : TextInput(attrs = {"class":"form-control", "placeholder": "Enter your write year ...", "type":"text"})}
        
### Photo
class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        widgets = {'year' :forms.Select(attrs = {'class':'form-control', "type":"text","placeholder":"Select"}),
                   'title': forms.TextInput(attrs = {'class':'form-control', "type":"text", "placeholder":"Enter your write title ..."}),
                   
                   }
        