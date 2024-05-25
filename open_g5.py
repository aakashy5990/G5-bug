
# ****************************g5 my contact open code*****************************

# import subprocess

# def open_g5_my_connect():
#     # Replace these with the actual paths to adb.exe and the device ID
#     adb_path = "C:\\Users\\aakas\\Desktop\\platform-tools_r35.0.0-windows\\platform-tools\\adb.exe"
#     device_id = "PD21ADS464023788"  # Replace with your device ID

#     # Package name and activity name of the G5 My Connect app
#     package_name = "com.giindia.www.g5myconnect"  # Replace with actual package name
#     activity_name = "com.giindia.www.g5myconnect.MainActivity"  # Replace with actual activity name

#     # Command to open the G5 My Connect app
#     open_app_command = [adb_path, "-s", device_id, "shell", "am", "start", "-n", f"{package_name}/{activity_name}"]
#     try:
#         subprocess.run(open_app_command, check=True)
#         print("G5 My Connect app opened successfully!")
#     except subprocess.CalledProcessError as e:
#         print(f"Error opening G5 My Connect app: {e}")

# # Call the function to open the G5 My Connect app
# open_g5_my_connect()


# ****************************g5 my contact open close*****************************





# ****************************g5 my contact click login code start*****************************


# import subprocess
# import time

# def open_g5_my_connect():
#     adb_path = "C:\\Users\\aakas\\Desktop\\platform-tools_r35.0.0-windows\\platform-tools\\adb.exe"
#     device_id = "PD21ADS464023788"  # Replace with your device ID

#     package_name = "com.giindia.www.g5myconnect"
#     activity_name = "com.giindia.www.g5myconnect.MainActivity"

#     open_app_command = [adb_path, "-s", device_id, "shell", "am", "start", "-n", f"{package_name}/{activity_name}"]
#     try:
#         subprocess.run(open_app_command, check=True)
#         print("G5 My Connect app opened successfully!")
#         time.sleep(2)  # Adjust as needed
#         tap_login_button(device_id)
#     except subprocess.CalledProcessError as e:
#         print(f"Error opening G5 My Connect app: {e}")

# def tap_login_button(device_id):
#     login_button_x = 600  # Replace with actual X coordinate
#     login_button_y = 900  # Replace with actual Y coordinate
#     tap_command = ["adb", "-s", device_id, "shell", "input", "tap", str(login_button_x), str(login_button_y)]
#     try:
#         subprocess.run(tap_command, check=True)
#         print("Clicked on the login button successfully!")
#     except subprocess.CalledProcessError as e:
#         print(f"Error clicking on the login button: {e}")

# # Call the function to open the G5 My Connect app and click the login button
# open_g5_my_connect()

# ****************************g5 my contact click login code close*****************************









# **************************typing complete*********************


# import subprocess
# import time

# def open_g5_my_connect():
#     # Replace these with the actual paths to adb.exe and the device ID
#     adb_path = "C:\\Users\\aakas\\Desktop\\platform-tools_r35.0.0-windows\\platform-tools\\adb.exe"
#     device_id = "PD21ADS464023788"  # Replace with your device ID

#     # Package name and activity name of the G5 My Connect app
#     package_name = "com.giindia.www.g5myconnect"  # Replace with actual package name
#     activity_name = "com.giindia.www.g5myconnect.MainActivity"  # Replace with actual activity name

#     # Command to open the G5 My Connect app
#     open_app_command = [adb_path, "-s", device_id, "shell", "am", "start", "-n", f"{package_name}/{activity_name}"]
#     try:
#         subprocess.run(open_app_command, check=True)
#         print("G5 My Connect app opened successfully!")
#         time.sleep(5)  # Wait for the app to fully open (adjust this as needed)

#         # Tap on the User Login field to set the focus
#         tap_input_field(device_id, 0x00000094, 0x0000023e)  # Update with the actual coordinates
#         time.sleep(3)  # Add a small delay after tapping to allow the cursor to appear

#         # Type the username into the User Login field
#         type_text(device_id, "2022cs190")

#         # Add a small delay before tapping on the password field
#         time.sleep(1)

#         # Tap on the Password field to set the focus
#         tap_input_field(device_id, 0x0000008f, 0x000001b9)  # Update with the actual coordinates
#         time.sleep(3)  # Add a small delay after tapping to allow the cursor to appear

