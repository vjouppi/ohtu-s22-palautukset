*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Check

*** Test Cases ***
Register With Valid Username And Password
    Set Username  abc
    Set Password  abcdefGH13
    Set Confirmation  abcdefGH13
    Submit Credentials
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  abcdefGH13
    Set Confirmation  abcdefGH13
    Submit Credentials
    Registering Should Fail With Message  Username must be 3 characters or more

Register With Valid Username And Too Short Password
    Set Username  abcd
    Set Password  abc
    Set Confirmation  abc
    Submit Credentials
    Registering Should Fail With Message  Password must be 8 characters or more

Register With Nonmatching Password And Password Confirmation
    Set Username  abcde
    Set Password  abcdefGH13
    Set Confirmation  abcdefG
    Submit Credentials
    Registering Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  abcc
    Set Password  abcdefGH13
    Set Confirmation  abcdefGH13
    Submit Credentials
    Registering Should Succeed
    Go To App Page
    Main Page Should Be Open
    Submit Logout
    Go To Login Page
    Login Page Should Be Open
    Set Username  abcc
    Set Password  abcdefGH13
    Submit Login
    Main Page Should Be Open
    
Login After Failed Registration
    Set Username  abcde
    Set Password  abcdefGH13
    Set Confirmation  abcdefG
    Submit Credentials
    Registering Should Fail With Message  Passwords do not match
    Go To Login Page
    Login Page Should Be Open
    Set Username  abcde
    Set Password  abcdefGH13
    Submit Login
    Page Should Contain  Invalid username or password

*** Keywords ***
Go To Register Page And Check
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Submit Logout
    Click Button  Logout

Submit Login
    Click Button  Login

Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
