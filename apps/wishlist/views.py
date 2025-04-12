from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import WishlistItem
import pandas as pd
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def index(request):
    order_by = request.GET.get('order_by', 'ordem_personalizada')
    items = WishlistItem.objects.all().order_by(order_by)
    return render(request, 'wishlist/index.html', {'items': items})

@csrf_exempt
@require_http_methods(["POST"])
def add_item(request):
    try:
        data = json.loads(request.body)
        item = WishlistItem.objects.create(**data)
        return JsonResponse({'status': 'success', 'id': item.id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def export_markdown(request):
    items = WishlistItem.objects.all()
    markdown = "# Minha Wishlist\n\n"
    for item in items:
        markdown += item.to_markdown() + "\n"
    response = HttpResponse(markdown, content_type='text/markdown')
    response['Content-Disposition'] = 'attachment; filename="wishlist.md"'
    return response

@csrf_exempt
def export_excel(request):
    items = WishlistItem.objects.all()
    df = pd.DataFrame.from_records(items.values())
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="wishlist.xlsx"'
    df.to_excel(response, index=False)
    return response

@csrf_exempt
@require_http_methods(["POST"])
def update_order(request):
    data = json.loads(request.body)
    for item_id, order in data.items():
        WishlistItem.objects.filter(id=item_id).update(ordem_personalizada=order)
    return JsonResponse({'status': 'success'})

@csrf_exempt
@require_http_methods(["POST"])
def update_status(request, item_id):
    try:
        item = WishlistItem.objects.get(id=item_id)
        item.status = request.POST.get('status')
        item.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)