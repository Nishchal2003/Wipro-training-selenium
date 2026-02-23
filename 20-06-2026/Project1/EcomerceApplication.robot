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
        Sleep    2s
        Wait Until Element Is Visible    //b[normalize-space()='Enter Account Information']
        Click Button    //input[@id='id_gender1']
        Input Text    //input[@id='password']    Admin@123
        Select From List By Label    //select[@id='days']       21   
        Select From List By Label    //select[@id='months']     February
        Select From List By Label    //select[@id='years']      2021
        Input Text    //input[@id='first_name']    Admin
        Input Text    //input[@id='last_name']    Home
        Input Text    //input[@id='last_name']    Wipro
        Input Text    //input[@id='address1']    Penya
        Select From List By Label    //select[@id='country']        India
        Input Text    //input[@id='state']    Karnataka
        Input Text    //input[@id='city']    Bengaluru
        Input Text    //input[@id='zipcode']    456321
        Input Text    //input[@id='mobile_number']    1234567890
        Click Button    //button[normalize-space()='Create Account']
        Wait Until Element Is Visible    //b[normalize-space()='Account Created!']
        Click Element    //a[normalize-space()='Continue']
        Wait Until Element Is Visible    //a[normalize-space()='Home']
        Close Browser

