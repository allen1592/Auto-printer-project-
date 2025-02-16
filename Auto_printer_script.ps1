function Download_File {
    param (
        [string]$url,
        [string]$saveFolder,
        [string]$printerDriver
    )
    
    # Combine the folder and file name to create the full save path
    $savePath = Join-Path -Path $saveFolder -ChildPath $printerDriver

    # Send a GET request to the URL
    $response = Invoke-WebRequest -Uri $url -UseBasicP -ErrorAction Stop

    # Check if the request was successful
    if ($response.StatusCode -eq 200) {
        # Create the folder if it doesn't exist
        if (-not (Test-Path -Path $saveFolder)) {
            New-Item -ItemType Directory -Path $saveFolder | Out-Null
        }

        # Save the content to the specified file path
        [System.IO.File]::WriteAllBytes($savePath, $response.Content)
        Write-Host "File downloaded successfully and saved to $savePath"
    } else {
        Write-Host "Failed to download file. Status code: $($response.StatusCode)"
    }
    return $savePath # Return the file path after checking
}

function Extract_ZipFile {
    param (
        [string]$ZipFilePath,
        [string]$ExtractionDirectory
    )

    try {
        # Extract a ZIP file to a specified directory.
        [System.IO.Compression.ZipFile]::ExtractToDirectory($ZipFilePath, $ExtractionDirectory)
        Write-Host "Extracted files to $ExtractionDirectory"
    } catch [System.IO.InvalidDataException] {
        Write-Host "Error: The file $ZipFilePath is not a valid ZIP file."
    } catch {
        Write-Host "An error occurred while extracting the ZIP file: $_"
    }
}

function Install_Driver {
    param (
        [string]$InstallerPath
    )

    # Run the installer executable.
    if (Test-Path $InstallerPath) {
        try {
            Start-Process -FilePath $InstallerPath -Wait -ErrorAction Stop
            Write-Host "Installation completed successfully."
        } catch {
            Write-Host "An error occurred during installation: $_"
        }
    } else {
        Write-Host "Installer not found: $InstallerPath"
    }
}
# Main execution block
$url = "https://business.toshiba.com/downloads/KB/f1Ulds/21280/ebn-Uni-7.222.5412.231.zip"
$saveFolder = "C:\Users\Public\Downloads"  # Change to your desired path
$zipFilename = "printer_driver.zip" # Change name of the file when downloaded

# Step 1: Download the ZIP file
$zipFilePath = Download-File -url $url -saveFolder $saveFolder -printerDriver $zipFilename

# Step 2: Extract Zip file
if ($ZipFilePath) { # Check if the download was successfuls
    $ExtractionDirectory = $SaveFolder # Specify the extraction directory
    Extract_ZipFile -ZipFilePath $ZipFilePath -ExtractionDirectory $ExtractionDirectory
}

# Step 3: Auto install file 
    $InstallerName = "essetup.exe"  # Change this to the actual installer name if different
    $InstallerPath = Join-Path "C:\Users\Public\Downloads\UNI" $InstallerName 
    # Nếu file giải nén có thêm 1 folder khác cần thay đổi đường dẫn nơi chưa file cài đặt
    Install_Driver -InstallerPath $InstallerPath