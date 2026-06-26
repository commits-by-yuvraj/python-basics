class Chef:

    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes special dish")


# ChineseChef inherits from Chef
class ChineseChef(Chef):

    # Overrides the parent's method
    def make_special_dish(self):
        print("The chef makes orange chicken")

    # New method only for ChineseChef
    def make_fried_rice(self):
        print("The chef makes fried rice")


myChef = Chef()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_salad()


# ---------------- Notes ----------------

# ChineseChef(Chef) -> ChineseChef inherits from Chef.
# ChineseChef can use all methods of Chef.
# It can also:
#   1. Override a parent method.
#   2. Add new methods.

# Parent object -> Only parent methods.
# Child object  -> Parent methods + Child methods.

# Example:
# myChineseChef.make_salad()        # Inherited
# myChineseChef.make_special_dish() # Overridden
# myChineseChef.make_fried_rice()   # Child's own method