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
        Input Text    //input[@data-qa='login-email']    nishu@gmail.com
        Input Text    //input[@placeholder='Password']    Admin@123
        Click Button    //button[normalize-space()='Login']
        Wait Until Element Is Visible    //a[normalize-space()='Contact us']
        Click Element    //a[normalize-space()='Contact us']
        Wait Until Element Is Visible    //h2[normalize-space()='Get In Touch']
        Input Text    //input[@placeholder='Name']    nishchal
        Input Text    //input[@placeholder='Email']    nishu@gmail.com
        Input Text    //input[@placeholder='Subject']    Upload File
        Input Text    //textarea[@id='message']    Uploading
        Scroll Element Into View    //input[@name='submit']
        Choose File    //input[@name='upload_file']    C:\\Users\\Nikhil\\Downloads\\upload.txt
        Click Element    //input[@name='submit']

        #Handle Alert    action=ACCEPT    timeout=3
        #Wait Until Element Is Visible    //h2[normalize-space()='Get In Touch']
        Close Browser
