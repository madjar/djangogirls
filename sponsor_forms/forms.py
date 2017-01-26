from django import forms


class BaseSponsorForm(forms.Form):
    """
    A base class that implements the logic of converting between django field
    names and PDF field names (usually contain spaces and such).
    """

    PDF_NAME_MAPPING = {}

    def as_pdf_field_names(self):
        """
        Return a dict of the form's cleaned data where the keys are valid PDF
        field names (which can be different from the Django form's field names).
        """
        assert self.is_valid()
        return {self.PDF_NAME_MAPPING.get(k, k): v for k, v in self.cleaned_data.items()}


class GitHubWireRequestForm(BaseSponsorForm):
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

    PDF_NAME_MAPPING = {
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
