from DjangoProject1.urls import path
from .import views

urlpatterns=[
    path('', views.index, name='index'),

    path('characters/',views.character_list,name='character_list'),
    path('weapons/', views.weapon_list, name='weapon_list'),
    path('items/', views.item_list, name='item_list'),
    path('skills/', views.skill_list, name='skill_list'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
    path('classes/', views.class_list, name='class_list'),
    path('classes/<int:pk>/', views.class_detail, name='class_detail'),

    #path('<int:characters_id>',views.detail,name='movies_detail'),
]
