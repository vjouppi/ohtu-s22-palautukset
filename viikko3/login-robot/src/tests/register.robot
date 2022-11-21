*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  abc  abcdefg1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  abc  abcdefg1
    Input New Command
    Input Credentials  abc  abcdefg1
    Output Should Contain  User with username abc already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  abcdefg1
    Output Should Contain  Username must be 3 characters or more
    
Register With Valid Username And Too Short Password
    Input Credentials  abc  abc
    Output Should Contain  Password must be 8 characters or more

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  abc  aBcDeFgH
    Output Should Contain  Password must have special characters
