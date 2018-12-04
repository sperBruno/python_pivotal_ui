#!/usr/bin/env bash
#!/bin/sh
ROOT_PATH=$(cd ..; pwd)

(ps aux | grep -i robot | awk {'print $2'} | xargs kill -9) || echo "Killed all robot processes"

rm  -rf ../logs && echo "Removed old log files"

export PYTHONPATH="$ROOT_PATH/src:$ROOT_PATH/features:$ROOT_PATH/environment"
export PATH="$PATH:$ROOT_PATH/drivers/geckodriver"

echo $PYTHONPATH
export DISPLAY=:2.0

robot --xunit ../reports/junit.xml \
      --report ../reports/html-report-pivotal-ui --log ../logs/html-log-pivotal \
      --logtitle Pivotal --suitestatlevel 1 --name Full-Regression-Suites \
      --VariableFile ../environment/global_variables.py \
      --ArgumentFile ../argument_files/full_regression_api_suites.txt
