from django.forms import ModelForm

from django import forms

from online_shop_app.models import Product, Version


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'CheckboxInput':
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})


class ProductForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'price')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_restricted_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_restricted_words(description)
        return description

    @staticmethod
    def validate_restricted_words(text):
        restricted_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for word in restricted_words:
            if word in text.lower():
                raise forms.ValidationError(f"Запрещено использование слова: {word}")


class ProductModeratorForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')


class VersionForm(ModelForm, StyledFormMixin):
    class Meta:
        model = Version
        fields = ['product', 'number_version', 'name_version', 'is_active']
