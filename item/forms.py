from django import forms
from .models import Item

INPUT_FIELD = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')
        widgets = {
            'category':forms.Select(attrs={
                'class': INPUT_FIELD  
            }),

            'name':forms.TextInput(attrs={
                'class': INPUT_FIELD  
            }),

            'description':forms.Textarea(attrs={
                'class': INPUT_FIELD  
            }),

            'price':forms.TextInput(attrs={
                'class': INPUT_FIELD  
            }),

            'image':forms.FileInput(attrs={
                'class': INPUT_FIELD  
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold')
        widgets = {
            
            'name':forms.TextInput(attrs={
                'class': INPUT_FIELD  
            }),

            'description':forms.Textarea(attrs={
                'class': INPUT_FIELD  
            }),

            'price':forms.TextInput(attrs={
                'class': INPUT_FIELD  
            }),

            'image':forms.FileInput(attrs={
                'class': INPUT_FIELD  
            })
        }