#         # Type the password into the Password field
#         type_text(device_id, "2354")
#     except subprocess.CalledProcessError as e:
#         print(f"Error opening G5 My Connect app: {e}")

# def tap_input_field(device_id, x_coordinate, y_coordinate):
#     # Command to tap on the input field specified by X and Y coordinates
#     tap_command = ["adb", "-s", device_id, "shell", "input", "tap", str(x_coordinate), str(y_coordinate)]
#     try:
#         subprocess.run(tap_command, check=True)
#         print(f"Tapped on input field at X: {x_coordinate}, Y: {y_coordinate}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error tapping input field: {e}")

# def type_text(device_id, text):
#     # Type each character with a delay
#     for char in text:
#         type_command = ["adb", "-s", device_id, "shell", "input", "text", char]
#         try:
#             subprocess.run(type_command, check=True)
#             print(f"Typed {char}")
#             # Add a short delay between typing each character
#             time.sleep(0.5)
#         except subprocess.CalledProcessError as e:
#             print(f"Error typing text: {e}")

# # Call the function to open the G5 My Connect app and type the username and password
# open_g5_my_connect()



# **************************typing complete end*********************








# *********************************type code with login button complete***********************************



# import subprocess
# import time

# def open_g5_my_connect():
#     # Replace these with the actual paths to adb.exe and the device ID
#     adb_path = "C:\\Users\\aakas\\Desktop\\platform-tools_r35.0.0-windows\\platform-tools\\adb.exe"
#     device_id = "PD21ADS464023788"  # Replace with your device ID

#     # Package name and activity name of the G5 My Connect app
#     package_name = "com.giindia.www.g5myconnect"  # Replace with actual package name
#     activity_name = "com.giindia.www.g5myconnect.MainActivity"  # Replace with actual activity name

#     # Command to open the G5 My Connect app
#     open_app_command = [adb_path, "-s", device_id, "shell", "am", "start", "-n", f"{package_name}/{activity_name}"]
#     try:
#         subprocess.run(open_app_command, check=True)
#         print("G5 My Connect app opened successfully!")
#         time.sleep(5)  # Wait for the app to fully open (adjust this as needed)

#         # Tap on the User Login field to set the focus
#         tap_input_field(device_id, 0x00000094, 0x0000023e)  # Update with the actual coordinates
#         time.sleep(3)  # Add a small delay after tapping to allow the cursor to appear

#         # Type the username into the User Login field
#         type_text(device_id, "2022cs190")

#         # Add a small delay before tapping on the password field
#         time.sleep(1)

#         # Tap on the Password field to set the focus
#         tap_input_field(device_id, 0x0000008f, 0x000001b9)  # Update with the actual coordinates
#         time.sleep(3)  # Add a small delay after tapping to allow the cursor to appear

#         # Type the password into the Password field
#         type_text(device_id, "2345")

#         # Tap on the Login button
#         tap_login_button(device_id)
#     except subprocess.CalledProcessError as e:
#         print(f"Error opening G5 My Connect app: {e}")

# def tap_input_field(device_id, x_coordinate, y_coordinate):
#     # Command to tap on the input field specified by X and Y coordinates
#     tap_command = ["adb", "-s", device_id, "shell", "input", "tap", str(x_coordinate), str(y_coordinate)]
#     try:
#         print("Tapping input field with command:", " ".join(tap_command))  # Debug information
#         subprocess.run(tap_command, check=True)
#         print(f"Tapped on input field at X: {x_coordinate}, Y: {y_coordinate}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error tapping input field: {e}")

# def type_text(device_id, text):
#     # Type each character with a delay
#     for char in text:
#         type_command = ["adb", "-s", device_id, "shell", "input", "text", char]
#         try:
#             subprocess.run(type_command, check=True)
#             print(f"Typed {char}")
#             # Add a short delay between typing each character
#             time.sleep(0.5)
#         except subprocess.CalledProcessError as e:
#             print(f"Error typing text: {e}")

# def tap_login_button(device_id):
#     # Replace these coordinates with the actual coordinates of the login button
#     login_button_x = 356
#     login_button_y = 665
#     tap_command = ["adb", "-s", device_id, "shell", "input", "tap", str(login_button_x), str(login_button_y)]
#     try:
#         print("Tapping login button with command:", " ".join(tap_command))  # Debug information
#         subprocess.run(tap_command, check=True)
#         print("Clicked on the login button successfully!")
#     except subprocess.CalledProcessError as e:
#         print(f"Error clicking on the login button: {e}")

