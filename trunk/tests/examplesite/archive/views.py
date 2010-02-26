
from django.shortcuts import render_to_response
from examplesite.archive.models import Image

 
def images(request):
	return render_to_response('archive/images.html', {'images':Image.objects})
