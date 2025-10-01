import pandas as pd
import os

class Recommender:

    #DATASET
    def __init__(self, dataset_path=None):
        if dataset_path is None:
            # Get the absolute path to the data directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            dataset_path = os.path.join(os.path.dirname(current_dir), "data", "datasetParfum.xlsx")
        self.df = pd.read_excel(dataset_path)

        print("Kolom Dataset: ", self.df.columns)


    #PREPOCESSING
    def prepocessing(self):
        
        self.df = self.df.dropna() #Menghapus baris dengan nilai kosong
        self.df = self.df.drop_duplicates() #Menghapus baris duplikat
        text_columns = self.df.select_dtypes(include=['object']).columns #Ubah data ke lowercase, hapus spasi, hapus karakter khusus
        for col in text_columns:
            self.df[col] = self.df[col].str.lower()
            self.df[col] = self.df[col].str.strip()
            self.df[col] = self.df[col].str.replace(r'\s+', ' ', regex=True)
            self.df[col] = self.df[col].str.replace(r'[^a-z0-9\s]', '', regex=True)
        
        self.df = self.df.reset_index(drop=True) #Reset index setelah menghapus baris
        
        return self.df
    


if __name__ == "__main__":
    rec = Recommender()
    processed_df = rec.prepocessing()
    
    print(processed_df.head())
    print(processed_df.info())