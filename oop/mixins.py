"============== Миксины =============="
# Миксин - класс, который будет использоваться для наследования
# от миксинов не создаются объекты


class CreateMixin:
    def product_create(self, title, price):
        # self.__class - обращение к классу, 
        # который наследовался от этого миксина
        model = self.__class__

        obj = model()
        _id = model._id
        obj.title = title
        obj.price = price
        obj.id = _id
        model.objects[_id] = obj
        model._id += 1


class ReadMixin:
    def product_detail(self, p_id):
        from pprint import pprint
        model = self.__class__
        obj = self.objects.get(p_id)
        print({'id': self.id, 'title': self.title, 'price': self.price})

class UpdateMixin:
    ...

class DeleteMixin:
    def delete_prodict(self, p_id):
        model = self.__class__
        model.objects.pop(p_id)

class ProductCRUD(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    objects = {}
    _id = 1

    def __str__(self):
        return f"{self.id} -> {self.title}"

# crud = ProductCRUD()
# crud.product_create("obj", 45)
# crud.product_create("obj2", 456)
# crud.product_detail(id)
