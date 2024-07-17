from django.shortcuts import render, redirect, get_object_or_404
from blog_site_backend.models import Tag
from blog_site_backend.forms_folder.tag_forms import TagForm
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
    tags = Tag.objects.all().order_by('-id')
    translated_word = _("Hello, world!")
    return render(request, 'tags/index.html', {
        'tags': tags,
        'translated_word': translated_word
    })

def show(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'tags/show.html', {'tag': tag})

def create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags.index')
    else:
        form = TagForm()
    return render(request, 'tags/create.html', {'form': form})

def update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tags.index')
    else:
        form = TagForm(instance=tag)
    return render(request, 'tags/create.html', {'form': form})

def delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tags.index')
    return render(request, 'tags/tag_confirm_delete.html', {'tag': tag})
