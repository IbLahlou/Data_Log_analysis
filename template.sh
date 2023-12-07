#!/bin/bash

# Script: setup_project.sh
# Description: Set up the project directory structure

# Define folder names
SRC_FOLDER="src/main/java/com/example/periodiclogging"
RESOURCES_FOLDER="resources"

# Create source folder structure
mkdir -p "$SRC_FOLDER"

# Create resources folder
mkdir -p "$RESOURCES_FOLDER"

# Create log file
touch "logs/application.log"

# Print success message
echo "Project structure created successfully."
