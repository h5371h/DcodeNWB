# IMPORTS

import subprocess
import tkinter as tk
from tkinter import filedialog, simpledialog
import matplotlib.pyplot as plt
from pynwb import NWBHDF5IO

# DANDI CLI Download Function

def download_nwb_from_dandi(dandiset_id, target_path):
    command = f"dandi download https://dandiarchive.org/dandiset/{dandiset_id} --target {target_path}"
    try:
        subprocess.run(command, shell=True, check=True)
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
    # Initialize the main window
    root = tk.Tk()
    root.title("NWB Data Viewer")

    # Ensure 'root' is defined before creating widgets that depend on it
    download_button = tk.Button(root, text="Download NWB from DANDI", command=handle_download)
    download_button.pack()

    # Main event loop
    root.mainloop()

# Function to handle the download process
def handle_download():
    # Assuming this function interacts with the UI, make sure it's called after the UI setup begins
    dandiset_id = simpledialog.askstring("Input", "Enter DANDIset ID:")
    target_path = filedialog.askdirectory()
    if dandiset_id and target_path:  # Make sure values are provided
        download_nwb_from_dandi(dandiset_id, target_path)

# Main entry point of the application
if __name__ == "__main__":
    setup_ui()

