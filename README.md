### **Proyecto de Pruebas Automatizadas – Urban Routes**  

---

## **1. Descripción General**  
Este proyecto tiene como objetivo la automatización de pruebas para la aplicación *Urban Routes*, utilizada para solicitar taxis, configurar tarifas, agregar métodos de pago y administrar viajes.  

Se emplea *Selenium WebDriver* para simular la interacción con la interfaz web, permitiendo la validación de procesos clave como la configuración de direcciones, la selección de tarifas y la gestión de pagos.  

---

## **2. Tecnologías Utilizadas**  
🔹 **Selenium WebDriver** – Automatización de pruebas en la interfaz de usuario.  
🔹 **Python** – Lenguaje de programación para la escritura de pruebas.  
🔹 **pytest** – Framework para la ejecución y gestión de pruebas.  
🔹 **WebDriverWait** – Manejo de esperas dinámicas para la carga de elementos.  

---

## **3. Estructura del Proyecto**  
📂 **data.py** – Contiene configuraciones como direcciones, números de teléfono y datos de pago.  
📂 **main.py** – Lógica principal de las pruebas (configuración de direcciones, selección de tarifas, pagos, etc.).  
📂 **Pages.py** – Define la clase `UrbanRoutesPage` con métodos y localizadores de la aplicación.  
📂 **Helpers.py** – Funciones auxiliares, como la recuperación de códigos de verificación (`retrieve_phone_code()`).  

---

## **4. Pasos para Ejecutar las Pruebas**  
✅ **Instalar dependencias:**  
Ejecutar el siguiente comando para instalar los paquetes necesarios:  
```bash
pip install -r requirements.txt
```  

✅ **Configurar Selenium:**  
Asegurar la instalación del *WebDriver* adecuado para el navegador (por ejemplo, *chromedriver* para Chrome).  

✅ **Ejecutar pruebas:**  
Ejecutar las pruebas con el siguiente comando:  
```bash
pytest main.py
```  

✅ **Validar resultados:**  
Se espera que todas las pruebas se ejecuten con éxito, verificando la funcionalidad de la aplicación.  

---

## **5. Escenarios de Prueba**  
🔹 **Configuración de direcciones** – Establecimiento de origen y destino.  
🔹 **Selección de tarifa Comfort** – Verificación de tarifas.  
🔹 **Ingreso de número de teléfono** – Introducción de número válido y recepción de código.  
🔹 **Añadir tarjeta de crédito** – Registro de datos de pago.  
🔹 **Mensaje al conductor** – Envío de mensaje en el campo correspondiente.  
🔹 **Solicitud de artículos adicionales** – Pedido de mantas, pañuelos y helados.  
🔹 **Asignación del conductor** – Validación del modal con información del conductor y cuenta regresiva.  

---

## **6. Implementación del Patrón Page Object Model (POM)**  
Para mejorar la organización y mantenimiento del código, se ha aplicado el patrón *Page Object Model (POM)*, estructurando los elementos de la interfaz de usuario en clases independientes. Esto facilita la reutilización del código y mejora su legibilidad.  
