from django.urls import path, re_path,include

from rest_framework import routers
from . import views

# Api Endpoints

router = routers.DefaultRouter()
router.register(r'cust',views.CustomerViewSet,basename='customer')
router.register(r'pol',views.PolicyViewSet,basename='policy')


urlpatterns = [

    # to list all the customers
    path('customers/', views.customer, name='customer'),
    # return tuple of customer with <customer_id>
    path('customer/<int:customer_id>', views.customer, name='customer2'),
    # returns policy corresponding with <policy_id>
    path('policysearch/', views.policySearch, name='policy'),
    # update the policy details with reference to specific policy_id
    path('policy/<int:policy_id>', views.policy, name='policy-update'),
    # returns the chart parameters
    path('chart/<str:region>', views.chart, name='chart'),
    # path('router/',include((router.urls,'mediAssist')))
    path('', include(router.urls)),

]

