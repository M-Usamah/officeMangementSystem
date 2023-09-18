from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializes import EmployDetailsSerializer
from .models import EmployDetails
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def docs(request):
    routes = [
        {
            'Endpoint':'/employ/details',
            'method':'GET',
            'body':'None',
            'discription':'Returns all the data of the Employies '
        },
        {
            'Endpoint':'/employ/detail/<id>',
            'method':'GET',
            'body':'None',
            'discription':'Returns the data of the Employ'
        },
        {
            'Endpoint':'/employ/AddNew',
            'method':'POST',
            'body':'None',
            'discription':'Add a new employ'
        },
        {
            'Endpoint':'/employ/update/<id>',
            'method':'PUT',
            'body':'None',
            'discription':'Returns the data of the Employ'
        },
        {
            'Endpoint':'/employ/delete/<id>',
            'method':'DELETE',
            'body':'None',
            'discription':'Delete the employ from the table'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def details(request):
    details  = EmployDetails.objects.all()
    serializer = EmployDetailsSerializer(details,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request,pk):
    details  = EmployDetails.objects.get(id=pk)
    serializer = EmployDetailsSerializer(details,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddNew(request):
    data = request.data
    employ = EmployDetails.objects.create(
        first_name=data['first_name'],
        middle_name=data.get('middle_name', ''),  # Use get to handle optional field
        last_name=data['last_name'],
        age=data['age']
    )

    serializer = EmployDetailsSerializer(employ,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateEmploye(request, pk):
    employ = EmployDetails.objects.get(id=pk)
    serializer = EmployDetailsSerializer(employ, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteEmploye(requesr,pk):
    employ = EmployDetails.objects.get(id=pk)
    employ.delete()
    return Response("Employ data has been Deleted")