from rest_framework.response import Response
from rest_framework.decorators import api_view
from .algorithm import predict


@api_view(['POST'])
def spam_or_ham(request):
    data = request.data
    res = predict(data['message'])
    ret = { 'messaage': data['message'], 'class': res }
    return Response(ret)