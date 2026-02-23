*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice


*** Test Cases ***
Verify radio elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Wait Until Element Is Visible    xpth://input[value='radio1']
        Click Button    xpath://input[@value = 'radio1']
        Sleep    5s
        Click Button    id=checkBoxOption3
        close Browser