from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FlowerForm
from .models import Flower


@login_required(login_url="login_url")
def create_order(request):
    template_name = 'flowerapp/create.html'
    form = FlowerForm()
    if request.method == "POST":
        form = FlowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_order(request):
    template_name = 'flowerapp/show.html'
    orders = Flower.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)


def update_order(request, pk):
    obj = Flower.objects.get(id=pk)
    form = FlowerForm(instance=obj)
    if request.method == "POST":
        form = FlowerForm(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, 'flowerapp/create.html', context)


def cancel_order(request, pk):
    obj = Flower.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, 'flowerapp/confirmation.html')
