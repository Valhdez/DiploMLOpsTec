
### Esta funcion ya tiene todos los requierimientos de la actividad
def resta(num1, num2):
  try:
     num1_str = str(num1)
     num2_str = str(num2)

     if num2_str == '0':
       print("La division entre 0 es matematicamente imposible")
      
     else:
       if "/" in num1_str:
          numerador_1 = float(num1_str.strip('/')[0])
          denominador_1 = float(num1_str.strip('/')[2])
          primer_numero = numerador_1 / denominador_1
       else : 
          primer_numero = float(num1_str)
      
       if "/" in num2_str:
          numerador_2 = float(num2_str.strip('/')[0])
          denominador_2 = float(num2_str.strip('/')[2])
          segundo_numero = numerador_2 / denominador_2
       else : 
          segundo_numero = float(num2_str)

          resultado = primer_numero - segundo_numero
          return resultado
  except:
      print( "Argumento Invalido")