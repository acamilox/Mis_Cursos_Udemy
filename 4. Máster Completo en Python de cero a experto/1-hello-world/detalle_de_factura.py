def generar_detalle(nombre_factura: str, precio_1: float, precio_2: float) -> str:
    total_bruto = precio_1 + precio_2
    impuesto = total_bruto * 0.19  # 19% de IVA
    total_neto = total_bruto + impuesto

    detalle = f"La factura {nombre_factura} tiene un total bruto de {total_bruto:.2f}, con un impuesto de {impuesto:.2f} y el monto después de impuesto es de {total_neto:.2f}"

    return detalle

if __name__ == "__main__":
    resultado = generar_detalle("Compra supermercado", 2500.0, 2241.25)
    print(resultado)