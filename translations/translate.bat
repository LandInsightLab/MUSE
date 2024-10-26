@echo off
setlocal enabledelayedexpansion

rem 设置输入文件夹路径
set input_dir=..\resources\ui
set output_file=translations.ts

rem 清空输出文件
del %output_file%

rem 构建参数字符串
set params=

for %%f in (%input_dir%\*.ui) do (
    set params=!params! %%f
)

rem 执行 lupdate 命令
pyside6-lupdate.exe !params! -ts %output_file%

endlocal
