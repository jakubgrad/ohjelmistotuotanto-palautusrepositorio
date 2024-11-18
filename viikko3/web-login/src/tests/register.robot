*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username    john
    Set Password    Password123!
    Set Password Confirmation    Password123!
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username    jo
    Set Password    Password123!
    Set Password Confirmation    Password123!
    Submit Registration
    Registration Should Fail With Message    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username    john
    Set Password    Pass
    Set Password Confirmation    Pass
    Submit Registration
    Registration Should Fail With Message    Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username    john
    Set Password    password
    Set Password Confirmation    password
    Submit Registration
    Registration Should Fail With Message    Password must include at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username    john
    Set Password    Password123!
    Set Password Confirmation    WrongPassword
    Submit Registration
    Registration Should Fail With Message    Password and confirmation do not match

Register With Username That Is Already In Use
    Create User    john    Password123!
    Set Username    john
    Set Password    Password123!
    Set Password Confirmation    Password123!
    Submit Registration
    Registration Should Fail With Message    Username is already taken

*** Keywords ***
Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Confirmation
    [Arguments]    ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}

Submit Registration
    Click Button    Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Welcome Page Should Be Open
    Title Should Be    Welcome to Ohtu Application!

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
