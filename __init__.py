import requests

API_KEY = ""
HOSTNAME = ""
SESSION = ""

class Cpanel():
    def __init__(self):
        self.username = "iouygq"
        self.auth_header = {"Authorization":"whm root:%s" % (API_KEY)}
        self.BASE_URL = 'https://%s:2087/%s/json-api/' % (HOSTNAME, SESSION)

    def add_pop(self, new_user, domain, new_pass, cpanel_user):
        url = self.BASE_URL + ''.join(['cpanel?cpanel_jsonapi_user=%s' % cpanel_user,
                                       '&cpanel_jsonapi_apiversion=2',
                                       '&cpanel_jsonapi_module=Email',
                                       '&cpanel_jsonapi_func=addpop',
                                       '&domain=%s' % domain,
                                       '&email=%s' % new_user,
                                       '&password=%s' % new_pass,
                                       '&quota=500'])

        with requests.get(url, headers=self.auth_header) as s:
            print(s.text)

    def add_domain_forward(self, domain, cpanel_user, dest_domain):
        url = self.BASE_URL + ''.join(['cpanel?cpanel_jsonapi_user=%s' % cpanel_user,
                                       '&cpanel_jsonapi_apiversion=2',
                                       '&cpanel_jsonapi_module=Email',
                                       '&cpanel_jsonapi_func=adddomainforward',
                                       '&domain=%s' % domain,
                                       '&destdomain=%s' % dest_domain,
                                       ])
        with requests.get(url, headers=self.auth_header) as s:
            print(s.text)

    def add_mailbox_forward(self, domain, email, forward_email, user):
        url = self.BASE_URL + ''.join(['cpanel?cpanel_jsonapi_user=%s' % user,
                                       '&cpanel_jsonapi_apiversion=2',
                                       '&cpanel_jsonapi_module=Email',
                                       '&cpanel_jsonapi_func=addforward&domain=%s' % domain,
                                       '&email=%s' % email,
                                       '&fwdopt=fwd',
                                       '&fwdemail=%s' % forward_email,
                                       ])
        with requests.get(url, headers=self.auth_header) as s:
            print(s.text)


