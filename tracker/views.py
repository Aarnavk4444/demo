import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import GroceryItem

def calculate_status(expiry_date):
    today = datetime.now().date()
    days_left = (expiry_date - today).days

    if days_left < 0:
        return "Expired", "#ef4444"
    elif days_left <= 3:
        return "Expiring Soon", "#f59e0b"
    else:
        return "Fresh", "#10b981"

def dashboard(request):
    db_items = GroceryItem.objects.all().order_by('expiry_date')
    processed_items = []
    has_expired_items = False

    for item in db_items:
        status, color = calculate_status(item.expiry_date)
        if status == "Expired":
            has_expired_items = True
        processed_items.append({
            'id': item.id,
            'name': item.name,
            'category': item.category,
            'expiry_date': item.expiry_date.strftime('%Y-%m-%d'),
            'status': status,
            'color': color
        })

    # Matplotlib Generation
    chart_dir = os.path.join(os.path.dirname(__file__), 'static', 'tracker', 'images')
    os.makedirs(chart_dir, exist_ok=True)
    chart_path = os.path.join(chart_dir, 'expiry_chart.png')
    
    has_chart = False
    if processed_items:
        df = pd.DataFrame(processed_items)
        status_counts = df['status'].value_counts()
        
        plt.figure(figsize=(6, 4))
        status_counts.plot(kind='bar', color=['#10b981', '#f59e0b', '#ef4444'], edgecolor='none')
        plt.title('Inventory Health Matrix', fontsize=12, fontweight='bold', pad=12)
        plt.xlabel('Status', fontsize=10)
        plt.ylabel('Items Count', fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig(chart_path, transparent=True)
        plt.close()
        has_chart = True

    context = {
        'items': processed_items,
        'has_chart': has_chart,
        'has_expired_items': has_expired_items
    }
    return render(request, 'tracker/dashboard.html', context)

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        expiry_date = request.POST.get('expiry_date')
        if name and category and expiry_date:
            GroceryItem.objects.create(name=name, category=category, expiry_date=expiry_date)
            return redirect('home')
    return render(request, 'tracker/add_item.html')

def delete_item(request, item_id):
    item = get_object_or_404(GroceryItem, id=item_id)
    item.delete()
    return redirect('home')