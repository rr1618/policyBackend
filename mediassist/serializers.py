from .models import Vehicle, Policy, Customer
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id','customer_gender',
                  'customer_income_group',
                  'customer_region',
                  'customer_marital_status']
        read_only_fields = ['customer_id']


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy

        fields = ['policy_id',
                  'date_of_purchase',
                  'customer_id',
                  'vehicle_segment_id',
                  'premium',
                  'bil',
                  'pip',
                  'pdl',
                  'collision',
                  'comprehensive']
        read_only_fields = ['policy_id','date_of_purchase']
        depth = 1
