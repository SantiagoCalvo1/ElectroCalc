import numpy as np

class RF:
    """ Define un objeto con todas las funciones relacionadas a RF """

    def equiv_potencia(self, valor, unidad_in, unidad_out=None, ret=False):
        """
        Brinda equivalencias para las mediciones de potencias.
        :param  valor:      numeric (integer or float).
        :param  unidad_in:  str. Posibilidades: dBm, W, mW, uW.
        :param  unidad_out: str. default = None. Posibilidades: dBm, W, mW, uW.
        :param  ret:        bool. True si quiero return numérico y no quiero imprimir. False en caso contrario.
               
        :return:    Si ret == True y unidad_out != None, se devuelve el valor. np.float64.
                    Si ret == False, se imprime el valor.
                    Si ret == True y unidad_out == None. Se devuelve una tupla con todos los valores.
        """
        try:
            # Convierte el valor de str a np.float64
            valor = np.float64(valor)
        except Exception as e:
            print('@param "valor" no es numerico.\nException:', e)
        
        unidad_in = unidad_in.strip().lower()
        # Cálculo de todo a mW, para mantener el código corto
        if unidad_in == 'dbm':
            mW = 10**(valor/10)
            unidad_in = 'dBm'
        elif unidad_in == 'w':
            mW = valor*1000
            unidad_in = 'W'
        elif unidad_in == 'mw':
            mW = valor
            unidad_in = 'mW'
        elif unidad_in == 'uw':
            mW = valor/1000
            unidad_in = 'uW'
        # Si no se escribió ninguna unidad de entrada válida
        else:
            print('El segundo parámetro (unidad_in) no es correcto. Puede ser: "dBm", "W", "mW", "uW".')
            return False
        
        # Cáculo de mW al resto de las unidades
        dBm = 10 * np.log10(mW)
        W = mW / 1000
        uW = mW * 1000
        pW = uW * 1000
        
        # Selección de los returns y los datos de salida  
        if unidad_out != None:
            unidad_out = unidad_out.strip()
        
        if ret == True:
            # No se imprime, sino que se devuelve el valor
            if unidad_out == 'dBm':
                return dBm
            elif unidad_out == 'W':
                return W
            elif unidad_out == 'mW':
                return mW
            elif unidad_out == 'uW':
                return uW
            elif unidad_out == None:
                return (dBm, 'dBm'), (W, 'W'), (mW, 'mW'), (uW, 'uW')
            # Si no se escribió ninguna unidad de salida válida
            else:
                print('El parámetro unidad_out no es correcto. Puede ser: "dBm", "W", "mW", "uW" o dejarse por default ("None").')
                return False
            
        elif ret == False:
            # Se imprime, no se devuelve el valor
            if unidad_out == 'dBm':
                print('%f [%s] = %f [dBm]' %(valor, unidad_in, dBm))
            elif unidad_out == 'W':
                print('%f [%s] = %f [W]' %(valor, unidad_in, W))
            elif unidad_out == 'mW':
                print('%f [%s] = %f [mW]' %(valor, unidad_in, mW))
            elif unidad_out == 'uW':
                print('%f [%s] = %f [uW]' %(valor, unidad_in, uW))
            elif unidad_out == None:
                print('%f [dBm] = %f [W] = %f [mW] = %f [uW] = %f [pW]' %(dBm, W, mW, uW, pW))
            # Si no se escribió ninguna unidad de salida válida
            else:
                print('El parámetro unidad_out no es correcto. Puede ser: "dBm", "W", "mW", "uW" o dejarse por default ("None").')
                return False
        
        else:
            print('El parámetro ret no es correcto. Puede ser: "True", "False" o dejarse por default ("False").')
            return False
    
    
    
    def equiv_ganancia(self, valor, unidad_in, ret=False):
        """
        Uso de la equivalencia de Veces a dB y viceversa para potencia (multiplica x10 en vez de x20 (voltaje)).
        :param  valor:      numeric (integer or float).
        :param  unidad_in:  str. Posibilidades: dB o Veces.
        :param  ret:        bool. True si quiero return numérico y no quiero imprimir. False en caso contrario.
               
        :return:    Si ret == True se devuelve el valor. np.float64.
                    Si ret == False, se imprime el valor.
        """
        try:
            # Convierte el valor de str a np.float64
            valor = np.float64(valor)
        except Exception as e:
            print('@param "valor" no es numerico.\nException:', e)
        
        unidad_in = unidad_in.strip().lower()  
        if unidad_in == 'db':
            unidad_in = 'dB'
            unidad_out = 'Veces'
            dB = valor
            veces = 10**(dB/10)
        elif unidad_in == 'veces':
            unidad_in = 'Veces'
            unidad_out = 'dB'
            veces = valor
            dB = 10 * np.log10(veces)
        # Si no se escribió ninguna unidad de entrada válida
        else:
            print('El segundo parámetro (unidad_in) no es correcto. Puede ser: "dB" o "Veces".')                  
            return False
        
        if ret == True:
            # No se imprime, sino que se devuelve el valor
            if unidad_in == 'dB':
                return veces
            elif unidad_in == 'Veces':
                return dB
            # Si no se escribió ninguna unidad de salida válida
            else:
                print('El segundo parámetro (unidad_in) no es correcto. Puede ser: "dB" o "Veces".')
                return False
            
        elif ret == False:
            # Se imprime, no se devuelve el valor
            if unidad_in == 'dB':
                print('%f [%s] = %f [Veces]' %(dB, unidad_in, veces))
            elif unidad_in == 'Veces':
                print('%f [%s] = %f [dB]' %(veces, unidad_in, dB))
            # Si no se escribió ninguna unidad de salida válida
            else:
                print('El segundo parámetro (unidad_in) no es correcto. Puede ser: "dB" o "Veces".')
                return False    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test(self):
        resultado = True
        resultado = resultado and self.__test_equiv_potencia()
        resultado = resultado and self.__test_equiv_ganancia()
        return resultado
    
    def __test_equiv_potencia(self):
        resultado = True
        # Si la diferencia entre el valor calculado y esperado es mayor a la tolerancia atol=1e-3, no pasa el test
        if not np.allclose(self.equiv_potencia(0, 'dBm', 'mW', True), np.float64(1.0), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_potencia(15, 'dBm', 'mW', True), np.float64(31.622776602), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_potencia(-30, 'dBm', 'mW', True), np.float64(0.001), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_potencia(10, 'mW', 'W', True), np.float64(0.01), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_potencia(0.2, 'W', 'uW', True), np.float64(200000), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_potencia(120, 'uW', 'dBm', True), np.float64(-9.2081875395), rtol=0, atol=1e-3):
            resultado = False
        return resultado
    
    def __test_equiv_ganancia(self):
        resultado = True
        # Si la diferencia entre el valor calculado y esperado es mayor a la tolerancia atol=1e-3, no pasa el test
        if not np.allclose(self.equiv_ganancia(0, 'dB', True), np.float64(1.0), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_ganancia(28, 'dB ', True), np.float64(630.957344480193), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_ganancia(-30, 'db', True), np.float64(0.001), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_ganancia(10, 'Veces', True), np.float64(10), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_ganancia(10, 'veces ', True), np.float64(10), rtol=0, atol=1e-3):
            resultado = False
        return resultado        
