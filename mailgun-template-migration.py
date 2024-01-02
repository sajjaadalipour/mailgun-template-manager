import requests

api_key = "API_KEY"
from_url = 'SOURCE_DOMAIN_URL'
to_url = 'DESTINATION_DOMAIN_URL'

def list_templates():
    url = f"{from_url}/templates?limit=100"
    return requests.get(url,  auth=('api', api_key))

def get_template_versions(name):
    url = f"{from_url}/templates/{name}/versions"
    response = requests.get(url,  auth=('api', api_key)).json()
    return response["template"]["versions"]

def get_template_version(template_name,tag):
    url = f"{from_url}/templates/{template_name}/versions/{tag}"
    response = requests.get(url,  auth=('api', api_key)).json()
    return response["template"]["version"]

def create_template(name,description):
    url = f"{to_url}/templates"
    data = {
        'name': name,
        'description': description
    }
    response = requests.post(url,  auth=('api', api_key),data=data).json()

def crete_version(template_name,version):
    url = f"{to_url}/templates/{template_name}/versions"
    data = {
        'engin': version["engine"],
        'template': version["template"],
        'tag': version["tag"]
    }
    response = requests.post(url,  auth=('api', api_key),data=data)

def delete_all_templates(url):
    url = f"{url}/templates"
    response = requests.delete(url,  auth=('api', api_key)).json()
    print(response)

def copy_template(template):
    template_name = template["name"]
    create_template(template_name,template["description"])
    versions = get_template_versions(template_name)
    for version in versions:
        template_version_detail = get_template_version(template_name,version["tag"])
        crete_version(template_name,template_version_detail)
    print(f"Template {template_name} done \n")

templates_response=list_templates()

if templates_response.status_code == 200:
    templates = templates_response.json()["items"]
    for template in templates:
        copy_template(template)
else:
    print("Error fetching templates from source domain.")
