from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from registry.models import Registry
from registry.serializers import RegistrySerializer

# Create your views here.
@csrf_exempt
def registry_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        registry = Registry.objects.all()
        serializer = RegistrySerializer(registry, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def registry_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Registry.objects.get(pk=pk)
    except Registry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RegistrySerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegistrySerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



