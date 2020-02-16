from rest_framework.routers import DefaultRouter,SimpleRouter
from .views import DepartmentOp

deptrouter = SimpleRouter()
deptrouter.register('dept',DepartmentOp)
urlpatterns = deptrouter.urls