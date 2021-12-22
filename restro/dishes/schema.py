from graphene_django import DjangoObjectType,DjangoListField
import graphene
from .models import Category,Dish,Chef

class DishInput(graphene.InputObjectType):
    name=graphene.String()
    category=graphene.String()
    rating=graphene.String()
    cost=graphene.String()
class CategoryInput(graphene.InputObjectType):
    name=graphene.String()    

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        fields='__all__'
class DishesType(DjangoObjectType):
    class Meta:
        model=Dish
        fields=('id','name')
class Chefss(DjangoObjectType):
    class Meta:
        model=Chef
        fields='__all__'
    
class choicegender(graphene.Enum):
    Male='Male'
    Female='Female'
class Query(graphene.ObjectType):
    # all_quiz=DjangoListField(QuizType)   
    fetch_Dishes=graphene.List(DishesType)   
    fetch_Chefs=graphene.List(Chefss)
    fetch_Category=graphene.List(CategoryType)
    
    create_dishes=graphene.List(DishesType,id=graphene.Int())
    create_chefs=graphene.List(Chefss,id=graphene.Int())
    create_category=graphene.List(CategoryType,id=graphene.Int())
    
    def resolve_fetch_Dishes(root,info):
        return Dish.objects.filter(category__name ="Chinese")
    
    def resolve_fetch_Chefs(root,info):
        return Chef.objects.all()
    
    def resolve_fetch_Category(root,info):
        return Category.objects.all()
    
    
        
        
class AddDishesMutation(graphene.Mutation):#for adding dishes data
    class Arguments:
        name=graphene.String(required=True)
        category=graphene.Int()
        rating=graphene.Int()
        cost=graphene.Int()
    dishes=graphene.Field(DishesType)
    
    @classmethod
    def mutate(cls,root,info,name,category,rating,cost):
        category_name=Category.objects.get(id=category)
        dishes=Dish(name=name,category=category_name,rating=rating,cost=cost)
        dishes.save()  
        return AddDishesMutation(dishes=dishes) 
class AddCatgoryMutation(graphene.Mutation):#for adding category data
    class Arguments:
        name=graphene.String(required=True)  
    category=graphene.Field(CategoryType)
    
    @classmethod
    def mutate(cls,root,info,name):
        category=Category(name=name)
        category.save()  
        return AddCatgoryMutation(category=category)
    
class AddChefMutation(graphene.Mutation):#for adding chef data
    class Arguments:
        first_name=graphene.String(required=True)  
        age=graphene.Int()
        gender=choicegender()
        # dishes=graphene.List(graphene.ID)
        dishes=graphene.List(DishInput)
    chef=graphene.Field(Chefss)
    
    @classmethod
    def mutate(cls,root,info,first_name,age,gender,dishes):
        # dish=Dish.objects.get(id=dishes)
        chef=Chef(first_name=first_name,age=age,gender=gender)
        chef.save()  
        # for x in dishes:
        #     try:
        #         dish=Dish.objects.get(id=x)
        #     except:
        #         raise Exception("no dish found with this id")
        #     chef.dishes.add(dish.id)
        #     chef.save()
        for y in dishes:
            cat=Category.objects.get(id=y.category)
            t=Dish(
                name=y.name,
                category=cat,
                rating=y.rating,
                cost=y.cost
                
            )
            t.save()
            chef.dishes.add(t.id)
            chef.save()
        return AddChefMutation(chef=chef)
#updation of Chef 
class UpdateChefMutation(graphene.Mutation):
    class Arguments:
        first_name=graphene.String(required=True)  
        age=graphene.Int()
        id=graphene.ID()
        gender=choicegender()
        dishes=graphene.List(DishInput)
        
    chef=graphene.Field(Chefss)
    
    @classmethod
    def mutate(cls,root,info,first_name,age,gender,dishes,id):
        #chef=Chef(first_name=first_name,age=age,gender=gender,id=id)
        #chef.save()  
        for y in dishes:
            cat=Category.objects.get(id=y.category)
            t=Dish(
                name=y.name,
                category=cat,
                rating=y.rating,
                cost=y.cost
                
            )
            t.save()
            chef.dishes.add(t.id)
            chef=Chef.objects.get(id=id)
            chef.first_name=chef.first_name
            chef.save()
        return UpdateChefMutation(chef=chef)
class UpdateDishesMutation(graphene.Mutation):#for adding dishes data
    class Arguments:
        id=graphene.ID()
        name=graphene.String(required=True)
        category=graphene.Int()
        rating=graphene.Int()
        cost=graphene.Int()
    dishes=graphene.Field(DishesType)
    
    @classmethod
    def mutate(cls,root,info,id,name,category,rating,cost):
        category_name=Category.objects.get(id=category)
        #dishes=Dish(name=name,id=id,category=category_name,rating=rating,cost=cost)
        dishes=Dish.objects.get(id=id)
        dishes.name=name
        dishes.category=category_name
        dishes.rating=rating
        dishes.cost=cost
        dishes.save()  
        return UpdateDishesMutation(dishes=dishes)

class UpdateCatgoryMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)  
        id=graphene.ID()
    category=graphene.Field(CategoryType)
    
    @classmethod
    def mutate(cls,root,info,id,name):
        #category=Category(name=name)
        category=Category.objects.get(id=id)
        category.name=name
        category.save()  
        return UpdateCatgoryMutation(category=category)

class DeleteCatgoryMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    category=graphene.Field(CategoryType)
    
    @classmethod
    def mutate(cls,root,info,id):
        category=Category.objects.get(id=id)
        category.delete()  
        return 
class DeleteDishesMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    dish=graphene.Field(DishesType)
    
    @classmethod
    def mutate(cls,root,info,id):
        dishes=Dish.objects.get(id=id)
        dishes.delete()  
        return
class DeleteChefMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    chef=graphene.Field(Chefss)
    
    @classmethod
    def mutate(cls,root,info,id):
        chefs=Chef.objects.get(id=id)
        chefs.delete()  
        return 
class Mutation(graphene.ObjectType):
    update_dish=AddDishesMutation.Field()
    update_category=AddCatgoryMutation.Field()
    update_chef=AddChefMutation.Field()
    update_chef_data=UpdateChefMutation.Field()
    update_dish_data=UpdateDishesMutation.Field()
    update_category_data=UpdateCatgoryMutation.Field()
    delete_category=DeleteCatgoryMutation.Field()
    delete_dishes=DeleteDishesMutation.Field()
    delete_chef=DeleteChefMutation.Field()
schema=graphene.Schema(query=Query,mutation=Mutation)