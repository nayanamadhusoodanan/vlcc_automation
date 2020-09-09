import mysql.connector
import json

class DBHelper:

    def __init__(self):
      with open('appconfig.json') as f:
        config = json.load(f)
        self.host = config['mysql']['host']
        self.user = config['mysql']['user']
        self.password = config['mysql']['password']
        self.db = config['mysql']['database']

    def __connect__(self):
        self.con = mysql.connector.connect(host = self.host, user = self.user, passwd = self.password, database = self.db)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()

    def makeTestCaseData(self, data):
        tc_id = data.split(",")
        global result
        global testData
        testData = {}
        testInstance = DBHelper()
        for key in tc_id:
            result = testInstance.fetch("SELECT test_case_id,title,test_data FROM test_data WHERE test_case_id  = '"+key+"';")
            for x in result:
                id = {"test_id": x[0]}
                title = {"test_title":x[1]}
                jsn = json.loads(x[2])
                jsn.update(title)
                jsn.update(id)
                testData[key] = jsn
        return testData

    def makeTestRunData(self, data):
        testInstance = DBHelper()
        global testData
        testData = ""
        result = testInstance.fetch("SELECT test_case FROM test_run_links WHERE test_run  = '"+data+"';")

        for x in result:
            if testData == "":
                testData = x[0]
            else :
                testData = testData+","+x[0]

        return testData