from .forms import BookModelForm

def add_book(request):
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'title': form.cleaned_data['title']})
    else:
        form = BookModelForm()

    return render(request, 'add_book.html', {'form': form})
