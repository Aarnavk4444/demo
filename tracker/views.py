import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.shortcuts import redirect, render
from .utils import calculate_status, load_items, save_items

def dashboard(request):
  items = load_items()
  processed_items = []
  has_expired_items = False

  for item in items:
    status, color = calculate_status(item['expiry_date'])
    processed_items.append({
        'name': item['name'],
        'category': item['category'],
        'expiry_date': item['expiry_date'],
        'status': status,
        'color': color,
    })
    if status == 'Expired':
      has_expired_items = True

  # --- Matplotlib Chart Generation ---
  chart_dir = os.path.join(
      os.path.dirname(__file__), 'static', 'tracker', 'images'
  )
  os.makedirs(chart_dir, exist_ok=True)
  chart_path = os.path.join(chart_dir, 'expiry_chart.png')

  # Always define has_chart first as False
  has_chart = False

  if processed_items:
    df = pd.DataFrame(processed_items)
    status_counts = df['status'].value_counts()

    plt.figure(figsize=(5, 4))
    status_counts.plot(
        kind='bar', color=['#10b981', '#f59e0b', '#ef4444'], edgecolor='black'
    )
    plt.title('Expiry Status Breakdown')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    has_chart = True  # Set to True only if chart is created successfully

  context = {
      'items': processed_items,
      'has_chart': has_chart,
      'has_expired_items': has_expired_items,
  }
  return render(request, 'tracker/dashboard.html', context)
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        expiry_date = request.POST.get('expiry_date')
        if name and category and expiry_date:
            items = load_items()
            items.append({'name': name, 'category': category, 'expiry_date': expiry_date})
            save_items(items)
            return redirect('home')
    return render(request, 'tracker/add_item.html')