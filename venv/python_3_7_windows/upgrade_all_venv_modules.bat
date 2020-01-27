for /d %%d in (*) do (
%~dp0%%d\scripts\activate.bat
python update_all_modules.py "python -m pip " %1
%~dp0%%d\Scripts\deactivate.bat
)