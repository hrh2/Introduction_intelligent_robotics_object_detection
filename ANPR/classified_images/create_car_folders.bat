@echo off
setlocal enabledelayedexpansion

:: Initialize maxIndex to 0
set "maxIndex=0"

:: Find the highest existing car_[index] folder
for /d %%F in (car_*) do (
    for /f "tokens=2 delims=_" %%I in ("%%F") do (
        if %%I gtr !maxIndex! set "maxIndex=%%I"
    )
)

:: Ask user how many new folders to create
set /p "folderCount=Enter the number of folders to create: "

:: Calculate the starting index for new folders
set /a startIndex=maxIndex + 1

:: Create the requested number of folders
for /l %%I in (0,1,%folderCount%) do (
    set /a currentIndex=startIndex + %%I
    md car_!currentIndex!
    echo Created folder: car_!currentIndex!
)

echo All folders created successfully.
pause
