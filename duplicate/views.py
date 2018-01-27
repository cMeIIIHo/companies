import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt


domain = "tropa.bitrix24.ru"
url = f"https://{domain}/rest/crm.company.list.json"


@xframe_options_exempt
@csrf_exempt
def show_duplicates(request):
    # access_token = request.POST['access_token']
    # params = {'auth': access_token}
    # r = requests.get(url=url, params=params)
    # companies = r.json()['result']
    # company_names = {}
    # for company in companies:
    #     company_names[company['TITLE']] = company_names.get(company['TITLE'], [])
    #     company_names[company['TITLE']].append(company['ID'])
    # duplicates = {name: identifiers for name, identifiers in company_names.items() if len(identifiers) > 1}
    return JsonResponse({'a': 1})
