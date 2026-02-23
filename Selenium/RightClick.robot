*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Wait Until Element Is Visible    //a[normalize-space()='Sell']
        Open Context Menu    link=Sell
        Sleep    2s
        Double Click Element    //a[normalize-space()='Mobiles']
        Sleep    2s
        Close Browser