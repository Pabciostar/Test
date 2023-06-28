def total_pago(cant_1, cant_2, cant_3, cant_4):
    valor_1 = 1500
    valor_2 = 1800
    valor_3 = 1600
    valor_4 = 1700
    total = cant_1*valor_1 + cant_2*valor_2 + cant_3*valor_3 + cant_4*valor_4
    if total >= 3000:
        descuento = total*0.1
    total_descuento = total - descuento
    return(total_descuento)
