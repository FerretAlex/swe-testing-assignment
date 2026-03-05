# Testing
## Testing strategy
The strategy for testing this system is straightforward: test all the main functions of the system with
user expected values, and edge-cases for user non-expected values. The integration testing consists of testing the ui
functions of the program, to ensure that all of the buttons and outputs work correctly.

The unit tests follow black-box testing, because the functionality of the system is minimal and is only concerned with 
correctly outputting computation results depending on the input.

Most of the tests conducted were functional tests as the most important for this system is to have correct outputs. The 
non-functional tests were minimal as all of the computation is handled by the functions of the system, and the integration
follows a very simple architecture.

The testing together compiles a non-full testing pyramid, however, it follows the recommended proportions, as there are
twice as more unit tests vs integration tests. There were no service tests conducted, as they were not necessary for this system.
## Unit tests:
The unit tests for this system were as follows:
1. Addition test
2. Subtraction test
3. Multiplication test
4. Division test
5. Clear functionality test
6. Divison by zero test
7. Decimal numbers test
8. Very big numbers test

All of the unit tests were passed successfully by the system.
## Integration tests:
1. All the function buttons work
2. Inputs for both variables work
3. Results are outputted correctly.

All of the integration tests were passed successfully.
## Summary
|Test name|Result|
|---|---|
|addition|pass|
|subtraction|pass|
|multiplication|pass|
|division|pass|
|clear|pass|
|division by 0|pass|
|decimal|pass|
|big numbers|pass|
|buttons|pass|
|inputs|pass|
|results|pass|