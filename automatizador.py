# Nuestro primer software de automatización para negocios
import datetime

# 1. Simulamos una base de datos de clientes de un negocio local
clientes = [
    {"nombre": "Juan Pérez", "producto": "Diseño Web", "saldo_pendiente": 0, "telefono": "+595981000000"},
    {"nombre": "María Galeano", "producto": "Mantenimiento PC", "saldo_pendiente": 150000, "telefono": "+595971111111"},
    {"nombre": "Carlos Benítez", "producto": "Sistema Apache", "saldo_pendiente": 300000, "telefono": "+595961222222"},
]

print("=== SISTEMA DE AUTOMATIZACIÓN DE COBROS ===")
print(f"Fecha del reporte: {datetime.date.today()}\n")

# 2. El algoritmo busca automáticamente quién tiene deudas pendientes
print("Buscando deudores en la base de datos...")
print("-" * 45)

for cliente in clientes:
    if cliente["saldo_pendiente"] > 0:
        # Genera el mensaje personalizado de cobro de forma automática
        mensaje_whatsapp = f"Hola {cliente['nombre']}, te saludamos de IT-Soluciones. Te recordamos que tienes un saldo pendiente de {cliente['saldo_pendiente']} Gs. por el servicio de {cliente['producto']}."
        
        print(f"⚠️ CLIENTE CON DEUDA DETECTADO: {cliente['nombre']}")
        print(f"📱 Enviar a: {cliente['telefono']}")
        print(f"💬 Mensaje listo para enviar: '{mensaje_whatsapp}'")
        print("-" * 45)

print("¡Reporte generado con éxito! Listo para exportar.")