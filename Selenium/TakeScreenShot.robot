*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/upload-download.php

*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    //a[@id='downloadButton']
        Sleep    3s
        Capture Element Screenshot    //a[@id='downloadButton']        E:/Nishchal/download_button.png
        Sleep    3s
        Close Browser