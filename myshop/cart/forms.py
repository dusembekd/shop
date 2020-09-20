from django import forms

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOISES, coerce=int)
    update = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=False)

