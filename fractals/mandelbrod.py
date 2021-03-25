

def mandel_func(c, z = 0, r = 0):
    """Toma la distancia desde el centro de la pantalla hasta el punto c y la z como argumento que cambia el fractal (r siempre= 0)"""
    
    if r > 50 or abs(z) >= 2:
        return r
    else:
        r += 1
        return mandel_func(c, z*z + c , r)

