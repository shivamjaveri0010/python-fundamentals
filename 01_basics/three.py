import os

# Get contents of the current directory
directory_contents = os.listdir(".")

print("Raw List:", directory_contents)
print("\n--- Folder Contents ---")

# Print each item separately
for item in directory_contents:
    print(f"- {item}")