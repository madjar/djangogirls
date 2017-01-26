from django import forms


class GitHubWireRequestForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postcode = forms.CharField()

    iban = forms.CharField()
    swift = forms.CharField()
    bank_name = forms.CharField()
    bank_address = forms.CharField()
    bank_city = forms.CharField()
    bank_country = forms.CharField()

    routing_instructions1 = forms.CharField(required=False)
    routing_instructions2 = forms.CharField(required=False)

    def as_pdf_field_names(self):
        """
        Return a dict of the form's cleaned data where the keys are valid PDF
        field names (which can be different from the Django form's field names).
        """
        assert self.is_valid()
        NAME_MAPPING = {
            # Only in case the field name doesn't match the one in the PDF
            'name': 'Name on account',
            'postcode': 'postal code',

            'iban': 'Bank account number',
            'swift': 'Swift code',
            'bank_name': 'Bank name',
            'bank_address': 'bank address',
            'bank_city': 'City',
            'bank_country': 'Country',

            'routing_instructions1': 'additional 01',
            'routing_instructions2': 'additional 02',
        }

        return {NAME_MAPPING.get(k, k): v for k, v in self.cleaned_data.items()}
