from django.urls import path

from AutoParts.store.views import cart, checkout, updateItem, process_order

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update item'),
    path('process-order/', process_order, name='process order')
]