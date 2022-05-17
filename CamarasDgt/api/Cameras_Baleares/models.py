from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class CamerasBaleares(TimeStampedModel, SoftDeletableModel):
        title = models.CharField(max_length=50, blank=True)
        url = models.URLField(blank=True)
        lat = models.FloatField(blank=True, null=True)
        lon = models.FloatField(blank=True, null=True)
        is_removed = models.BooleanField(default=False)
        
     
        def __str__(self):
            return self.title

#         def  load_data(self):
#             import csv
#             self.file = open(r'/home/elsamex/Documentos/CamarasBaleares.csv')
#             self.row = csv.reader(self.file, delimiter=',')
#             self.list = list(self.row)
#             del (self.list[0])
#             self.tupla = tuple(self.list)

#         def  save_data(self):
#             import psycopg2
#             self.connection = psycopg2.connect("dbname=Camaras_trafico_dgt, user=postgres, password=123456")
#             self.cursor = self.connection.cursor()
#             self.cursor.executemany ("""INSERT INTO Cameras_Baleares (title, url, lat, lon) VALUES (%s, %s, %s, %s)""", self.tupla)
#             self.connection.commit()
#             self.cursor.close()
#             self.connection.close()
        
#         def select (self):
#             self.load_data()
#             self.save_data()
#             self.cursor = self.connection.cursor()
#             self.cursor.execute("""SELECT * FROM Cameras_Baleares""")
#             self.rows = self.cursor.fetchall()
#             self.cursor.close()
#             self.connection.close()
#             return self.rows
    
# ins_db= CamerasBaleares()
# ins_db.load_data()
# ins_db.save_data()
# ins_db.select()
        



