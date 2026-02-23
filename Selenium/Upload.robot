*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://the-internet.herokuapp.com/upload

*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Wait Until Element Is Visible    //input[@id="file-upload"]
        Choose File    //input[@id="file-upload"]    C:\\Users\\Nikhil\\Downloads\\upload.txt        Click Element    //input[@id='file-submit']
        Sleep    2s
        Element Text Should Be    //h3[normalize-space()='File Uploaded!']    File Uploaded!
        Sleep    2s
        Close Browser