from django.shortcuts import render, redirect, get_object_or_404
from blog_site_backend.models import Tag
from blog_site_backend.forms_folder.tag_forms import TagForm

# Create your views here.
def index(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})

def show(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'tags/tag_detail.html', {'tag': tag})

def create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags.index')
    else:
        form = TagForm()
    return render(request, 'tags/tag_form.html', {'form': form})

def update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tags.index')
    else:
        form = TagForm(instance=tag)
    return render(request, 'tags/tag_form.html', {'form': form})

def delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tags.index')
    return render(request, 'tags/tag_confirm_delete.html', {'tag': tag})
