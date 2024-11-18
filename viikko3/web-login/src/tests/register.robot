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

Login After Successful Registration
    Set Username    john
    Set Password    Password123!
    Set Password Confirmation    Password123!
    Submit Registration
    Click Link  Continue to main page
    Submit Logout
    Login Page Should Be Open
    Set Username    john
    Set Password    Password123!
    Submit Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username    john123
    Set Password    Password123!
    Set Password Confirmation    Password123!
    Submit Registration
    Page Should Contain    Username can only contain lowercase letters (a-z)
    Click Link  Login
    Login Page Should Be Open
    Set Username    john123
    Set Password    Password123!
    Submit Login
    Login Page Should Be Open
    Page Should Contain   Invalid username or password

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

Submit Login
    Click Button    Login

Submit Logout
    Click Button    Logout

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Welcome Page Should Be Open
    Title Should Be    Welcome to Ohtu Application!

Main Page Should Be Open
    Title Should Be    Ohtu Application main page

Login Page Should Be Open
    Title Should Be    Login

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
