from .views import DepartmentOp
from rest_framework.routers import DefaultRouter,SimpleRouter

deptrouter = SimpleRouter()
deptrouter.register("dept",DepartmentOp)
urlpatterns = deptrouter.urls