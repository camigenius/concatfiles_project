import os
import pandas as pd


class ConcatDataFrames:
    def __init__(self):
        self.dataframes = []

    def add_dataframe(self, df):
        """
        Agrega un DataFrame a la lista de DataFrames.
        """
        self.dataframes.append(df)

    def concat_dataframes(self):
        """
        Concatena los DataFrames en la lista y reinicia el índice.
        Retorna el DataFrame concatenado si las columnas son iguales,
        None si las columnas son diferentes o la lista está vacía.
        """
        if len(self.dataframes) == 0:
            print("La lista de DataFrames está vacía.")
            return None

        # Obtiene la lista de nombres de columnas del primer DataFrame en la lista
        columns = self.dataframes[0].columns.to_list()

        # Verifica si todas las columnas son iguales en todos los DataFrames
        if all(df.columns.to_list() == columns for df in self.dataframes):
            # Si las columnas son iguales, concatena los DataFrames y reinicia el índice
            concatenated_df = pd.concat(self.dataframes, ignore_index=True)
            return concatenated_df
        else:
            # Si las columnas son diferentes en algún DataFrame, imprime un mensaje de error
            print("Los DataFrames tienen diferentes nombres de columnas.")
            return None
    def list_file_in_folder(folder):
      files = []
    # Obtiene la lista de archivos en la carpeta
      for file in os.listdir(folder):
        # Verifica si el elemento es un archivo
        if os.path.isfile(os.path.join(folder, file)):
            files.append(os.path.join(folder, file))
      return files

