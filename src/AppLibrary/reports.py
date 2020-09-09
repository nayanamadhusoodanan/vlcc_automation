import json
import os
import requests
import platform

class Reports:

    def __init__(self):
      with open('appconfig.json') as f:
        config = json.load(f)
        self.helper_api = config['app_helper']['api_url']
        self.helper_key = config['app_helper']['key']
        self.browser = config['app_settings']['browser']
        self.environment = config['app_settings']['environment']
        self.build_number = config['app_settings']['build_number']
        self.report_update = config['app_helper']['report_update']

    def sendReportToAppHelper(self, test_env):
        global type
        type = ""
        if "TR" == test_env:
            type = "Test Run"
        else:
            type = "Test Case"
        if "yes" == self.report_update:
          files = [('html', open('report.html', 'rb')), ('log', open('log.html', 'rb')), ('output', open('output.xml', 'rb')), ('test_log', open('test_log.txt', 'rb'))]
          values = {'key': self.helper_key, 'browser': self.browser, 'build': self.build_number, 'environment': self.environment, 'os': platform.system()+" "+platform.release(), 'title': type}
          r = requests.post(self.helper_api, files=files, data=values)