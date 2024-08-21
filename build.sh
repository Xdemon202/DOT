#!/bin/bash

# Define variables
PYTHON=python3
PIP=pip3
TEST_DIR="."

# Install dependencies
install() {
    echo "Installing dependencies..."
    $PIP install -r requirements.txt
}

# Run tests
test() {
    echo "Running tests..."
    $PYTHON -m unittest test_logic.py -v
}

# Package the application
package() {
    echo "Creating deployable package..."
    zip -r password_manager.zip password_manager_gui.py password_manager_logic.py test_logic.py requirements.txt build.sh
}

# Show usage information
usage() {
    echo "Usage: $0 {install|test|package|all}"
    exit 1
}

# Check arguments
if [ $# -eq 0 ]; then
    usage
fi

# Execute the appropriate function based on the argument
case $1 in
    install)
        install
        ;;
    test)
        test
        ;;
    package)
        package
        ;;
    all)
        install
        test
        package
        ;;
    *)
        usage
        ;;
esac
