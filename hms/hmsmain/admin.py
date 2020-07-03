from django.contrib import admin
from .models import MyUser,Medicine,Order,orderDetail,Consumption,consumptionDetail
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(orderDetail)
admin.site.register(Consumption)
admin.site.register(consumptionDetail)
