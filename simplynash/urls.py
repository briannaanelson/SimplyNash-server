from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from simplynashapi.views import register_user, login_user
from rest_framework import routers
from simplynashapi.views.ambiance import AmbianceTypeView
from simplynashapi.views.food_type import FoodTypeView
from simplynashapi.views.price import PriceTypeView
from simplynashapi.views.rating import RatingTypeView
from simplynashapi.views.restaurant_post import RestaurantPostView
from simplynashapi.views.review import ReviewView
from simplynashapi.views.category import CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'ambiance', AmbianceTypeView, 'ambiance')
router.register(r'categories',CategoryView, 'category' )
router.register(r'foodtypes', FoodTypeView, 'foodtype')
router.register(r'prices', PriceTypeView, 'price')
router.register(r'ratings', RatingTypeView, 'rating')
router.register(r'restaurantposts', RestaurantPostView, 'restaurantpost')
router.register(r'reviews', ReviewView, 'review')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]