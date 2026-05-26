import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json

from .models import Measurement


def check_variable(variable_id):
    try:
        url = f"{settings.PATH_VAR}/variables/{variable_id}/"
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def measurements(request):
    if request.method == 'GET':
        variable_id = request.GET.get('variable', None)
        if variable_id:
            all_measurements = Measurement.objects.filter(variable=variable_id)
        else:
            all_measurements = Measurement.objects.all()
        data = serialize('json', all_measurements)
        return JsonResponse(json.loads(data), safe=False, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def create_measurement(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except (json.JSONDecodeError, TypeError):
            body = request.POST.dict()
        variable_id = body.get('variable')
        value = body.get('value')
        unit = body.get('unit')
        place = body.get('place')
        if not all([variable_id, value, unit]):
            return JsonResponse({'error': 'Campos requeridos: variable, value, unit'}, status=400)
        if not check_variable(variable_id):
            return JsonResponse({'error': f'Variable con id={variable_id} no encontrada'}, status=404)
        measurement = Measurement(
            variable=variable_id,
            value=float(value),
            unit=unit,
            place=place or '',
        )
        measurement.save()
        return JsonResponse({'message': 'Measurement created', 'id': measurement.id}, status=201)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
