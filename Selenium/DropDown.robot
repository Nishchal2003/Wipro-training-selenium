*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/


*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        @{labels}=        Get WebElements    id=dropdown-class-example
        Select From List By Label    id=dropdown-class-example      Option3
        Sleep    2s
        Select From List By Index    id=dropdown-class-example      2
        Sleep    2s
        Select From List By Value    id=dropdown-class-example      option1
        Sleep    2s
        Close Browser