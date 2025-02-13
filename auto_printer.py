import os # module hỗ trợ xác định hệ điều hành 
import requests # Modile yêu cầu get file.exe từ URL
import subprocess #module auto install file

    
def download_file(url, save_folder, printer_driver):
    # Create the full path for saving the file
    save_path = os.path.join(save_folder, printer_driver)

    # Send a GET request to the URL
    response = requests.get(url)
    
        # Check if the request was successful
    if response.status_code == 200:
        # Create the folder if it doesn't exist
        os.makedirs(save_folder, exist_ok=True)

        # Open the file in binary write mode and save the content
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def install_driver(printer_driver):
# Check if the file exists before trying to run it
    if os.path.exists(printer_driver):
        try:
            subprocess.run([printer_driver], check=True)
            print("Installation completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during installation: {e}")
    else:
        print(f"File not found: {printer_driver}")


# Định nghĩa các tên chính sẽ được sử dụng trong function 
if __name__ == "__main__":
    # Replace with the actual URL of the .exe file you want to download
    url = "https://drive.google.com/drive/u/0/folders/1mEtMRIXoVTr7gnqRVSrM1NFn7yPcjUGG"
    # Replace with the path to the folder where you want to save the file
    save_folder = r"C:\Users\danhp\Downloads"  # add r trước đường dẫn để tránh bị hiểu nhầm là khoảng trắng trong string
    # Specify the desired filename
    printer_driver = "toshiba_printer.exe"
    
    # Step 1: Call the download_file function
    download_file(url, save_folder, printer_driver)
    
    #Step 2: combines function download_file and install driver 
    full_driver_path = os.path.join(save_folder, printer_driver)
    
    # Step 3: Install the driver
    install_driver(printer_driver)
    

    