*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php


*** Test Cases ***
Varify check elements
        Open Browser        ${url}      chrome
        Maximize Browser Window
        ${elements}=        Get WebElements    //input[starts-with(@id,'c_bs_')]
        FOR    ${element}    IN    @{elements}
            Click Element    ${element}
            Sleep    2s
        END
        Close Browser