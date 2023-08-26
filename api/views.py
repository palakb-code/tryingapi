from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Staff
from .serializers import StaffSerializer
from django.http import JsonResponse

@api_view(['POST'])
def create_data(request):
    serializer = StaffSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_data(request):
    mydata = Staff.objects.all()
    serializer = StaffSerializer(mydata, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_staff(request, staff_id):
    try:
        staff = Staff.objects.get(id=staff_id)
        staff.delete()
    except Staff.DoesNotExist:
        return JsonResponse({"error": "Staff not found"}, status=404)
    return JsonResponse({"status": "Staff deleted successfully"}, status=200)

