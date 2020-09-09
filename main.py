import sys
from src.AppLibrary.DataBase import DBHelper
from src.AppLibrary.generateAppLauncher import Launcher
from src.AppLibrary.reports import Reports
from src.AppLibrary.ExcelData import Excel
import json
import robot
import os

data_env = str(sys.argv[1])
data_run = str(sys.argv[2])
run_key = str(sys.argv[3])
testInstance = DBHelper()
launcherInstance = Launcher()
reportInstance = Reports()
excelInstance = Excel()
global testData

if "-tc" == data_run:

    if "-db" == data_env:

        result = testInstance.makeTestCaseData(run_key)
        json_data = json.dumps(result)
        launcherInstance.makeData(json_data)

    elif "-excel" == data_env:
        result = excelInstance.makeTestCaseData(run_key)
        json_data = json.dumps(result)
        launcherInstance.makeData(json_data)

    elif "-jira" == data_env:
        print("Development in progress...")

elif "-tr" == data_run:

    if "-db" == data_env:

        keys = testInstance.makeTestRunData(run_key)
        result = testInstance.makeTestCaseData(keys)
        json_data = json.dumps(result)
        launcherInstance.makeData(json_data)

    elif "-excel" == data_env:
        keys = excelInstance.makeTestRunData(run_key)
        result = excelInstance.makeTestCaseData(keys)
        json_data = json.dumps(result)
        launcherInstance.makeData(json_data)

    elif "-jira" == data_env:
        print("Development in progress...")

logFile = open('test_log.txt', 'w')
robot.run("src/ExecutionScript/AppLauncher.robot",stdout=logFile)
#os.popen('robotmetrics -M test_report.html --logo "images/logo.png"')
#os.popen.close()
reportInstance.sendReportToAppHelper(data_run)