*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/


*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        ${elements}=        Get WebElements    xpth://input[@type = 'checkbox']
        FOR    ${element}    IN    @{elements}
            Click Element    ${element}
            Sleep    2s
        END
        Close Browser