from . import views
from django.urls import path


urlpatterns = [
    path("", views.IndexView.as_view()),
    path("tables/", views.TableView.as_view()),
    path("create_user/", views.CreateUserView.as_view()),
    path("ranking/", views.RankingView.as_view()),
    path("scan_user/", views.ScanUserView.as_view()),
    path("dashboards/", views.DashboardView.as_view()),
    path("inventory/", views.InventoryView.as_view()),
    path("gastos/", views.GastosView.as_view()),
]
