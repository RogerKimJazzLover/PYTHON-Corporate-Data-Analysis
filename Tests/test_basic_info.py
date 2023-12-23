import pytest
import sys
sys.path.append('./')

#THIS 'API_KEYS' IS A PYTHON FILE OF MINE THAT SOTERS MY PRIVATE API KEYS.
from API_KEYS import * #SO DELETE THIS LINE!!!!!
 
#IMPORTING THE FILES
import get_basic_info
import manipulate_basic_info

def test_everything_work():
    get_basic_info.main()
    manipulate_basic_info.main()