from django.db import models, reset_queries
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models import signals

# import datetime



class answers(models.Model):
    pool = models.ForeignKey('Pool', on_delete=models.CASCADE)
    answer = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if self.answer==1:
                self.pool.vote(1)
            elif self.answer==2:
                self.pool.vote(2)
        return super().save(*args, **kwargs)

class Pool(models.Model):
    quesstion = models.TextField()
    option_one = models.CharField(max_length=225)
    value_one = models.IntegerField(null=True, blank=True)
    option_two = models.CharField(max_length=225)
    value_two = models.IntegerField(null=True, blank=True)
    answer = models.ManyToManyField('answers')

    def __init__(self):
        self.old_value_one = self.value_one
        super().__init__(*args, **kwargs)
    def save(self, *args, **kwargs):
        if self.old_value_one != self.value_one:
            
        if not self.pk:
                self.value_one = 0
                self.value_two=0

        return super().save(*args, **kwargs)

    def vote(self, choice):#, choice):
        if choice==1:
            self.value_one+=1
        elif choice==2:
            self.value_two+=1
        self.save()
    
    def percentage(self)->tuple:
        vals_sum = self.value_one+ self.value_two
        return (self.value_two*100/vals_sum, self.value_one*100/vals_sum)
    
    

