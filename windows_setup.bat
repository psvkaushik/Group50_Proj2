@echo off
setlocal enabledelayedexpansion

:: Check if pip is installed
where pip > nul 2>&1
if %errorlevel%==0 (
    set PIP_COMMAND=pip
) else (
    echo pip is not installed. Attempting to install it...
    :: Install pip using ensurepip
    python -m ensurepip --default-pip
    set PIP_COMMAND=pip
)

:: Install the required Python packages using the determined pip command
!PIP_COMMAND! install requests flask PyYAML

:: Check if the installation was successful
if !errorlevel!==0 (
    echo Packages installed successfully.
) else (
    echo Package installation failed.
)

endlocal
