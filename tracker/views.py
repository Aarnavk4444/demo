from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import GroceryItem

def calculate_status(expiry_date):
    """
    Computes viability and status color based on remaining shelf-life days.
    """
    today = datetime.now().date()
    days_left = (expiry_date - today).days

    if days_left < 0:
        return "Expired", "#f43f5e"
    elif days_left <= 3:
        return "Expiring Soon", "#fbbf24"
    else:
        return "Fresh", "#10b981"

def dashboard(request):
    """
    Primary dashboard view for KitchenSync Pro Enterprise Telemetry Suite.
    Aggregates financial metrics in NPR, tracks expired assets, and organizes data grids.
    """
    db_items = GroceryItem.objects.all().order_by('expiry_date')
    processed_items = []
    expired_items_list = []
    
    total_inventory_value = 0.0
    potential_waste_loss = 0.0
    total_count = len(db_items)
    fresh_count = 0

    # Aggregators for dynamic Chart.js graphing
    status_counts = {'Fresh': 0, 'Expiring Soon': 0, 'Expired': 0}
    category_values = {}

    for item in db_items:
        status, color = calculate_status(item.expiry_date)
        item_price = float(item.price)
        total_inventory_value += item_price

        if status in status_counts:
            status_counts[status] += 1

        if item.category in category_values:
            category_values[item.category] += item_price
        else:
            category_values[item.category] = item_price

        if status == "Expired":
            potential_waste_loss += item_price
            expired_items_list.append({
                'id': item.id,
                'name': item.name,
                'category': item.category,
                'price': f"{item_price:,.2f}",
                'expiry_date': item.expiry_date.strftime('%Y-%m-%d')
            })
        elif status == "Fresh":
            fresh_count += 1

        processed_items.append({
            'id': item.id,
            'name': item.name,
            'category': item.category,
            'price': f"{item_price:,.2f}",
            'expiry_date': item.expiry_date.strftime('%Y-%m-%d'),
            'status': status,
            'color': color
        })

    health_ratio = int((fresh_count / total_count) * 100) if total_count > 0 else 100

    context = {
        'items': processed_items,
        'expired_items_list': expired_items_list,
        'total_inventory_value': f"{total_inventory_value:,.2f}",
        'potential_waste_loss': f"{potential_waste_loss:,.2f}",
        'health_ratio': health_ratio,
        'status_labels': list(status_counts.keys()),
        'status_data': list(status_counts.values()),
        'cat_labels': list(category_values.keys()),
        'cat_data': list(category_values.values()),
    }
    return render(request, 'tracker/dashboard.html', context)

def financial_metrics_view(request):
    """
    Dedicated high-precision financial analytics page showing advanced calculators,
    depreciation schedules, waste leakage analytics, and portfolio valuation metrics in NPR.
    """
    db_items = GroceryItem.objects.all()
    
    total_val = 0.0
    waste_val = 0.0
    category_breakdown = {}

    for item in db_items:
        status, _ = calculate_status(item.expiry_date)
        price = float(item.price)
        total_val += price
        
        if status == "Expired":
            waste_val += price

        category_breakdown[item.category] = category_breakdown.get(item.category, 0.0) + price

    net_active_capital = total_val - waste_val
    waste_percentage = (waste_val / total_val * 100) if total_val > 0 else 0.0

    context = {
        'total_inventory_value': f"{total_val:,.2f}",
        'potential_waste_loss': f"{waste_val:,.2f}",
        'net_active_capital': f"{net_active_capital:,.2f}",
        'waste_percentage': f"{waste_percentage:.1f}",
        'total_items_count': len(db_items),
    }
    return render(request, 'tracker/financial_metrics.html', context)

def add_item(request):
    """
    Handles secure ingestion of new items into the local inventory database.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price', 0.00)
        expiry_date = request.POST.get('expiry_date')
        if name and category and expiry_date:
            GroceryItem.objects.create(name=name, category=category, price=price, expiry_date=expiry_date)
            return redirect('home')
    return render(request, 'tracker/add_item.html')

def delete_item(request, item_id):
    """
    Removes specified inventory entry from the persistent database record.
    """
    item = get_object_or_404(GroceryItem, id=item_id)
    item.delete()
    return redirect('home')