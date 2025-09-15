import pandas as pd

class Recommender:

    #DATASET
    def __init__(self, dataset_path="../data/datasetParfum.xlsx"):
        self.df = pd.read_excel(dataset_path)

        print("Kolom Dataset: ", self.df.columns)


    #PREPOCESSING
    def prepocessing(self, text):
        pass




if __name__ == "__main__":
    rec = Recommender()
    print(rec.df.head()) 