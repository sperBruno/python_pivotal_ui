SET PYTHONPATH=%~dp0..\src;%~dp0..\features;%~dp0..\environment

robot --VariableFile ..\environment\global_variables.py --output ../reports/xml-report2008.xml --report ../reports/html-report2008 --log ../logs/html-logs2008 --logtitle API-Test --suitestatlevel 1 --name Full-Regression-Suites --ArgumentFile ../argument_files/full_regression_suites.txt
