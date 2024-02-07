from django.db import models

#Entité infographiste 

class CgArtist(models.Model):
     types=[
        ('LIGHT','lighting'),
        ('COMP','compositing'),
        ('ANIM','animation'),
        ('MODEL','modelling'),
        ('SURFACE','surfacing'),
        ('FX','fx'),
        ('RIG','rigging')
                             ]
     name=models.CharField(max_length=50)
     email=models.EmailField()
     role=models.CharField(max_length=50,choices=types)
     def __str__(self):
        return self.name


#Entité chargé de production
class Producer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__(self):
        return self.name



#Entité superviseur
class Supervisor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__(self):
        return self.name

 
 #Entité Production
class PRODUCTION(models.Model):
    name=models.CharField(max_length=50)
    client=models.CharField(max_length=50, default='client-default')
    producers=models.ManyToManyField(Producer,related_name="prods")  #related_name permettra de récupérer les productions suivies par un Producer
                                                                     #producer_instance=Producer.objects.get(pk=number)
                                                                     #productions_suivies=producer_instance.prods.all()
   
    def __str__(self):
        return self.name
    
     
#Entité tâche  
class Task(models.Model):
    types=[
        ('LIGHT','lighting'),
        ('COMP','compositing'),
        ('ANIM','animation'),
        ('MODEL','modelling'),
        ('SURFACE','surfacing'),
        ('FX','fx'),
        ('RIG','rigging')
    ]
    id=models.IntegerField(primary_key=True) 
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50,choices=types)
    dateCreated=models.DateField(auto_now_add=True)
    dateDue=models.DateField(auto_now_add=False, null=True, blank=True)
    completed=models.BooleanField(default=False)
                                #4 clés étrangères : une tâche est associée à l'ID d'un producer(chargé de prod), l'ID  d'un Superviseur, l'ID d'Un cgArtist(infographiste)
                                #et l'ID d'une PRODUCTION 
                                # Si une PRODUCTION est détruite toutes les tâches associées seront aussi détruites (en cascade) alors que si un Producer , Supervisor et CgArtist
                                #le champ de la Task associée sera laissé vide (Set Null)
                            
    producerID=models.ForeignKey(Producer, on_delete=models.SET_NULL,blank=True,null=True,related_name="producerTasks")
    supervisorID=models.ForeignKey(Supervisor, on_delete=models.SET_NULL,blank=True,null=True,related_name="supervisorTasks")
    cgArtistId=models.ForeignKey(CgArtist, on_delete=models.SET_NULL,blank=True,null=True,related_name="cgArtistTasks")
    PRODUCTIONId=models.ForeignKey(PRODUCTION, on_delete=models.CASCADE,null=True,related_name="PRODUCTIONTasks")

    def __str__(self):
        return self.name
       
    
    

    

    
    
    
    
    

    
    