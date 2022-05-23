from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Employeeleave

from app.serializers import EmployeeleaveSerializer
# Create your views here.


# ENDPOINT purely for employee leave request
class EmployeeLeaveRequest(APIView):
    # POST request endpoint to apply for leave
    def post(self, request):
        if request.user.is_employee:
            data = request.data
            data['leave_applied_by'] = request.user.id
            serializer = EmployeeleaveSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Leave Applied Successfully'},status=201)
            return Response(serializer.errors,status=400)
        return Response({'message': 'User Not Allowed'},status=403)
    
    # GET request endpoint to allow employee to view his leave request
    def get(self, request):
        if request.user.is_employee:
            data = Employeeleave.objects.filter(leave_applied_by=request.user)
            serializer = EmployeeleaveSerializer(data,many=True)
            return Response(serializer.data,status=200)
        return Response({'message': 'User Not Allowed'},status=403)
    
# ENDPOINT purely for admin to approve leave request
class EmployeeLeaveApproval(APIView):
    # PUT request endpoint to approve leave request
    def patch(self, request, pk):
        if request.user.is_admin:
            try:
                employee = Employeeleave.objects.get(id=pk)
                data = request.data
                data['leave_approved_by'] = request.user.id
                data['leave_status'] = 'APPROVED'
                serializer = EmployeeleaveSerializer(employee,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'Leave Approved Successfully'},status=201)
                return Response(serializer.errors,status=400)
            except Employeeleave.DoesNotExist:
                return Response({'message': 'Leave Request Not Found'},status=404)
            except Exception as e:
                return Response({'message': 'Something went wrong'},status=500)
        return Response({'message': 'User Not Allowed'},status=403)
    

# ENDPOINT purely for admin to reject leave request
class EmployeeLeaveRejection(APIView):
    # PUT request endpoint to request leave request
    def patch(self, request, pk):
        if request.user.is_admin:
            try:
                employee = Employeeleave.objects.get(id=pk)
                data = request.data
                data['leave_status'] = 'REJECTED'
                serializer = EmployeeleaveSerializer(employee,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'Leave Rejected Successfully'},status=201)
                return Response(serializer.errors,status=400)
            except Employeeleave.DoesNotExist:
                return Response({'message': 'Leave Request Not Found'},status=404)
            except Exception as e:
                return Response({'message': 'Something went wrong'},status=500)
        return Response({'message': 'User Not Allowed'},status=403)

class EmployeeLeaveStatus(APIView):
    # GET request endpoint to allow admin to view all leave requests
    def get(self, request):
        if request.user.is_admin:
            data = Employeeleave.objects.all()
            serializer = EmployeeleaveSerializer(data,many=True)
            return Response(serializer.data,status=200)
        return Response({'message': 'User Not Allowed'},status=403)