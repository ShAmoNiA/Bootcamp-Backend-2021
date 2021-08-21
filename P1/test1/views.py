from django.http.request import HttpRequest
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.core.cache import cache


def factorial_view(request: HttpRequest):
    if request.method == "GET":
        value = request.GET.get("number", 6)
        try:
            int(value)
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()
        cached_value = cache.get(value)
        if cached_value is not None:
            response = cached_value
        else:
            response = 1
            for i in range(1, int(value)+1):
                response *= i
        json_object = {
            "result": response
        }
        cache.set(value, response)
        return JsonResponse(json_object)
