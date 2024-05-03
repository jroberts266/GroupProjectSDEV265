from django.shortcuts import render, get_object_or_404
from django.views import View
from store.models.product import Products

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        return render(request, 'product_detail.html', {'product': product})
