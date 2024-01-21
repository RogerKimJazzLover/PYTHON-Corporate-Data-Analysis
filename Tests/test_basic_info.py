import pytest
import sys
sys.path.append('./')

#THIS 'API_KEYS' IS A PYTHON FILE OF MINE THAT SOTERS MY PRIVATE API KEYS.
from API_KEYS import * #SO DELETE THIS LINE!!!!!
 
#IMPORTING THE FILES
import create_basic_info
import create_bf_for_analysis

def test_everything_work():
    create_basic_info.main()
    create_bf_for_analysis.main()