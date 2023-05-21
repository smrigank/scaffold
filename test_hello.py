from hello import toyou, add, subtract

def test_add():
    assert(add(10)) == 11
    
def test_subtract():
    assert(subtract(10)) == 9
    
def test_toyou():
    assert(toyou("Mrigank")) == "hi Mrigank"