from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey


class OrderView(APIView):
    permission_classes = [HasAPIKey]

    def get(self):
        print('ola mundo')
        return Response("Olá mundo")
