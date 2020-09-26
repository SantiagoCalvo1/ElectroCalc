import numpy as np

class RF:
    """ Define un objeto con todas las funciones relacionadas a RF """

    def equiv_potencia(self, valor, unidad_in, unidad_out=None, ret=False):
        """
        Brinda equivalencias para las mediciones de potencias.
        :param  valor:      numeric (integer or float).
        :param  unidad_in:  str. Posibilidades: dBm, W, mW, uW, nW, pW.
        :param  unidad_out: str. default = None. Posibilidades: dBm, W, mW, uW, nW, pW.
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
        
        unidad_in = unidad_in.strip()
        # Cálculo de todo a mW, para mantener el código corto
        if unidad_in == 'dBm':
            mW = 10**(valor/10)
        elif unidad_in == 'W':
            mW = valor*1000
        elif unidad_in == 'mW':
            mW = valor
        elif unidad_in == 'uW':
            mW = valor/1000
        elif unidad_in == 'pW':
            mW = valor/1000000
        # Si no se escribió ninguna unidad de entrada válida
        else:
            print('El segundo parámetro (unidad_in) no es correcto. Puede ser: "dBm", "W", "mW", "uW", "pW".')
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
            elif unidad_out == 'pW':
                return pW
            elif unidad_out == None:
                return (dBm, 'dBm'), (W, 'W'), (mW, 'mW'), (uW, 'uW'), (pW, 'pW')
            # Si no se escribió ninguna unidad de salida válida
            else:
                print('El parámetro unidad_out no es correcto. Puede ser: "dBm", "W", "mW", "uW", "pW" o dejarse por default ("None").')
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
            elif unidad_out == 'pW':
                print('%f [%s] = %f [pW]' %(valor, unidad_in, pW))
            elif unidad_out == None:
                print('%f [dBm] = %f [W] = %f [mW] = %f [uW] = %f [pW]' %(dBm, W, mW, uW, pW))
            # Si no se escribió ninguna unidad de salida válida
            else:
                print('El parámetro unidad_out no es correcto. Puede ser: "dBm", "W", "mW", "uW", "pW" o dejarse por default ("None").')
                return False
        
        else:
            print('El parámetro ret no es correcto. Puede ser: "True", "False" o dejarse por default ("False").')
            return False
    
    
    
    def equiv_ganancia(self, valor, unidad_in, unidad_out=None, ret=False):
        try:
            # Convierte el valor de str a np.float64
            valor = np.float64(valor)
        except Exception as e:
            print('@param "valor" no es numerico.\nException:', e)
        
        unidad_in = unidad_in.strip()
        # Cálculo de todo a mW, para mantener el código corto    
        if unidad_in == 'dB':
            veces = 
    
    
    
    
    def test(self):
        resultado = self.__test_equiv_potencia()
        return resultado
    
    def __test_equiv_potencia(self):
        resultado = True
        # Si la diferencia entre el valor calculado y esperado es mayor a la tolerancia atol=1e-3, no pasa el test
        if not np.allclose(self.equiv_potencia(0, 'dBm', 'mW', True), np.float64(1.0), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_potencia(10, 'dBm', 'mW', True), np.float64(10.0), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_potencia(15, 'dBm', 'mW', True), np.float64(31.622776602), rtol=0, atol=1e-3):
            resultado = False
        if not np.allclose(self.equiv_potencia(-30, 'dBm', 'mW', True), np.float64(0.001), rtol=0, atol=1e-3):
            resultado = False
        return resultado
