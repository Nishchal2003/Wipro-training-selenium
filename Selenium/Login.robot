*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
 
 
*** Test Cases ***
Verify login scenario with valid credentials
        Open Browser        ${url}      edge
        #maximize the browser window
        Maximize Browser Window
        #wait till the element is loaded
        Wait Until Element Is Visible    xpath://label[normalize-space()='Username']
        #Enter the text in the username field
        Input Text    //input[@placeholder='Username']    admin@gmail.com
        
        Input Text    //input[@placeholder='Password']    Admin@2003
        
        Click Element    //button[normalize-space()='Login']
        
        Wait Until Element Is Visible    //h6[normalize-space()='Dashboard']
        Close Browser