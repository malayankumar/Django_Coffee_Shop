from django.urls import path
from .views import HomeView, AboutView, AddProduct, ProductDetails,UpdateProduct, DeleteProduct, SearchView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about", AboutView.as_view(), name="aboutpage"),
    
    path("products/add", AddProduct.as_view(), name="addproduct"),
    path("products/<int:pk>", ProductDetails.as_view(), name="prod_details"),
    path("products/edit/<int:pk>", UpdateProduct.as_view(), name="editproduct"),
    path("products/del/<int:pk>", DeleteProduct.as_view(), name="delproduct"),
    
    path("products/search", SearchView.as_view(), name="search"),
]
