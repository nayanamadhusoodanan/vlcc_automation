*** Settings ***
Library  SeleniumLibrary
Library           OperatingSystem
Resource    ../Utility/GetData.robot

*** Keywords ***
launchBrowser
    ${data}     GetData.getAppData
    Open Browser    about:  ${data["browser"]}
    Maximize Browser Window
    Go to  ${data["base_url"]}

closeBrowser
	Close all browsers