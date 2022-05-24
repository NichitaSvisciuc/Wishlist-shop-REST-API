from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):

	name = models.CharField(max_length = 200)
	price = models.IntegerField(default = 0)
	description = models.TextField()

	numarul_de_utilizatori_ce_au_adaugat_produsul = models.IntegerField(default = 0, blank = True, null = True)

	slug = models.SlugField()

	def __str__(self):
		return f'Item name : {self.name}'


class OrderItem(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)

	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	quantity = models.IntegerField(default = 1)

	def __str__(self):
		return f'{self.quantity} of {self.item.name}'


class WishList(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)

	name = models.CharField(max_length = 200)
	items = models.ManyToManyField(OrderItem, blank=True)

	def __str__(self):
		return f"{self.user.username}'s wishlist"

	def get_total_price(self):
		total_price = 0

		for i in items.objects.all():
			total_price += i.price

		return total_price