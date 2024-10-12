from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import RequestDemoSerializer, ContactUsSerializer
import requests


class RequestDemoAPIView(APIView):
    serializer_class = RequestDemoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            demo_request = serializer.save()

            endpoint_configs = EndPointSendRequestDemo.objects.all()

            if endpoint_configs.exists():
                for endpoint_config in endpoint_configs:
                    try:
                        data_to_send = {}

                        if endpoint_config.full_name:
                            data_to_send['full_name'] = demo_request.full_name
                        if endpoint_config.email:
                            data_to_send['email'] = demo_request.email
                        if endpoint_config.phone_number:
                            data_to_send['phone_number'] = demo_request.phone_number
                        if endpoint_config.company_name:
                            data_to_send['company_name'] = demo_request.company_name
                        if endpoint_config.message:
                            data_to_send['message'] = demo_request.message
                        if endpoint_config.module_name:
                            data_to_send['module_name'] = demo_request.module_name
                        if endpoint_config.requested_at:
                            data_to_send['requested_at'] = demo_request.requested_at.isoformat()

                        print(data_to_send)
                        response = requests.post(endpoint_config.request_link, json=data_to_send)

                        if response.status_code != 200:
                            LogTicket.objects.create(status_code=response.status_code, request_body=data_to_send, response=response.text, exception='')
                    except Exception as e:
                        LogTicket.objects.create(exception=e)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ContactUsAPIView(APIView):
    serializer_class = ContactUsSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            contact = serializer.save()
            endpoint_configs = EndPointSendContactUs.objects.all()
            if endpoint_configs.exists():
                for endpoint_config in endpoint_configs:
                    try:
                        data_to_send = {}

                        if endpoint_config.full_name:
                            data_to_send['full_name'] = contact.full_name
                        if endpoint_config.email:
                            data_to_send['email'] = contact.email
                        if endpoint_config.subject:
                            data_to_send['subject'] = contact.subject
                        if endpoint_config.message:
                            data_to_send['message'] = contact.message
                        if endpoint_config.contacted_at:
                            data_to_send['contacted_at'] = contact.contacted_at.isoformat()
                        print(data_to_send)
                        response = requests.post(endpoint_config.request_link, json=data_to_send)
                        if response.status_code != 200:
                            LogTicket.objects.create(status_code=response.status_code, request_body=data_to_send,
                                                      response=response.text, exception='')
                    except Exception as e:
                        LogTicket.objects.create(exception=e)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)