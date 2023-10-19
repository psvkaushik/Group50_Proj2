#!/bin/bash

#Ask for input from user

#read -p "Enter username please: " Username
#read -p "Enter your auth token please: " Token


# Check if pip is installed

if command -v pip &>/dev/null; then

    PIP_COMMAND=pip

else

    echo "pip is not installed. Attempting to install it..."

    sudo apt-get update

    sudo apt-get install -y python3-pip  # Install pip

    PIP_COMMAND=pip  # Use pip

fi

# Set GitHub environment variable

export GITHUB_TOKEN=$Token

# Install the required Python packages using the determined pip command

$PIP_COMMAND install requests flask PyYAML

# Check if the installation was successful

if [ $? -eq 0 ]; then

    echo "Packages installed successfully."

else

    echo "Package installation failed."

fi
