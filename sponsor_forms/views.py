from os import path

from django.conf import settings
from django.http import HttpResponse
from django.views import generic


from .forms import GitHubWireRequestForm, GithubInvoiceForm, GitHubACHRequestForm
from .utils import fill_form


class BasePDFFormView(generic.FormView):
    template_name = 'sponsor_forms/base_form.html'

    pdf_template_file = None  # Child class should define this

    def form_valid(self, form):
        """
        Generate a response that downloads the PDF data.
        """
        actual_template_location = path.join(settings.SPONSOR_FORM_PDF_DIR, self.pdf_template_file)
        pdf_data = fill_form(actual_template_location, form.as_pdf_field_names())
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(self.pdf_template_file)
        response.write(pdf_data)
        return response


class GitHubWireRequestView(BasePDFFormView):
    form_class = GitHubWireRequestForm
    pdf_template_file = 'GitHub_Wire_request.pdf'


class GitHubACHRequestView(BasePDFFormView):
    form_class = GitHubACHRequestForm
    pdf_template_file = 'GitHub_ACHrequest.pdf'


class GithubInvoiceView(BasePDFFormView):
    form_class = GithubInvoiceForm
    pdf_template_file = 'Github_invoice.pdf'
