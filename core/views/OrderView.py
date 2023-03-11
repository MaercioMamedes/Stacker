from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey


class OrderView(APIView):

    def get(self, request):
        key = self.request.GET['api_key']
        try:
            api_key = APIKey.objects.get_from_key(key)
            return Response(api_key.name)

        except APIKey.DoesNotExist as err:
            print(str(err))
            return Response(
                {
                    'msg': str(err)
                },
                status=401)

