*** Settings ***
Library  SeleniumLibrary
Library     OperatingSystem
Resource    ../TestBase/TestBase.robot
Resource    ../TestCase/Login/Login.robot

Suite Setup  TestBase.launchBrowser
Suite Teardown  TestBase.closeBrowser
Library  SeleniumLibrary
Library     OperatingSystem

*** Test Cases ***
TC001
    [Documentation]  Login to the test application
    Login.TC001
TC002
    [Documentation]  Logout from the test application
    Login.TC002

