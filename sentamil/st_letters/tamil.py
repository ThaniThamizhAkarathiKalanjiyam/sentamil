#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      muthukumaran
#
# Created:     13/04/2019
# Copyright:   (c) muthukumaran 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import st_encode.types as encd

def getTamilLetters(encod_type = encd.UTF8):
    if(encod_type == encd.UTF8):
        print "UTF8"
    else:
        print "TACE16"
    return

