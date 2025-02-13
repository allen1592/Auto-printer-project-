import os 
import requests # module get url 
import subprocess #module auto install file
import zipfile #extract File 

    
def download_file(url, save_folder, printer_driver):
    # Sau khi download file từ url thì sẽ kết hợp file về folder và tên file
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
    return save_path # cần sử dụng return để cho phép sau khi check thì trả lại hàm 

# Hàm giải nén file 
def extract_zip(zip_path, extract_to):
    try:
        """Extract a ZIP file to a specified directory."""
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted files to {extract_to}")
    except zipfile.BadZipFile:
            print(f"Error: The file {zip_path} is not a valid ZIP file.")
    except Exception as e:
            print(f"An error occurred while extracting the ZIP file: {e}")
# Hàm auto run file.exe
def install_driver(installer_path):
    """Run the installer executable."""
    if os.path.exists(installer_path):
        try:
            subprocess.run([installer_path], check=True)
            print("Installation completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during installation: {e}")
        except OSError as e:
            print(f"OS error occurred: {e}")
    else:
        print(f"Installer not found: {installer_path}")


# Câu lệnh bên dưới cho pháp chạy các tính năng chính có trong hàm phía trên 
if __name__ == "__main__":
    # URL of the printer driver ZIP file
    url = "https://business.toshiba.com/downloads/KB/f1Ulds/21280/ebn-Uni-7.222.5412.231.zip"
    
    # Folder to save the downloaded file
    save_folder = r"C:\Users\Public\Downloads"  # Change to your desired path
    zip_filename = "printer_driver.zip" # chaneg name file when was download 
    
    # Step 1: Download the ZIP file
    zip_path = download_file(url, save_folder, zip_filename)
    
    if zip_path:  # Check if the download was successful
        # Step 2: Extract the ZIP file
        extract_to = save_folder  # Specify the extraction directory
        extract_zip(zip_path, extract_to)

        # Step 3: Find the installer executable (adjust the name as necessary)
        installer_name = "essetup.exe"  # Change this to the actual installer name if different
        installer_path = os.path.join(r"C:\Users\Public\Downloads\UNI", installer_name) 
        #Nếu file giải nén có thêm 1 folder khác cần thay đổi đường dẫn nơi chưa file cài đặt

        # Step 4: Install the driver
        install_driver(installer_path)

     

  
    

    
