from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, CustomUserCreate, LoginPage, UserListView, UserDetailView, CustomerListView, CustomerDetailView, CustomerCreateView, BakerListView, BakerDetailView, BakerCreateView, ProductListView,  ProductDetailView,  ProductCreateView, ProductFormListView,  ProductFormDetailView,  ProductFormCreateView, ProductStuffListView,  ProductStuffDetailView,  ProductStuffCreateView, ProductToppingListView,  ProductToppingDetailView,  ProductToppingCreateView, OrderListView, OrderDetailView, OrderCreateView, CatalogListView, CatalogDetailView, CatalogCreateView, ReviewListView, ReviewDetailView, ReviewCreateView, Test, ImageModelListView, ImageModelCreateView

urlpatterns = [
	path('users/create/', CustomUserCreate.as_view(), name="create_user"),
	path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
	path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
	path('login/', LoginPage.as_view(), name='login_page'),
	path('users/', UserListView.as_view()),
	path('users/<int:pk>/', UserDetailView.as_view()),

	path('users/customers', CustomerListView.as_view()),
	path('users/customers/<int:pk>', CustomerDetailView.as_view()),
	path('users/customers/create', CustomerCreateView.as_view()),

	path('users/bakers', BakerListView.as_view()),
	path('users/bakers/<int:pk>', BakerDetailView.as_view()),
	path('users/bakers/create', BakerCreateView.as_view()),

	path('products/', ProductListView.as_view()),
	path('products/<int:pk>', ProductDetailView.as_view()),
	path('products/create', ProductCreateView.as_view()),

	path('product/forms/', ProductFormListView.as_view()),
	path('product/forms/<int:pk>', ProductFormDetailView.as_view()),
	path('product/forms/create', ProductFormCreateView.as_view()),

	path('product/stuff/', ProductStuffListView.as_view()),
	path('product/stuff/<int:pk>', ProductStuffDetailView.as_view()),
	path('product/stuff/create', ProductStuffCreateView.as_view()),

	path('product/topping/', ProductToppingListView.as_view()),
	path('product/topping/<int:pk>', ProductToppingDetailView.as_view()),
	path('product/topping/create', ProductToppingCreateView.as_view()),

	path('orders', OrderListView.as_view()),
	path('orders/<int:pk>', OrderDetailView.as_view()),
	path('orders/create', OrderCreateView.as_view()),

	path('catalog', CatalogListView.as_view()),
	path('catalog/<int:pk>', CatalogDetailView.as_view()),
	path('catalog/create', CatalogCreateView.as_view()),

	path('review', ReviewListView.as_view()),
	path('review/<int:pk>', ReviewDetailView.as_view()),
	path('review/create', ReviewCreateView.as_view()), 

	path('userpassport/', Test.as_view()),
	path('imagepassport/', ImageModelListView.as_view()),
	path('imagepassport/create', ImageModelCreateView.as_view()),
]