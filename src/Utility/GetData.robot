*** Settings ***
Library  SeleniumLibrary
Library           OperatingSystem

*** Keywords ***
getAppData
    ${file}    Get File    appconfig.json
        ${data}    Evaluate    json.loads('''${file}''')    json
            [Return]    ${data["app_settings"]}

getTestData
    ${file}    Get File    test_data.json
        ${data}    Evaluate    json.loads('''${file}''')    json
            [Return]    ${data}