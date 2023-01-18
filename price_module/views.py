from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PriceModule


# Create your views here.
@api_view(['GET'])
def price_calculation(request):
    time_required = int(request.data.get("time_required",0))
    distance_travelled = int(request.data.get("distance_travelled",0))
    addition_distance = 0
    dbp_query = PriceModule.objects.get(id = 1)
    if (distance_travelled) > dbp_query.distance_in_meters:
        addition_distance = distance_travelled - dbp_query.distance_in_meters
        addition_distance = addition_distance / 1000
    dap_query = PriceModule.objects.get(id = 3)
    tbp = dap_query.tmf_under_hour if time_required <= 1 else dap_query.tmf_for_two_hour if time_required > 1 and time_required <= 2 else dap_query.tmf_for_three_hour
    total_price = (dbp_query.price + (addition_distance * dap_query.price)) * tbp
    return Response({"message": "success", "data": total_price})
