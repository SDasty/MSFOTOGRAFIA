from django.contrib import admin
from .models import Movie, Review, CarouselImage

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(CarouselImage)