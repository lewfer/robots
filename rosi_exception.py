# Think Create Learn
#
# Think Create Learn
# www.thinkcreatelearn.co.uk 
#
# Exception handlong

# ------------------------------------------------------------------------------------------------------
# Exception to raise if something goes wrong
# ------------------------------------------------------------------------------------------------------
class RosiException(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)


