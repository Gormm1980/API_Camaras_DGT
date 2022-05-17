from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class CamerasBaleares(TimeStampedModel, SoftDeletableModel):
        title = models.CharField(max_length=50, blank=True)
        lat = models.FloatField(blank=True, null=True)
        lon = models.FloatField(blank=True, null=True)
        url = models.URLField(blank=True)
        is_removed = models.BooleanField(default=False)
        
     
        def __str__(self):
            return self.title

        def  load_data(self):
            import csv
            self.file = open(r'/home/elsamex/Documentos/CamarasBaleares.csv')
            self.row = csv.reader(self.file, delimiter='"')
            self.list = list(self.row)
            self.tupla = tuple(self.list)
        

        def  save_data(self):
            import psycopg2
            self.connection = psycopg2.connect("dbname=camarasdgt user=elsamex password=123456")
            self.cursor = self.connection.cursor()
            self.cursor.executemany ("INSERT INTO api_camerasbaleares (title, lat, lon, url) VALUES (%s, %s, %s, %s)", self.tupla)
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        
        def select (self):
            self.load_data()
            self.save_data()
            self.cursor = self.connection.cursor()
            self.cursor.execute("""SELECT * FROM api_camerasbaleares""")
            self.rows = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            return self.rows
    
ins_db= CamerasBaleares()
ins_db.load_data()
ins_db.save_data()
ins_db.select()
        



