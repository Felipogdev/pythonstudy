import pandas as pd
import kagglehub

path = kagglehub.dataset_download("dylanjcastillo/7k-books-with-metadata")

print("Path to dataset files:", path)

books = pd.read_csv(f"{path}/books.csv")

books.to_excel(f"{path}", sheet_name="livros", index=False)