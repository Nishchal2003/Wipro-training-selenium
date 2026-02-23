*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}       https://practice.automationtesting.in/

*** Test Cases ***
Verify Link Tests
        Open Browser        ${url}       chrome
        Maximize Browser Window
        Click Element    //a[normalize-space()='My Account']
        Wait Until Element Is Visible    //h2[normalize-space()='Login']
        
        Input Text    //input[@id='username']    Admin
        Input Text    //input[@id='password']    Admin123
        Click Element    //input[@name='login']

        
