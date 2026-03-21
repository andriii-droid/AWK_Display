import pandas as pd
import glob
from course import Course
from player import Player



class CreateAWK:
    def __init__(self):
        excel_files = glob.glob("data/*.xlsx")
        self.course = []

        for file_path in excel_files:
            df = pd.read_excel(file_path, dtype=str, skiprows=4)
            df = df.drop(df.columns[3:5], axis=1)

            print(f"Processing {file_path}: {len(df)} rows found.")

            try:
                idx_leiter = df[df.iloc[:, 0].astype(str).str.contains("Leiter", na=False)].index[0]
                idx_teilnehmer = df[df.iloc[:, 0].astype(str).str.contains("Teilnehmer", na=False)].index[0]
            except IndexError:
                print("Fehler: Schlüsselwörter 'Leiter' oder 'Teilnehmer' nicht gefunden!")

            df_metadata = df.iloc[:idx_leiter].copy()
            df_trainer = df.iloc[idx_leiter + 1 : idx_teilnehmer].copy()
            df_players = df.iloc[idx_teilnehmer + 1 :].copy()

            df_players = df_players.replace(['J', 'j', 'K', 'k', 'K, J', 'k, j'], 1)
            df_players = df_players.fillna(0)

            df_trainer = df_trainer.replace(['J', 'j', 'K', 'k', 'K, J', 'k, j'], 1)
            df_trainer = df_trainer.fillna(0)

            df_metadata = df_metadata.replace(['J', 'j', 'K', 'k', 'K, J', 'k, j'], 1)
            df_metadata = df_metadata.replace(['X'], 0)

            list_executed = df_metadata.iloc[6].tolist()[3:]
            list_dates = df_metadata.iloc[1].tolist()[3:]
            list_course_type = df_metadata.iloc[3].tolist()[3:]
            list_days = df_metadata.iloc[0].tolist()[3:]

            c = Course(executed=list_executed,
                       types=list_course_type,
                       days=list_days, 
                       dates=list_dates,
                       name=file_path)

            self.course.append(c)

            for index, row in df_players.iterrows():
                p = row.tolist()  
                name = f"{p[2]} {p[1]}"
                attendance = p[3:]
                Player(c, attendance, name)

            for index, row in df_trainer.iterrows():
                p = row.tolist()  
                name = f"{p[2]} {p[1]}"
                attendance = p[3:]
                Player(c, attendance, name, coach=True)