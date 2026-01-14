import kagglehub

# Download latest version
path = kagglehub.dataset_download("sudalairajkumar/indian-startup-funding")

print("Path to dataset files:", path)