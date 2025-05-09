import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.calculator import Calculator

def main():
    """Funcion principal para la interfaz.
    """
    st.title("Calculadora")
    st.write("Permite hacer sumas, multiplicaciones y divisiones.")

    operacion = st.selectbox(
        label="Selecciona una opcion",
        options=["Suma", "Multiplicacion", "Division"]
    )

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input("Primer numero", value=1.0)
    
    with col2:
        b = st.number_input("Segundo numero", value=1.0)
    
    if st.button("Calcular"):
        try:
            if operacion == "Suma":
                result = Calculator.add(a, b)
                st.success(f"Resultado {a} + {b} = {result}")

            if operacion == "Multiplicacion":
                result = Calculator.multiply(a,b)
                st.success(f"Resultado: {result}")

            if operacion == "Division":
                result = Calculator.divide(a, b)
                st.success(f"Resultado: {result}")
        
        except ValueError as e:
            st.error(str(e))

if __name__ == "__main__":
    main()