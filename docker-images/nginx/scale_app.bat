@echo off

if "%~1"=="" (
    echo Usage: scale_apps.bat ^<number_of_instances^>
    exit /b 1
)

docker-compose -f .\nginx.yaml up -d --scale app=%1
