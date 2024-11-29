from django.shortcuts import render, get_object_or_404
from .models import Phone

def catalog(request):
    sort_by = request.GET.get('sort', 'name')  # Получаем параметр сортировки из URL
    if sort_by == 'price':
        phones = Phone.objects.all().order_by('price')
    elif sort_by == 'min_price':
        phones = Phone.objects.all().order_by('-price')  # Сортировка по убыванию цены
    else:
        phones = Phone.objects.all().order_by('name')

    return render(request, 'catalog.html', {'phones': phones})

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})
