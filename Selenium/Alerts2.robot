*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/alerts.php

*** Test Cases ***
Verify check elements
    [Teardown]    Close Browser
    Open Browser    ${url}    chrome
    Maximize Browser Window

    #  Standard Alert
    Wait Until Element Is Visible    xpath=//button[text()='Alert']
    Click Element                    xpath=//button[text()='Alert']
    Handle Alert    action=ACCEPT    timeout=10s
    Sleep    2s

    #  Confirmation Alert
    Wait Until Element Is Visible    xpath=(//button[text()='Click Me'])[2]
    Click Element                    xpath=(//button[text()='Click Me'])[2]
    Handle Alert    action=ACCEPT    timeout=10s
    Sleep    2s

    #  Prompt Alert
    Wait Until Element Is Visible    xpath=(//button[text()='Click Me'])[3]
    Click Element                    xpath=(//button[text()='Click Me'])[3]
    Input Text Into Alert    Hello    action=ACCEPT
    Sleep    2s
    Close Browser