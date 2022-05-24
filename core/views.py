from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


def index(request):
	return render(request, 'index.html')


def wishlists(request):
	return render(request, 'wishlists.html')


def removeItemFromWishlist(request, order_item_pk, wishlists_pk):

	item = Item.objects.get(id = order_item_pk)
	order_item = OrderItem.objects.get(item = item, user = request.user)

	wishlist = WishList.objects.get(id = wishlists_pk)

	wishlist.items.remove(order_item)
	order_item.delete()

	return redirect(request.META['HTTP_REFERER'])


def addItemtoWishlist(request, item_id, wishlists_pk):

	item = Item.objects.get(id = item_id)

	order_item, created = OrderItem.objects.get_or_create(item = item, user = request.user)
	wishlist = WishList.objects.get(id = wishlists_pk)

	if created:
		wishlist.items.add(order_item)

		return redirect(request.META['HTTP_REFERER'])

	order_item.quantity += 1
	order_item.save()

	return redirect(request.META['HTTP_REFERER'])


@api_view(['GET'])
def apiUrls(request):

	api_urls = {
		'Create a wishlist' : '127.0.0.1:8000/api/create-wishlist',
		'Delete a wishlist' : '127.0.0.1:8000/api/delete-wishlist/<slug>',

		'Display items' : '127.0.0.1:8000/api/display-items',
		'Display wishlists' : '127.0.0.1:8000/api/display-wishlists',
	}

	return Response(api_urls)


@api_view(['POST'])
def updateItem(request, pk):

	item = Item.objects.get(id = pk)

	serializer = ItemSerializer(instance = item, data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def updateWishlist(request, pk):

	wishlist = Wishlist.objects.get(id = pk)

	serializer = WhishListSerializer(instance = wishlist, data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['GET'])
def displayItems(request):

	items = Item.objects.all()
	serializer = ItemSerializer(items, many = True)

	return Response(serializer.data)


@api_view(['GET'])
def displayWhislists(request):

	wishlists = WishList.objects.filter(user = request.user)
	serializer = WhishListSerializer(wishlists, many = True)

	return Response(serializer.data)


@api_view(['POST'])
def createWishlist(request):

	serializer = WhishListSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def createItem(request):

	serializer = ItemSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def deleteItem(request, pk):

	item = Item.objects.get(id = pk)
	item.delete()

	return Response('Item successfully deleted')


@api_view(['GET'])
def wishlistOrderItems(request, pk):

	wish_list = WishList.objects.get(id = pk)
	items = wish_list.items.all()

	serializer = OrderItemSerializer(items, many = True)

	return Response(serializer.data)


@api_view(['GET'])
def wishlistItems(request, pk):

	item = Item.objects.get(id = pk)

	serializer = ItemSerializer(item, many = False)

	return Response(serializer.data)


@api_view(['DELETE'])
def deleteWishlist(request, pk):

	wish_list = WishList.objects.get(id = pk)
	wish_list.delete()

	return Response('Wishlist successfully deleted')