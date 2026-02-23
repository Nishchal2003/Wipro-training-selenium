*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Sleep    2s
        Set Selenium Implicit Wait    5s
        Scroll Element Into View    link=Sell on Amazon
        Sleep    2s
        Click Element    link=Sell on Amazon
        Sleep    2s
        Title Should Be               Amazon.in:Selling on Amazon - Start Selling Now
        Close Browser