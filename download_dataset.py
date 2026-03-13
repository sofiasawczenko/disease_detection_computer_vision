import kagglehub

# baixar dataset
path = kagglehub.dataset_download("emmarex/plantdisease")

print("Dataset baixado em:", path)