from django.forms import ModelForm

from django import forms

from online_shop_app.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_restricted_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_restricted_words(description)
        return description

    def validate_restricted_words(self, text):
        restricted_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for word in restricted_words:
            if word in text.lower():
                raise forms.ValidationError(f"Запрещено использование слова: {word}")
