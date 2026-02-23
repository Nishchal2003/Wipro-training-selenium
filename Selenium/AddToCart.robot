*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.saucedemo.com/

*** Test Cases ***
Verify cart
        Open Browser    ${url}    chrome
        Maximize Browser Window
        Wait Until Element Is Visible    locator