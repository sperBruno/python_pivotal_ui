# python_pivotal_ui

This repository will test the ui of a pivotal tracker ui web app

Following you can see the tools that will be used for this porpuse:

 1. Robotframework
 2. Selenium
---
Install:
--
1. pip install robotframework
2. pip install simplejson
3. pip install selenium
--
1. pip install -r requirements.txt

---
Test Credential
--
* *UserName:* pirateTest@mailinator.com
* *Password:* pirateTest123

---
Run Test
---

To run test execute the full_regression file which is located inside of the scripts folder
>scripts\full_regression.bat

to add more tests to the regression just add the test file path to the argument_files/full_regression_suites.txt file

To run individual test execute a the following command

>robot --VariableFile environment\global_variables.py --test *User* features/qa/ui/login.txt
