from django.urls import path

from employdata.views import AddNew, deleteEmploye, detail, details, docs, updateEmploye, homePage

urlpatterns = [
    path('',homePage),
    path('docs/',docs),
    path('details/',details),
    path('detail/<str:pk>/',detail),
    path('AddNew/', AddNew ),
    path('update/<str:pk>',updateEmploye),
    path('delete/<str:pk>',deleteEmploye)
]