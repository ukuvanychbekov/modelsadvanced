from my_app.models import *

u1 = User.objects.create(email='nikname21@gmail.com', password='defender42')
c1 = Client.objects.create(name='Азат Соколов', card_number='4147 5657 9878 9009', user=u1)

u2 = User.objects.create(email=' altywa1998@gmail.com', password='nono34')
w1 = Worker.objects.create(name='Алтынай Алиева', position='Оператор кассы', user=u2)

shaurma = Food.objects.create(name='Шаурма', start_price=50)
burger= Food.objects.create(name='Гамбургер', start_price=25)

Syr = Ingredient.objects.create(name='Сыр', extra_price=10)
Kurica = Ingredient.objects.create(name='Курица', extra_price=70)
Gov = Ingredient.objects.create(name='Говядина', extra_price=80)
Salat = Ingredient.objects.create(name='Салат', extra_price=15)
Fri = Ingredient.objects.create(name='Фри', extra_price=15)

order1 =Order.objects.create(food=shaurma, ingredient=Gov, client=c1, worker = w1, order_date_time=2019)
Order.ingredient.set([Syr, Salat, Fri])







