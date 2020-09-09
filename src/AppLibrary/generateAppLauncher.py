import json
import os

class Launcher:

    def __init__(self):
      with open('appconfig.json') as f:
        config = json.load(f)
        self.app_launcher_path = config['app_settings']['app_launcher_path']
        self.suite_header_path = config['app_settings']['suite_header_path']
        self.suite_footer_path = config['app_settings']['suite_footer_path']
        self.test_data = config['app_settings']['test_data']

    def makeData(self, data):

        jsn = json.loads(data)
        if os.path.exists(self.test_data):
            os.remove(self.test_data)
        test_data_write = open(self.test_data, "a")
        test_data_write.write(json.dumps(jsn, indent = 4, sort_keys=True))
        test_data_write.close()

        if os.path.exists(self.app_launcher_path):
            os.remove(self.app_launcher_path)
        head = open(self.suite_header_path, "r")
        footer = open(self.suite_footer_path, "r")
        data_write = open(self.app_launcher_path, "a")
        data_write.write(head.read())

        for jsn_data in jsn:
            data_write.write(jsn_data + "\n")
            data_write.write("    "+"[Documentation]  "+jsn[jsn_data]["test_title"]+"\n")
            data_write.write("    "+jsn[jsn_data]["test_identifier"]+"."+jsn_data+"\n")

        data_write.write(footer.read()+"\n")
        data_write.close()
        head.close()
        footer.close()