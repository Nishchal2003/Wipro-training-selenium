*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php


*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Wait Until Element Is Visible    //input[@id='c_bs_1']
        Click Button    //input[@id='c_bs_1']
        Click Button    //input[@id='c_bs_2']
        Close Browser