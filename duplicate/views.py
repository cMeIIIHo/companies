import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import urllib.request
import json

# domain = "tropa.bitrix24.ru"
# url = f"https://{domain}/rest/crm.company.list.json"

domain = "tropa.bitrix24.ru"


# @xframe_options_exempt
# @csrf_exempt
# def show_duplicates(request):
#     access_token = request.POST['access_token']
#     r = urllib.request.urlopen('https://tropa.bitrix24.ru/rest/crm.company.list.json?auth='+ access_token)
#     # companies = r.json()['result']
#     # company_names = {}
#     # for company in companies:
#     #     company_names[company['TITLE']] = company_names.get(company['TITLE'], [])
#     #     company_names[company['TITLE']].append(company['ID'])
#     # duplicates = {name: identifiers for name, identifiers in company_names.items() if len(identifiers) > 1}
#
#     return HttpResponse(r.read())


@xframe_options_exempt
@csrf_exempt
def show_duplicates(request):
    # access_token = request.POST['access_token']
    # domain = request.POST['domain']
    access_token = 'axibr3qn4uas1hodp8clcg4rq7m06gjt'
    domain = "tropa.bitrix24.ru"
    # data = {'select': ['ID', 'TITLE']}
    method = 'crm.company.list'
    url = 'https://%s/rest/%s.json?auth=%s' % (domain, method, access_token)
    r = requests.post(url=url)
    companies = r.json()['result']
    # print(companies)
    company_names = {}
    for company in companies:
        company_names[company['TITLE']] = company_names.get(company['TITLE'], [])
        company_names[company['TITLE']].append(company['ID'])
    duplicates = {name: identifiers for name, identifiers in company_names.items() if len(identifiers) > 1}
    return JsonResponse(duplicates)
