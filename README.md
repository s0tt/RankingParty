# RankingParty
A simple Python UI and visualization for partys. Split the guests into teams and enjoy some drinks together.
Using Pythons matplotlib, PyQT5 and TinyDB as simple JSON database.

Show updated data live in a horizontal bar graph:
![Live bar update demo](demo/demo01.gif)

Intuitive GUI based on PyQT5 to add new drinks into the database live:
![Live GUI demo](demo/demo02.gif)

To convert the UI files in the ui/ folder to actual Python code, use the following command:
pyuic5 ui/<filename>.ui -o RankingPartyGUI.py


# Run manual
1. Install requirements.txt file with

        pip install -r requirements.txt
    

2. Run GUI and main file from cmd

        python GUI.py 
        python main.py

3. Place windows as intended on the multiple screen setup
![HW Setup](demo/hw_setup.jpg)
   
4. Enjoy!