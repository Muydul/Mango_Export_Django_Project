from django.shortcuts import render, redirect, get_object_or_404
from .models import MangoExport
from .forms import MangoExportForm
from django.db.models import Q 

def mango_list(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        mangos = MangoExport.objects.filter(
            Q(order_id__icontains=query) | Q(variety__icontains=query)
        )  # Search by order_id or variety
    else:
        mangos = MangoExport.objects.all()  # Display all if no query
    return render(request, 'mango/mango_list.html', {'mangos': mangos})


def mango_create(request):
    if request.method == "POST":
        form = MangoExportForm(request.POST)
        if form.is_valid():
            form.save()  # `order_id` is auto-generated
            return redirect('mango_list')
    else:
        form = MangoExportForm()
    return render(request, 'mango/create.html', {'form': form})

def mango_update(request, pk):
    mango = get_object_or_404(MangoExport, pk=pk)
    if request.method == "POST":
        form = MangoExportForm(request.POST, instance=mango)
        if form.is_valid():
            form.save()
            return redirect('mango_list')
    else:
        form = MangoExportForm(instance=mango)
    return render(request, 'mango/mango_form.html', {'form': form})

def mango_delete(request, pk):
    mango = get_object_or_404(MangoExport, pk=pk)
    if request.method == "POST":
        mango.delete()
        return redirect('mango_list')
    return render(request, 'mango/mango_confirm_delete.html', {'mango': mango})
