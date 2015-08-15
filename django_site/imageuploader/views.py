from django.shortcuts import render
from django.http import HttpResponse


from imageuploader.forms import UploadImageForm
from imageuploader.models import ImageModel

from django.utils.html import escapejs
from django.views.decorators.csrf import csrf_exempt


def imageupload(request):
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        print "asdf"
        image_model = ImageModel()
        image_model.image = form.cleaned_data['image']
        image_model.save()
        url = image_model.image.url
        print url
        return HttpResponse("<script>top.tinymce.activeEditor.windowManager.getParams().callback_func('%s');top.tinymce.activeEditor.windowManager.close(); </script>" % url)
    return HttpResponse("<script>alert('%s');</script>ImageField" % escapejs('\n'.join([v[0] for k, v in form.errors.items()])))


def uploader(request):
    return render(request, 'uploader.html')










