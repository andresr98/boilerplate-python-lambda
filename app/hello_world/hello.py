import settings
import numpy as np

def create_message():
    final_message = "No se ha establecido un valor para la variable de ambiente MESSAGE"

    if settings.MESSAGE != None:
        final_message = "El valor de MESSAGE es: " + settings.MESSAGE
    return final_message
