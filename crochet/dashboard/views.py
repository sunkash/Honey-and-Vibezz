from django.shortcuts import render
from item.models import Item, Category
from django.contrib.auth.decorators import login_required 
# Create your views here.


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    categories = Category.objects.all()
    return render(request, 'dashboard/index.html', {
        'items':items,
        'categories': categories,
    })


