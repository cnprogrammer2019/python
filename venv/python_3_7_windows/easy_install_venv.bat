python -m venv %1
call %1\Scripts\activate.bat
python -m pip install --upgrade pip -i %2
pip install %~3 -i %2
call %1\Scripts\deactivate.bat