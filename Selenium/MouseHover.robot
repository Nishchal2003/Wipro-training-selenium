*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://practice.expandtesting.com/hovers

*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    xpath://div[@class='example]//div[1]//img[1]
        Mouse Over    xpath://h5[contains(text(),'name:user1')]
        Close Browser