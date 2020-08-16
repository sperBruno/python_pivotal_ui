SET PYTHONPATH=%~dp0..;%~dp0..\src;%~dp0..\features;%~dp0..\environment

robot --VariableFile environment\global_variables.py --output reports/xml-report.xml --report reports/html-report --log logs/html-logs --logtitle API-Test --suitestatlevel 1 --name Full-Regression-Suites --ArgumentFile argument_files/full_regression_suites.txt
