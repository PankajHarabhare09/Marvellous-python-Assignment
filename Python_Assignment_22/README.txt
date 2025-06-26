# Duplicate File Removal Script

## Description:
This automation script scans a specified directory, removes duplicate files by comparing their checksums, and logs all removed files. It also sends an email with the log file and statistics.

## Usage:
DuplicateFileRemoval.py <DirectoryPath> <TimeIntervalInMinutes> <EmailID>

### Example:
DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

## Features:
- Scans for duplicate files using checksum
- Logs deleted duplicates to a timestamped file
- Sends email with log attachment and operation statistics
- Scheduled to repeat every given number of minutes

## Requirements:
- Python 3.x
- Internet access for email sending
- Replace email credentials in `FileOperations.py`
