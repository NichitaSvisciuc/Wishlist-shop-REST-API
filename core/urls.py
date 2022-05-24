from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name = 'index'),
	path('wishlists', wishlists, name = 'wishlists'),

	path('api/api-urls/', apiUrls, name = 'api-urls'),
	path('api/display-items/', displayItems, name = 'display-items'),
	path('api/display-wishlists/', displayWhislists, name = 'display-wishlists'),
	path('api/create-wishlists/', createWishlist, name = 'create-wishlists'),
	path('api/create-item/', createItem, name = 'create-item'),
	path('api/delete-item/<pk>', deleteItem, name = 'delete-item'),
	path('api/delete-wishlist/<pk>', deleteWishlist, name = 'delete-wishlist'),
	path('api/wishlist-order-items/<pk>', wishlistOrderItems, name = 'wishlist-order-items'),
	path('api/wishlist-items/<pk>', wishlistItems, name = 'wishlist-items'),
	path('api/update-items/<pk>', updateItem, name = 'update-items'),
	path('api/update-wishlist/<pk>', updateWishlist, name = 'update-wishlist'),

	path('add-item-to-wishlist/<item_id>/<wishlists_pk>', addItemtoWishlist, name = 'add-item-to-wishlist'),
	path('remove-item-from-wishlist/<order_item_pk>/<wishlists_pk>', removeItemFromWishlist, name = 'remove-item-from-wishlist'),
]