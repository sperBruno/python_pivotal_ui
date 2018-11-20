SET VCMT_INSTALLER_PATH=E:\installers\VCMT.1.0.0.0.exe
SET PYTHONPATH=C:\Python27\;%~dp0..\target_evironments\;%~dp0..\modules\;%~dp0..\robot-shared-keywords\modules\;%~dp0..\vipre-business-test;%~dp0..\vipre-business-test\resources\modules\

robot --VariableFile ..\target_environments\tpavct01\2012R2-cwa01-VB.py --output ../reports/xml-report2008.xml --report ../reports/html-report2008 --log ../logs/html-logs2008 --logtitle VIPRE-Cloud-Migration-Tool --suitestatlevel 1 --name Full-Regression-Suites --ArgumentFile ../argument_files/full_regression_suites.txt
