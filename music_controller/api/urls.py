from django.urls import path 
from .views import RoomViewSet, AppUserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
# router.register("room", RoomViewSet, basename="room")
router.register("user", AppUserViewSet, basename="user")

urlpatterns = router.urls