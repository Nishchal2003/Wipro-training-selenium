*** Settings ***

Library     Collections

*** Variables ***

${name}     Nishchal
${num1}     10
${num2}     20
${sum}      ${{ ${num1} +   ${num2} }}
${city}     Byadgi
@{fruits}     apple       bannana     grapes
&{user}     username=nishchal       status=active

*** Test Cases ***
My First Test
    Log     ${name}
    Log     ${sum}
    Log     My native is: ${city}
    ${my_var}       Set Variable        Original Value
    ${my_var}       Set Variable        Updated Value
    Log     The variable is now: ${my_var}
    Log     ${fruits}[0]
    FOR     ${fruit}       IN      @{fruits}
            Log     ${fruit}
    END
    ${list_length}      Get Length      ${fruits}
    Log     ${list_length}





