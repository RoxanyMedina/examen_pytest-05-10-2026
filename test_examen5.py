import pytest
from examen5 import dividir

# with pytest.raises(ZeroDivisionError): dividir(10,0)
# with pytest.raises(ValueError): dividir(10,0)
#assert dividir(10,0) == ValueError
assert pytest.raises(dividir(10,0))