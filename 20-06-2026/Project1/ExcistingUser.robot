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
        Wait Until Element Is Visible    //h2[normalize-space()='New User Signup!']
        Input Text    //input[@placeholder='Name']    nishchal
        Input Text    //input[@data-qa='signup-email']    nishu@gmail.com
        Click Button    //button[normalize-space()='Signup']
        Wait Until Element Is Visible    //p[normalize-space()='Email Address already exist!']
        Close Browser