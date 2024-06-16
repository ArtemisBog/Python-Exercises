Python Virtual Environment (venv) Cheat Sheet

Creating a Virtual Environment

    1.	Create a new virtual environment:
    python -m venv myenv

    2.	Create a new virtual environment with a specific Python version:
    python3.8 -m venv myenv

Activating the Virtual Environmen

    1.	Activate the virtual environment:
    source myenv/bin/activate

    2.	Deactivate the virtual environment:
    deactivate

Installing Packages in the Virtual Environment

    1.	Install a package in the virtual environment:
    pip install package_name

    2.	Upgrade a package in the virtual environment:
    pip install --upgrade package_name

    3.	Uninstall a package in the virtual environment:
    pip uninstall package_name

Managing Packages in the Virtual Environment

    1.	List all installed packages in the virtual environment:
    pip list

    2. Freeze the installed packages in the virtual environment:
    pip freeze > requirements.txt

    3. Install packages from a requirements.txt file:
    pip install -r requirements.txt
