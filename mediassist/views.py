from .models import Customer, Policy, Vehicle
from .serializers import CustomerSerializer, PolicySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import viewsets, serializers
from django.core import serializers
from django.http import JsonResponse


# Api to get the customers using customer id and update the customer object using the corresponding id
@api_view(['GET', 'PUT'])
def customer(request, customer_id):
    # checking the Http request
    if request.method == 'GET':
        # extracting the tuple related to the customer_id
        try:
            res = Customer.objects.get(customer_id=customer_id)
        except:
            return Response({'Error':'No Customer found for the given id'}, status=404)
        # serializing the tuple before sending to the client side
        serializer = CustomerSerializer(res, many=False)
        return Response(serializer.data)
    if request.method == 'PUT':
        # serializing the data received from the client
        data = CustomerSerializer(data=request.data['cust'],context={'request':request})
        # extracting the tuple which has to be upddated
        cust = Customer.objects.get(customer_id=customer_id)
        # checking if the data provided from the client is valid to be updated in the server
        if data.is_valid(raise_exception=True):
            data.update(cust,data.validated_data)
            return Response(data.validated_data)
    return Response({'message': 'wrong method'},status=500)

# Function which return the policy based either policy id or customer id
@api_view(['GET', 'PUT'])
def policySearch(request):
    # getting the parameters received from the client
    params = request.query_params
    # checking the Http request
    if request.method =='GET':
        # if the search parameter has the policy , search will take place on policy id
        if params['search'] == 'policy':
            try:
                # extracting the pol with reference to policy id in params
                pol = Policy.objects.get(policy_id__exact=params['id'])
                serializer = PolicySerializer(pol, many=False, context={'request': request})
            except:
                return Response({'error': 'No Policies Found'},status=400)
            return Response(serializer.data)
        # if the search parameter has the customer , search will take place on customer id
        elif params['search'] == 'customer':
            try:
                # extracting the policy/ policies with reference to policy id in params
                pols = Policy.objects.filter(customer_id=params['id'])
                serializer = PolicySerializer(pols, many=True)
            except:
                return Response({'error': 'No Policies Found'}, status=400)
            return Response(serializer.data)
        else:
            return Response({"message": "No results Found"}, status=400)


# This function helps in updating the policies details
@api_view(['PUT'])
def policy(request, policy_id):
    # checking the http request
    print("entered")
    if request.method == 'PUT':
        data = request.data
        print(data)
        try:
            # making changes in the vehicle model if it has been modified from client
            vechicle_id = Vehicle.objects.get(vehicle_segment=data['segment'])
            vechicle_id.fuel = data['fuel']
            vechicle_id.save()
        except:
            # if the vehicle segment and fuel combination doesn't exist, then creating a new one
            v =Vehicle(vehicle_segment=data['segment'],fuel=data['fuel'])
            v.save()
        #     validating the other policy parameters
        data = PolicySerializer(data=request.data['policy'], context={'request': request})
        policy = Policy.objects.get(policy_id=policy_id)
        # checking if the data sent for modification from the client is valid or not
        if data.is_valid(raise_exception=True):
            data.update(policy,data.validated_data)
            return Response(data.validated_data,status=201)
    return Response({'message':'fail'}, status=400)


# function which returns the data for chart preparation based on the region
@api_view(['GET'])
def chart(request, region):
    chartData= [["Policies", "Month"]]
    count = 0
    for i in range(1,13):
        pols = Policy.objects.filter(customer_id__customer_region=region,
                                     date_of_purchase__month=i)
        count += pols.count()
        chartData.append([i,pols.count()])
    return Response({'chart':chartData,'count':count})
