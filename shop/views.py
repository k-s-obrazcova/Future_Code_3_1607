from django.shortcuts import render, get_object_or_404

from .forms import ProductFilterForm, SupplierForm
from .models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# Create your views here.

def list_product(request):
    product_list = Product.objects.all()
    context = {
        'list_product': product_list
    }
    return render(request, 'shop/product/all_product.html', context)

def list_product_with_filter(request):
    product_list = Product.objects.all()
    if request.GET != None:
        product_form = ProductFilterForm(request.GET)
    else:
        product_form = ProductFilterForm()

    if product_form.is_valid():
        if product_form.cleaned_data.get('name') != "":
            product_list = product_list.filter(name__contains=product_form.cleaned_data.get('name'))
        if product_form.cleaned_data.get('min_price'):
            product_list = product_list.filter(price__gte=product_form.cleaned_data.get('min_price'))
        if product_form.cleaned_data.get('max_price'):
            product_list = product_list.filter(price__lte=product_form.cleaned_data.get('max_price'))

    context = {
        'product_list': product_list,
        'form': product_form,
    }
    return render(request, 'shop/product/all_product_filter.html', context)


def get_one_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, 'shop/product/one_product_table.html', context)


def get_one_filter_product(request):
    product_list = Product.objects.filter(is_exists=request.GET.get('is_ex'))
    context = {
        'list_product': product_list
    }
    return render(request, 'shop/product/all_product.html', context )


def get_more_filter_product(request):
    product_list = Product.objects.filter(
        price__gt=request.GET.get('min_price'),
        price__lte=request.GET.get('max_price')
    )
    context = {
        'list_product': product_list
    }
    return render(request, 'shop/product/all_product.html', context)


class ListSupplier(ListView):
    model = Supplier
    template_name = 'shop/supplier/supplier_list.html'
    allow_empty = True

class CreateSupplier(CreateView):
    model = Supplier
    extra_context = {
        'action': 'Создать'
    }
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm

class DetailSupplier(DetailView):
    model = Supplier
    template_name = 'shop/supplier/supplier_detail.html'

class UpdateSupplier(UpdateView):
    model = Supplier
    extra_context = {
        'action': 'Изменить'
    }
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm

class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = 'shop/supplier/supplier_delete.html'
    success_url = reverse_lazy('supplier_list')

