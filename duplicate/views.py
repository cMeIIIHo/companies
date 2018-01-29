import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render


@csrf_exempt
def index(request):
    return render(request, 'duplicate/index.html')


@csrf_exempt
def get_duplicates(request):
    access_token = request.POST['access_token']
    domain = request.POST['domain']
    method = 'crm.company.list'
    url = 'https://%s/rest/%s.json?auth=%s' % (domain, method, access_token)
    r = requests.post(url=url)
    companies = r.json()['result']
    company_names = {}
    for company in companies:
        company_names[company['TITLE']] = company_names.get(company['TITLE'], [])
        company_names[company['TITLE']].append(company['ID'])
    duplicates = [{'name': name, 'ids': ids} for name, ids in company_names.items() if len(ids) > 1]
    return JsonResponse(duplicates, safe=False)
