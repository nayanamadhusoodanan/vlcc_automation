import json
import os
import xlrd

class Excel:

    def __init__(self):
      with open('appconfig.json') as f:
        config = json.load(f)
        self.excel_path = config['app_settings']['excel_path']

    def makeTestCaseData(self, data):
      tc_id = data.split(",")
      global testData
      testData = {}
      loc = (self.excel_path)
      wb = xlrd.open_workbook(loc)
      sheet = wb.sheet_by_index(1)

      for i in range(sheet.nrows):
        if sheet.cell_value(i, 0) in tc_id:
          id = {"test_id": sheet.cell_value(i, 0)}
          title = {"test_title": sheet.cell_value(i, 2)}
          jsn = json.loads(sheet.cell_value(i, 1))
          jsn.update(title)
          jsn.update(id)
          testData[sheet.cell_value(i, 0)] = jsn

      return testData

    def makeTestRunData(self, data):
      loc = (self.excel_path)
      wb = xlrd.open_workbook(loc)
      sheet = wb.sheet_by_index(0)
      global testData
      testData = ""
      for i in range(sheet.nrows):
        if sheet.cell_value(i, 0) == data:
          if testData == "":
            testData = sheet.cell_value(i, 1)
          else:
            testData = testData + "," + sheet.cell_value(i, 1)

      return testData