from django import forms
from skillapp.models import Contacts, Customer, Admin, Sell, AddFeedback, Comment,Buy

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contacts
        fields="__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ('customer','title','description','cost','technologies','domain','datetime')

class AddFeedbackForm(forms.ModelForm):
    class Meta:
         model = AddFeedback
         fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
         model = Comment
         fields = "__all__"

class BuyForm(forms.ModelForm):
    class Meta:
         model = Buy
         fields = "__all__"