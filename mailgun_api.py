import requests


class MailgunApi:
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url = url

    def list_templates(self):
        url = f"{self.url}/templates?limit=100"
        return requests.get(url, auth=('api', self.api_key))

    def get_template_versions(self, name):
        url = f"{self.url}/templates/{name}/versions"
        response = requests.get(url, auth=('api', self.api_key)).json()
        return response["template"]["versions"]

    def get_template_version(self, template_name, tag):
        url = f"{self.url}/templates/{template_name}/versions/{tag}"
        response = requests.get(url, auth=('api', self.api_key)).json()
        return response["template"]["version"]

    def create_template(self, name, description):
        url = f"{self.url}/templates"
        data = {
            'name': name,
            'description': description
        }
        requests.post(url, auth=('api', self.api_key), data=data)

    def create_version(self, template_name, version):
        url = f"{self.url}/templates/{template_name}/versions"
        data = {
            'engine': version["engine"],
            'template': version["template"],
            'tag': version["tag"]
        }
        requests.post(url, auth=('api', self.api_key), data=data)

    def delete_all_templates(self):
        url = f"{self.url}/templates"
        response = requests.delete(url, auth=('api', self.api_key)).json()
        print(response)
