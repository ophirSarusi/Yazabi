
class Groceries:
    """
    A grocery list with ability to add or remove items, as well as check them off the list.

    """
    def __init__(self):
        """
        Instance is initialized as an empty dictionary.
        """  
        self.grocery_list = {}
        
    def add_item(self,item):
        """
        Adds an item to the grocery list, with value initialized to False.
        
        Args:
            item: the item to be added to the list.
            
        Raises:
            TypeError: If the input is not of type String
        """    
        if type(item) != str :
            raise TypeError('Items to be added must be of type String')
        else:
            self.grocery_list.update({item : False})
        
    def remove_item(self,item):
        """
        Removes an item from the grocery list.
        
        Args:
            item: the item to be removed from the list.
            
        Raises:
            TypeError: If the input is not of type String.
            ValueError: If the item does not exist in the list.
        """    
        if type(item) != str :
            raise TypeError('Items to be added must be of type String')
        elif item not in self.grocery_list:     
            raise ValueError('There is no item named %s in the list' % item)
        else:        
            self.grocery_list.pop(item)
    
    def check_item(self,item):
        """
        Set the value of an item to True to indicate it has been purchased. 
        It does not check if the value is already set to True.
        
        Args:
            item: the item to be checked off the list.
            
        Raises:
            TypeError: If the input is not of type String
            ValueError: If the item does not exist in the list.
        """    
        if type(item) != str :
            raise TypeError('Items to be checked must be of type String')
        elif item not in self.grocery_list:     
            raise ValueError('There is no item named %s in the list' % item)
        else:            
            self.grocery_list.update({item : True})
        
    def items_remaining(self):
        """
        Returns the number of unchecked items (False as the value) on the list
        
        Returns: The number of unchecked items on the list
            
        """    
        return sum([1 for x in self.grocery_list.values() if x==False])
        