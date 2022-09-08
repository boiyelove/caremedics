from django.shortcuts import render, Http404

# Create your views here.
from .models import Product, Catalog, CatalogCategory

def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query': q, 'products': products}
		template = 'products/results.html'	
	else:
		template = 'products/home.html'	
		context = {}
	return render(request, template, context)

def home(request):
	products = Product.objects.all()
	catalogs = Catalog.objects.all()
	category = CatalogCategory.objects.all()
	template = "products/home.html"
	context = {
		"products": products,
		"catalog": catalogs,
		"category": category,
	}
	return render(request, template, context)
def catalog(request, slug):
	cat = CatalogCategory.objects.get(slug=slug)
	products = Product.objects.filter(category = cat)
	
	template = "products/home.html"
	context = {
		"products": products,
		
	}
	return render(request, template, context)

def single(request, slug):
	try:
		product = Product.objects.get(slug = slug)
		context = {"product": product}
		template = "products/single.html"
		return render(request, template, context)
	except:
		raise Http404

def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'
	return render(request, template, context)


