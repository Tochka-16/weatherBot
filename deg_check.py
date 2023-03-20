#this function determines the wind direction by degrees
def determineWind (deg):
    if deg % 90 == 0:    
        if deg == 0 or deg == 360: 
            return 'северный'

        elif deg == 90:
            return 'восточный'
        
        elif deg == 180:
            return 'южный'
        
        elif deg == 270:
            return 'западный'
        
    elif deg > 0 and deg < 90:
        return 'северо-западный'
    
    elif deg > 90 and deg < 180:
        return 'юго-восточный'
    
    elif deg > 180 and deg < 270:
        return 'юго-западный'
    
    elif deg > 270 and deg < 360:
        return 'северо-западный'   
    
