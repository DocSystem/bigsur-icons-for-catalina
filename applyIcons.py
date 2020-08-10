import os

print("You need to have root rights to execute this script")
print("And SIP need to be disabled and system drive mounted as writable if on Catalina or more")

print(" ")

# Remounting Root FS as writable

print("Remouting system drive as writable (Required on Catalina+)")
os.system("sudo mount -uw /")

print(" ")

# Drives icons

print("Copying drives icons...")
print(" ")
print("Copying File Server icon...")
os.system("sudo cp -f Drives/GenericFileServerIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # File Server icon
print("Copying Time Machine icon...")
os.system("sudo cp -f Drives/GenericTimeMachineDiskIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Time Machine icon

print("Copying Internal drive icon...")
os.system("sudo cp -f Drives/Internal.icns /System/Library/Extensions/IOStorageFamily.kext/Contents/Resources/") # Internal Drive icon
print("Copying Removable drive icon...")
os.system("sudo cp -f Drives/Removable.icns /System/Library/Extensions/IOStorageFamily.kext/Contents/Resources/") # Removable drive icon

print(" ")

# Folders icons

print("Copying folders icons...")
print(" ")
print("Copying Applications folder icon...")
os.system("sudo cp -f Folders/ApplicationsFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Applications Folder icon
print("Copying Burnable folder icon...")
os.system("sudo cp -f Folders/BurnableFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Burnable Folder icon
print("Copying Desktop folder icon...")
os.system("sudo cp -f Folders/DesktopFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Desktop Folder icon
print("Copying Documents folder icon...")
os.system("sudo cp -f Folders/DocumentsFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Documents Folder icon
print("Copying Downloads folder icon...")
os.system("sudo cp -f Folders/DownloadsFolder.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Downloads Folder icon
print("Copying Generic folder icon...")
os.system("sudo cp -f Folders/GenericFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Generic Folder icon
print("Copying Home folder icon...")
os.system("sudo cp -f Folders/HomeFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Home Folder icon
print("Copying Library folder icon...")
os.system("sudo cp -f Folders/LibraryFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Library Folder icon
print("Copying Movies folder icon...")
os.system("sudo cp -f Folders/MovieFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Movies Folder icon
print("Copying Music folder icon...")
os.system("sudo cp -f Folders/MusicFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Music Folder icon
print("Copying Pictures folder icon...")
os.system("sudo cp -f Folders/PicturesFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Pictures Folder icon
print("Copying Sites folder icon...")
os.system("sudo cp -f Folders/SitesFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Sites Folder icon
print("Copying Smart folder icon...")
os.system("sudo cp -f Folders/SmartFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Smart Folder icon
print("Copying System folder icon...")
os.system("sudo cp -f Folders/SystemFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # System Folder icon
print("Copying Users folder icon...")
os.system("sudo cp -f Folders/UsersFolderIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Users Folder icon
print("Copying Utilities folder icon...")
os.system("sudo cp -f Folders/UtilitiesFolder.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Utilities Folder icon

print(" ")

# Other icons

print("Copying Other icons...")
print(" ")
print("Copying Generic Document icon...")
os.system("sudo cp -f Misc/GenericDocumentIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Generic Document icon
print("Copying Generic Application icon...")
os.system("sudo cp -f Applications/Icns/GenericApplicationIcon.icns /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/") # Generic Application icon

print(" ")

# Clean icon cache

print("Cleaning icon cache...")
os.system("sudo find /private/var/folders/ -name 'com.apple.dock.iconcache' -delete")
os.system("sudo find /private/var/folders/ -name 'com.apple.iconservices' -delete")
os.system("sudo rm -r /Library/Caches/com.apple.iconservices.store")

print(" ")

# Restart Finder and Dock

print("Restarting Finder and Dock")
os.system("killall Finder")
os.system("killall Dock")

print(" ")
print("Done!")
