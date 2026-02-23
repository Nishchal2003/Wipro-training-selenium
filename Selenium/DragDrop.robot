*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://the-internet.herokuapp.com/drag_and_drop

*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    //div[@id='column-a']
        Sleep    2s
        Drag And Drop    //div[@id='column-a']    //div[@id='column-b']
        Sleep    2s
        Close Browser