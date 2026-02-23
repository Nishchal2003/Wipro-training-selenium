*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/droppable.php

*** Test Cases ***
Verify Drag and Drop Functionality
        Open Browser        ${url}      chrome
        Maximize Browser Window

        Wait Until Element Is Visible    id:draggable
        Wait Until Element Is Visible    id:droppable

        # Perform the action
        Drag And Drop    id:draggable    id:droppable

        Wait Until Element Contains    id:droppable    Dropped!

        Close Browser