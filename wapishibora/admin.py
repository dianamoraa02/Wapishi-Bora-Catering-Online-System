from django.contrib import admin
from wapishibora.models import Book_Table, Employees, Items, CardItems, ItemsOrder

# Register your models here.

class Book_TableAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Number', 'Date', 'Person')

    def Name(self, obj):
        return obj.Name  
    
    def Email(self, obj):
        return obj.Email
    def Number(self, obj):
        return obj.Number  
    def Date(self, obj):
        return obj.Date 
    def Person(self, obj):
        return obj.Person 

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Username', 'user_email', 'Coins')

    def Name(self, obj):
        return obj.First_Name + ' ' +  obj.Last_Name 
    
    def Username(self, obj):
        return obj.Username 

    def user_email(self, obj):
        return obj.Email  

    def Coins(self, obj):
        return obj.Coins 

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('Type', 'item_title', 'item_description', 'item_price', 'item_quantity')

    def item_title(self, obj):
        return obj.Title 
    
    def Type(self, obj):
        return obj.Type  

    def item_description(self, obj):
        return obj.Decription  

    def item_price(self, obj):
        return obj.Price  
    def item_quantity(self, obj):
        return obj.Quantity  

class CardItemsAdmin(admin.ModelAdmin):
    list_display = ('Username', 'item_title', 'item_price', 'total_Items')

    def Username(self, obj):
        return obj.Username 
    
    def item_title(self, obj):
        return obj.Name  
    def item_price(self, obj):
        return obj.Price  
    
    def total_Items(self, obj):
        return obj.Quantity  

class ItemsOrderAdmin(admin.ModelAdmin):
    list_display = ('Username', 'item_title', 'item_price', 'total_Items')

    def Username(self, obj):
        return obj.Username 
    def item_title(self, obj):
        return obj.Name  

    def item_price(self, obj):
        return obj.Price 
    
    def total_Items(self, obj):
        return obj.Quantity 

admin.site.register(Book_Table, Book_TableAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(CardItems, CardItemsAdmin)
admin.site.register(ItemsOrder, ItemsOrderAdmin)
