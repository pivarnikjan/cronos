#!/bin/bash

SERVICE_NAME="src"

function migrate_db_and_run(){
    cd ${SERVICE_NAME}
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py collectstatic --noinput
    ./manage.py runserver 0:8000
}

function run_tests(){
    cd ${SERVICE_NAME}
    ./manage.py migrate
    ./manage.py test
}


function help_menu () {
    cat << EOF
    Usage: ${0} (-i | -r | -a | -t)

    OPTIONS:
        -r|--run        Activation of virtualenv, migration of db changes and running webservice
        -a|--all        Provision everything
        -t|--test       Curl on admin page


    EXAMPLES:

        Run app:
            $ ${0} -r
        Provision everything:
            $ ${0} -a
        Run test:
            $ ${0} -t

EOF
}

case "${1}" in
  -r|--run)
  migrate_db_and_run
  ;;
  -t|--test)
  run_tests
  ;;
  -h|--help)
  help_menu
  ;;
  *)
  echo "${1} is not a valid flag, try running: ${0} --help"
  ;;
esac
