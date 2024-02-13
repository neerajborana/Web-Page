from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})
