from django.views import generic


from .forms import GitHubWireRequestForm
from .utils import fill_form


class GitHubWireRequestView(generic.FormView):
    template_name = 'sponsor_forms/github_wire_request.html'
    form_class = GitHubWireRequestForm
    pdf_template_file = 'form.pdf'

    def form_valid(self, form):
        pdf_data = fill_form(self.pdf_template_file, form.as_pdf_field_names())
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="form.pdf"'
        response.write(pdf_data)
        return response
