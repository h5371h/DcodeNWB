# IMPORTS

import subprocess
import tkinter as tk
from tkinter import filedialog, simpledialog
import matplotlib.pyplot as plt
from pynwb import NWBHDF5IO

# DANDI CLI Download Function

def download_nwb_from_dandi(download_link):
    """
    Downloads data from DANDI given a specific command.
    
    Parameters:
    download_link (str): The DANDI command or URL for downloading.
                         This could be a Dandiset ID like 'DANDI:000023', a specific subject, or a direct file link.
    """
    try:
        # Execute the download command
        subprocess.run(f"dandi download {download_link}", shell=True, check=True)
        print("Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")


# NWB File Reading Function

def read_nwb_file(file_path):
    io = NWBHDF5IO(file_path, mode='r')
    nwbfile = io.read()
    print(nwbfile)
    # here you can add more specific processing, e.g., reading specific datasets.

    io.close()

# Visualization Function

def visualize_data(data):
    plt.figure(figsize=(10, 4))
    plt.plot(data)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Sample Visualization')
    plt.show()

# Application UI setup

def setup_ui():
    global root, download_entry  # Make these available globally for simplicity
    root = tk.Tk()
    root.title("NWB Data Viewer")
    
    # Entry for download link or ID
    download_entry = tk.Entry(root)
    download_entry.pack()
    
    download_button = tk.Button(root, text="Download NWB from DANDI", command=handle_download)
    download_button.pack()
    
    root.mainloop()

def handle_download():
    download_link = download_entry.get()  # Get the link or ID from the entry widget
    if download_link:
        download_nwb_from_dandi(download_link)
    else:
        print("Please enter a valid download link or Dandiset ID.")

# Main entry point of the application
if __name__ == "__main__":
    setup_ui()

