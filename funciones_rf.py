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
                print('%f [dBm] = %f [W] = %f [mW] = %f [uW]' %(dBm, W, mW, uW))
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
    
    
    
    def equiv_RL_VSWR_Z_Gamma(self, valor, medida_in, medida_out=None, ret=False):
        """
        Uso de la equivalencia de Pérdida de Retorno (dB) a VSWR a Impedancia (Ohm) a Coeficiente de Reflexión.
        Impedancia de referencia Z0 = 50 Ohm
        :param  valor:      numeric (integer or float).
        :param  medida_in:  str. Posibilidades: RL, VSWR, ZL, Gamma.
        :param  medida_out: str. default = None. Posibilidades: RL, VSWR, ZL, Gamma.
        :param  ret:        bool. True si quiero return numérico y no quiero imprimir. False en caso contrario.
               
        :return:    Si ret == True y medida_out != None, se devuelve el valor. np.float64.
                    Si ret == False, se imprime el valor.
                    Si ret == True y medida_out == None. Se devuelve una tupla con todos los valores.
        """        
        try:
            # Convierte el valor de str a np.float64
            valor = np.float64(valor)
        except Exception as e:
            print('@param "valor" no es numerico.\nException:', e)
        # Impedancia de referencia
        z0 = 50
        medida_in = medida_in.strip().lower()
        # Cálculo de todo a Coeficiente de Reflexión(Gamma), para mantener el código corto
        try:
            if medida_in == 'gamma':
                if valor < -1 or valor > 1:
                    print('Error: 0 < gamma < 1')
                gamma = valor
                medida_in = 'Gamma'
            elif medida_in == 'vswr':
                vswr = valor
                gamma = np.abs((vswr-1)/(vswr+1))
                medida_in = 'VSWR'
            elif medida_in == 'zl' or medida_in == 'zl(ohm)' or medida_in == 'zl[ohm]':
                zl = valor
                gamma = np.abs((zl-z0)/(zl+z0))
                medida_in = 'ZL[Ohm]'
            elif medida_in == 'rl' or medida_in == 'rl(db)' or medida_in == 'rl[db]':
                rl = valor
                gamma = np.abs(10**(-np.abs(rl)/20))
                medida_in = 'RL[dB]'
            # Si no se escribió ninguna medida de entrada válida
            else:
                print('El segundo parámetro (medida_in) no es correcto. Puede ser: "Gamma", "VSWR", "ZL", "RL".')
                return False
            
            # Cáculo de Coeficiente de Reflexión al resto de las unidades
            vswr = (1 + gamma) / (1 - gamma)
            zl_1 = z0 * (1+gamma) / (1-gamma)
            zl_2 = z0 * (1-gamma) / (1+gamma)
            rl = -20 * np.log10(gamma)
        except:
            # La excepción es la división por cero
            pass
        # Selección de los returns y los datos de salida  
        if medida_out != None:
            medida_out = unidad_out.strip()
        
        if ret == True:
            # No se imprime, sino que se devuelve el valor
            if medida_out == 'VSWR':
                return vswr
            elif medida_out == 'ZL[Ohm]':
                return zl_1, zl_2
            elif medida_out == 'RL[dB]':
                return rl
            elif medida_out == 'Gamma':
                return gamma
            elif medida_out == None:
                return (vswr, 'VSWR'), (zl_1, zl_2, 'ZL[Ohm]'), (rl, 'RL[dB]'), (gamma, 'Gamma')
            # Si no se escribió ninguna unidad de salida válida
            else:
                print('El parámetro medida_out no es correcto. Puede ser: "Gamma", "VSWR", "ZL", "RL" o dejarse por default ("None").')
                return False
            
        elif ret == False:
            # Se imprime, no se devuelve el valor
            if medida_out == 'VSWR':
                print('%f [%s] = %f (VSWR)' %(valor, medida_in, vswr))
            elif medida_out == 'ZL[Ohm]':
                print('%f [%s] = %f [Ohm] == %f [Ohm]' %(valor, medida_in, zl_1, zl_2))
            elif medida_out == 'RL[dB]':
                print('%f [%s] = %f [dB]' %(valor, medida_in, rl))
            elif medida_out == 'Gamma':
                print('%f [%s] = %f (Gamma)' %(valor, medida_in, gamma))
            elif medida_out == None:
                print('%f (VSWR) = %f [Ohm] == %f [Ohm] = %f [dB] = %f (Gamma)' %(vswr, zl_1, zl_2, rl, gamma))
            # Si no se escribió ninguna unidad de salida válida
            else:
                print('El parámetro medida_out no es correcto. Puede ser: "Gamma", "VSWR", "ZL", "RL" o dejarse por default ("None").')
                return False
        
        else:
            print('El parámetro ret no es correcto. Puede ser: "True", "False" o dejarse por default ("False").')
            return False    
    
    
    
    def microtira_analisis(self, w, Er, h, l=0, t=0, unidad='mm'):
        """ Fórmulas de Hammerstad para análisis """
        try:
            # Convierte el w de str a np.float64
            w = np.float64(w)
        except Exception as e:
            print('@param "w" no es numerico.\nException:', e)
        try:
            # Convierte el l de str a np.float64
            l = np.float64(l)
        except Exception as e:
            print('@param "l" no es numerico.\nException:', e)
        try:
            # Convierte Er de str a np.float64
            Er = np.float64(Er)
        except Exception as e:
            print('@param "Er" no es numerico.\nException:', e)
        try:
            # Convierte el h de str a np.float64
            h = np.float64(h)
        except Exception as e:
            print('@param "h" no es numerico.\nException:', e)
        try:
            # Convierte el t de str a np.float64
            t = np.float64(t)
        except Exception as e:
            print('@param "t" no es numerico.\nException:', e)
        # Impedancia de referencia
        z0 = 50
        unidad = unidad.strip().lower()
        """
        if unidad == 'mil' or unidad == 'mils':
            w = self.mil_a_mm(w)
            l = self.mil_a_mm(l)
            h = self.mil_a_mm(h)
            t = self.mil_a_mm(t)
        elif unidad == 'mm':
            pass
        else:
            print('@param "unidad" no es válido. Las opciones posibles son mil y mm (default)')
            return False
        """
        # Cálculo de la impedancia
        if w/h < 1:
            Er_prima = (Er+1)/2 + (Er-1)/2 * ((1/np.sqrt(1+12*h/w)) + 0.04*(1-w/h)**2)
            z0 = 60/np.sqrt(Er_prima) * np.log(8*h/w + w/(4*h))
        else: #w/h >= 1
            Er_prima = (Er+1)/2 + (Er-1)/2 * (1/np.sqrt(1+12*h/w))
            z0 = 120*np.pi/np.sqrt(Er_prima) / (w/h + 1.393 + 0.667*np.log(1.444 + w/h))

        print('Z0 = %f' %(z0))
    
        
    
    def mil_a_mm(self, mil):
        """ 
        Calcula el equivalente en mm de X mils 
        :param mil: numeric, la longitud a convertir
        :return mm: numeric, la longitud en mm
        """
        try:
            mil = np.float64(mil)
        except Exception as e:
            print('@param "mil" no es numerico.\nException:', e)
        mm = mil * 0.0254
        return mm


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
