from django.urls import path
from app import views

urlpatterns = [
    path('leaverequest/',views.EmployeeLeaveRequest.as_view(),name='applyleave'),
    path('leaverequestapproval/<int:pk>/',views.EmployeeLeaveApproval.as_view(),name='leaverequestapproval'),
    path('leaverequestrejection/<int:pk>/',views.EmployeeLeaveRejection.as_view(),name='leaverequestrejection'),
    path('leaverequestsview/',views.EmployeeLeaveStatus.as_view(),name='leaverequestsview'),
]
