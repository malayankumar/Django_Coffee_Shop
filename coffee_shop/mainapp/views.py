from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
)
from .models import Product

# Home Page - ListView
class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'product_list'  # This replaces 'products' in the template

# About Page - TemplateView
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Ayan"
        context['students'] = ["Varun", "Harsha", "Srikanth"]
        context['slept'] = False
        return context

# Add Product - CreateView
class AddProduct(CreateView):
    model = Product
    fields = ['name', 'price', 'desc', 'pic', 'stock']
    template_name = 'addproduct.html'
    success_url = reverse_lazy('home')

# Product Details - DetailView
class ProductDetails(DetailView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'prod'

# Update Product - UpdateView
class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'editproduct.html'

    def get_success_url(self):
        return reverse_lazy('prod_details', kwargs={'pk': self.object.pk})

# Delete Product - DeleteView
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delproduct.html'
    success_url = reverse_lazy('home')

# Search Product - ListView (Refactored)
class SearchView(ListView):
    model = Product
    template_name = 'searchResults.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('search_text')
        return Product.objects.filter(name__icontains=query) if query else Product.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search_text', '')
        return context
