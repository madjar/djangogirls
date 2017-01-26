from django.conf import settings
from django.http import HttpResponse
from django.views import generic


from .forms import GitHubWireRequestForm
from .utils import fill_form


class BasePDFFormView(generic.FormView):
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
    template_name = 'sponsor_forms/github_wire_request.html'
    form_class = GitHubWireRequestForm
    pdf_template_file = 'GitHub_Wire_request.pdf'
