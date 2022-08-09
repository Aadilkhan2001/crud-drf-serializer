from django.urls import path
from .views import indexview,AddRetriveEmployee,UpdateDeleteView

urlpatterns=[
    path('',indexview),
    path('addretrieve/',AddRetriveEmployee),
    path('updatedelete/<int:id>',UpdateDeleteView)
]


