*** Settings ***
Library  SeleniumLibrary
Library     OperatingSystem

*** Keywords ***
TC001
    ${data}     GetData.getTestData
    Click Link      ${data["TC001"]["login_button"]}
    Sleep  1s
    Input Text      ${data["TC001"]["user"]["element"]}     ${data["TC001"]["user"]["data"]}
    Input Text      ${data["TC001"]["password"]["element"]}     ${data["TC001"]["password"]["data"]}
    Click Button    ${data["TC001"]["login_button"]}
	Page should contain  ${data["TC001"]["login_msg"]}
	Sleep  2s

TC002
    ${data}     GetData.getTestData
    Submit Form     ${data["TC002"]["logout_form"]}
	Page should contain  ${data["TC002"]["welcome_msg"]}