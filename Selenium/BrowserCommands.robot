*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}       https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Browser Tests
        Open Browser        ${url}      chrome
