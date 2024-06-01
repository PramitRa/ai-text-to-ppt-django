from django.shortcuts import render
from django.http import HttpResponse
from .forms import PresentationForm
from .text_generation import generate_text
from .ppt_creation import create_ppt_from_content
import io

def index(request):
    return render(request, 'presentation/index.html')

def show_form(request):
    if request.method == 'POST':
        form = PresentationForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            slide_number = form.cleaned_data['slide_number']
            
            # Generate the presentation
            response = generate_text(topic, slide_number)
            pptx_data = create_ppt_from_content(response, topic)
            
            # Save to a BytesIO object
            file_path = f"{topic.replace(' ', '_')}.pptx"
            with io.BytesIO() as file:
                file.write(pptx_data.read())
                file.seek(0)
                response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
                response['Content-Disposition'] = f'attachment; filename={file_path}'
                return response
    else:
        form = PresentationForm()

    return render(request, 'presentation/form.html', {'form': form})

