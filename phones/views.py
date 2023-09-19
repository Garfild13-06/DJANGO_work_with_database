from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get("sort", "")
    template = 'catalog.html'
    if sort == "":
        phones_objects = Phone.objects.all()
    elif sort == "name":
        phones_objects = Phone.objects.all().order_by('name').values()
    elif sort == "min_price":
        phones_objects = Phone.objects.all().order_by('price').values()
    elif sort == "max_price":
        phones_objects = Phone.objects.all().order_by('-price').values()
    context = {'phones': phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=str(slug)).first()
    context = {"phone": phone}
    return render(request, template, context)
