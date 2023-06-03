from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"Message":"Welcome to API root"})