
# **********************start open instagram code*******************************

import subprocess

def open_instagram():
    package_name = "com.instagram.android"
    activity_name = "com.instagram.android.activity.MainTabActivity"
    adb_path = "C:\\Users\\aakas\\Desktop\\platform-tools_r35.0.0-windows\\platform-tools\\adb.exe"  # Replace this with the actual path to adb.exe
    command = [adb_path, "shell", "am", "start", "-n", f"{package_name}/{activity_name}"]
    try:
        subprocess.run(command, check=True)
        print("Instagram app opened successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error opening Instagram app: {e}")

# Call the function to open Instagram
open_instagram()

# **********************close open instagram code*******************************

# import subprocess
# import time

# def open_instagram_reels():
#     # Replace these with the actual paths to adb.exe and the device ID
#     adb_path = "C:\\Users\\aakas\\Desktop\\platform-tools_r35.0.0-windows\\platform-tools\\adb.exe"
#     device_id = "PD21ADS464023788"

#     # Command to open Instagram
#     open_instagram_command = [adb_path, "-s", device_id, "shell", "am", "start", "-n", "com.instagram.android/com.instagram.mainactivity.MainActivity"]
#     try:
#         subprocess.run(open_instagram_command, check=True)
#         print("Instagram opened successfully!")
#         time.sleep(5)  # Wait for Instagram to open (adjust as needed)

#         # Command to tap on the Reels icon
#         tap_reels_command = [adb_path, "-s", device_id, "shell", "input", "tap", " 00000210", "00000598"]  # Replace x_coordinate and y_coordinate with the coordinates of the Reels icon
#         subprocess.run(tap_reels_command, check=True)
#         print("Navigating to Reels...")
#     except subprocess.CalledProcessError as e:
#         print(f"Error opening Instagram: {e}")

# # Call the function to open Instagram and navigate to Reels
# open_instagram_reels()
