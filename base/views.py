from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseView(APIView):
    serializer_class = None
    action_class = None

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            results = self.action_class(serializer.validated_data)
            if results.is_success():
                return Response(status=status.HTTP_200_OK, data={'results': results.serializers()})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'results': results.serializers()})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class BasePOSTView(APIView):
    serializer_class = None
    action_class = None

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            results = self.action_class(request, serializer.validated_data)
            if results.is_success():
                return Response(status=status.HTTP_200_OK, data={'results': results.serializers()})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'results': results.serializers()})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class BaseGETView(APIView):
    serializer_class = None

    def get(self, request):
        serializer = self.serializer_class(data=request.query_params)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data={'results': serializer.validated_data})
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

