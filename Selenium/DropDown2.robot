*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php

*** Test Cases ***
Verify check elements
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Wait Until Element Is Visible    id=state
    Select From List By Label    id=state    Uttar Pradesh
    Sleep    2s
    Select From List By Index    id=state    3
    Sleep    2s

    Close Browser