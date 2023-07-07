from django.shortcuts import render
from django.http import HttpResponse
from .forms import PDFMergeForm
from .utils import merge_pdf_with_page
def merge_pdf(request):
    if request.method == 'POST':
        form = PDFMergeForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            page_file = form.cleaned_data['page_file']
            position = form.cleaned_data['position']
            merged_pdf = merge_pdf_with_page(pdf_file, page_file, position)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="merged_pdf.pdf"'
            response.write(merged_pdf.getvalue())

            return response
    else:
        form = PDFMergeForm()

    context = {'form': form}
    return render(request, 'pdfmerge/merge_pdf.html', context)
