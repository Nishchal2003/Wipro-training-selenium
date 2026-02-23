*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://automationexercise.com/

*** Test Cases ***
Verify Ecomerce Application
        Open Browser        ${url}       chrome
        Maximize Browser Window
        Wait Until Element Is Visible    //a[normalize-space()='Signup / Login']
        Click Element    //a[normalize-space()='Signup / Login']
        Wait Until Element Is Visible    //h2[normalize-space()='Login to your account']
        Input Text    //input[@data-qa='login-email']    nishu@gmailcom
        Input Text    //input[@placeholder='Password']    Admin123
        Click Button    //button[normalize-space()='Login']
        Wait Until Element Is Visible    //p[normalize-space()='Your email or password is incorrect!']
        Close Browser
