*** Settings ***
Library         SeleniumLibrary
Library         DataDriver      file=E:/Nishchal/RobotFramework/TestData/ddtLogindataCSV.csv      sheet_name=ddtLogindataCSV

Test Template   Login Test
Test Setup      Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
Test Teardown   Close Browser

*** Test Cases ***
Verify login scenario with user ${username}    Default    Default

*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    xpath://input[@name='username']
    Input Text      xpath://input[@name='username']    ${username}
    Input Text      xpath://input[@name='password']    ${password}
    Click Element       xpath://button[@type='submit']
    Wait Until Element Is Visible    //h6[normalize-space()='Dashboard']
