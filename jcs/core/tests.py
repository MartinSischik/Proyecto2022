from jcs.wsgi import *
from core.models import Type

#listar

#select * from tabla

# query = Type.objects.all()
# print (query)

#insertar

#t = Type()
#t.name = '24/h'
#t.save()

#edicion
# t=Type.objects.get(id=1)
# t.name ='muñaño'
# t.save()

#eliminacion

# t=Type.objects.get(id=1)
# t.delete()

# obj=Type.objects.filter(name__icontains='tiempo').count()
# print(obj)