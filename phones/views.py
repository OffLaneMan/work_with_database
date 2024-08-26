from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_ = request.GET.get('sort')
    if sort_ == "name":
        phone = Phone.objects.order_by('name').all()
    elif sort_ == 'min_price':
        phone = Phone.objects.order_by('price').all()
    elif sort_ == 'max_price':
        phone = Phone.objects.order_by('-price').all()
    else:
        phone = Phone.objects.all()
    phones = [
        {
            'name': p.name,
            'price': p.price,
            'image': p.image,
            'release_date': p.release_date,
            'lte_exists': p.lte_exists,
            'slug': p.slug,
        }
        for p in phone]
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p = Phone.objects.filter(slug=slug).first()
    phone = {
        'name': p.name,
        'price': p.price,
        'image': p.image,
        'release_date': p.release_date,
        'lte_exists': p.lte_exists,
    }
    context = {'phone': phone}
    return render(request, template, context)
