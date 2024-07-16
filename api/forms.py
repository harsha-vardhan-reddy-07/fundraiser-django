from django import forms

USER_TYPE={
        ('', 'Choose user type'),
        ('admin', 'admin'),
        ('user', 'user')
    }

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})) 
    usertype = forms.ChoiceField(choices=USER_TYPE, widget=forms.Select(attrs={'class': 'form-control mb-3', 'placeholder': 'Choose user type'}))

class LoginForm(forms.Form): 
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


PURPOSES = {
    ('Personal Education', 'Personal Education'),
    ('Personal Health', 'Personal Health'),
    ('Orphanages/Oldagehomes', 'Orphanages/Oldagehomes'),
    ('Disaster Relief', 'Disaster Relief')    

}

class FundraiserForm(forms.Form):
    applicantName = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    applicantEmail = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    applicantMobile = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    title = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    description = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    bannerImage = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    purpose = forms.ChoiceField(choices=PURPOSES, widget=forms.Select(attrs={'class': 'form-control mb-3', 'placeholder': 'Choose user type'}))
    deadline = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control mb-3',}))
    targetAmount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    extraImage1 = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    extraImage2 = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    extraImage3 = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    

class FundraiserUpdateForm(forms.Form):
    applicantName = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    applicantEmail = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    applicantMobile = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    title = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    description = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    bannerImage = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    purpose = forms.ChoiceField(choices=PURPOSES, widget=forms.Select(attrs={'class': 'form-control mb-3', 'placeholder': 'Choose user type'}))
    deadline = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control mb-3',}))
    targetAmount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    extraImage1 = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    extraImage2 = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    extraImage3 = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    

class DonationForm(forms.Form):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}))
    remarks = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Remarks'}))