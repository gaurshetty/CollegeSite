from rest_framework.routers import SimpleRouter
from .views import StudentOperations
simple_router = SimpleRouter()
simple_router.register("student", StudentOperations)
urlpatterns = simple_router.urls
