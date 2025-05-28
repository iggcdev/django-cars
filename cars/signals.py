from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarIventory
from openai_api.client import get_car_ai_bio

# @receiver(pre_save,sender=Car)
# def car_pre_save(sender,instance,**kwargs):
#     print('### PRE SAVE ###')
# @receiver(pre_delete,sender=Car)
# def car_pre_delete(sender,instance,**kwargs):
#     print('### PRE DELETE ###')

def car_inventory_update():
    cars_count = Car.objects.all().count()    
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    print(cars_value)
    CarIventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save,sender=Car)
def car_pre_save(sender,instance,**kwargs):
    if not instance.bio:
        ai_bio = get_car_ai_bio(
            model=instance.model, brand=instance.brand, year=instance.model_year
        )
        instance.bio = ai_bio

@receiver(post_save,sender=Car)
def car_post_save(sender,instance,created,**kwargs):
    if created:
        # novo registro detectado, lança o signal de criação
        car_inventory_update()
    else:
        #Caso seja uma atualização de registro, tambem será necessario chamar a função de signal para atualizar status do banco
        car_inventory_update()

@receiver(post_delete,sender=Car)
def car_post_delete(sender,instance,**kwargs):
    car_inventory_update()