# # Call the function to open the G5 My Connect app, type the username and password, and click the login button
# open_g5_my_connect()



# *********************************type code with login button complete***********************************





# **************************** loop code start ****************************



from datetime import *
import subprocess
import time

def open_g5_my_connect(password):
    # Replace these with the actual paths to adb.exe and the device ID
    adb_path = "C:\\Users\\aakas\\Desktop\\platform-tools_r35.0.0-windows\\platform-tools\\adb.exe"
    device_id = "PD21ADS464023788"  # Replace with your device ID

    # Package name and activity name of the G5 My Connect app
    package_name = "com.giindia.www.g5myconnect"  # Replace with actual package name
    activity_name = "com.giindia.www.g5myconnect.MainActivity"  # Replace with actual activity name

    # Command to open the G5 My Connect app
    open_app_command = [adb_path, "-s", device_id, "shell", "am", "start", "-n", f"{package_name}/{activity_name}"]
    try:
        subprocess.run(open_app_command, check=True)
        print("G5 My Connect app opened successfully!")
        time.sleep(1)  # Wait for the app to fully open (adjust this as needed)

        # Tap on the User Login field to set the focus
        tap_input_field(device_id, 0x00000094, 0x0000023e)  # Update with the actual coordinates
        time.sleep(1)  # Add a small delay after tapping to allow the cursor to appear

        # Type the username into the User Login field
        type_text(device_id, "2023csle005")

        # Add a small delay before tapping on the password field
        time.sleep(1)

        # Tap on the Password field to set the focus
        tap_input_field(device_id, 0x0000008f, 0x000001b9)  # Update with the actual coordinates
        time.sleep(1)  # Add a small delay after tapping to allow the cursor to appear

        # Type the password into the Password field
        type_text(device_id, password)

        # Tap on the Login button
        tap_login_button(device_id)
    except subprocess.CalledProcessError as e:
        print(f"Error opening G5 My Connect app: {e}")

def tap_input_field(device_id, x_coordinate, y_coordinate):
    # Command to tap on the input field specified by X and Y coordinates
    tap_command = ["adb", "-s", device_id, "shell", "input", "tap", str(x_coordinate), str(y_coordinate)]
    try:
        print("Tapping input field with command:", " ".join(tap_command))  # Debug information
        subprocess.run(tap_command, check=True)
        print(f"Tapped on input field at X: {x_coordinate}, Y: {y_coordinate}")
    except subprocess.CalledProcessError as e:
        print(f"Error tapping input field: {e}")

def type_text(device_id, text):
    # Type each character with a delay
    for char in text:
        type_command = ["adb", "-s", device_id, "shell", "input", "text", char]
        try:
            subprocess.run(type_command, check=True)
            print(f"Typed {char}")
            # Add a short delay between typing each character
            time.sleep(0.025)
        except subprocess.CalledProcessError as e:
            print(f"Error typing text: {e}")

def tap_login_button(device_id):
    # Replace these coordinates with the actual coordinates of the login button
    login_button_x = 356
    login_button_y = 665
    tap_command = ["adb", "-s", device_id, "shell", "input", "tap", str(login_button_x), str(login_button_y)]
    try:
        print("Tapping login button with command:", " ".join(tap_command))  # Debug information
        subprocess.run(tap_command, check=True)
        print("Clicked on the login button successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error clicking on the login button: {e}")

# Main loop to run the code with increasing password numbers
# for i in range(1, 6):  # Adjust the range as needed
#     password = f"235{i}"  # Update password format as needed
#     open_g5_my_connect(password)
#     time.sleep(5)  # Add a delay between each iteration



mydate=datetime(2002,1,1)
for i in range(366):
    p=mydate.strftime("%d%m")
    password=f"{p}2002"
    open_g5_my_connect(password)
    mydate+=timedelta(days=1)
    time.sleep(1)  # Add a delay between each iteration

# **************************** loop code close ****************************


# dawnloading SDK Plateform Tools link---->
# https://developer.android.com/tools/releases/platform-tools

# how to set path-->
# adb_path = "C:\\Users\\YourUsername\\Downloads\\platform-tools\\adb.exe"




