from django.shortcuts import render
from django.views.generic import TemplateView # MIRA EL CAMEL CASE 
# Create your views here.
class IndexView(TemplateView):
    template_name = "App/index.html"
    
# TABLAS 
class TableView(TemplateView):
    template_name = "App/tables.html"
    
# CREAR USUARIO   
class CreateUserView(TemplateView):
    template_name = "App/create_user.html"
    
    
# RANKING
class RankingView(TemplateView):
    template_name = "App/ranking.html"
    
# SCAN USER

class ScanUserView(TemplateView):
    template_name = "App/scan_user.html"
    
    
# DASHBOARDS
class DashboardView(TemplateView):
    template_name = "App/dashboards.html"
    
class InventoryView(TemplateView):
    template_name = "App/inventory.html"
    
class GastosView(TemplateView):
    template_name = "App/gastos.html"