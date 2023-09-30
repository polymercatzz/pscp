"""iPad Air"""
def main(color, stroage, wifi):
    """iPad Air"""
    capa = {64:19900, 256:24900}
    wifi_sto = {"Wi-Fi":0, "Wi-Fi + Cellular":4500}
    if color not in ['Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue'] or \
        wifi_sto.get(wifi, 1) == 1 or capa.get(stroage, 0) == 0:
        print("Not Available")
    else:
        print(wifi_sto[wifi]+capa[stroage])
main(input(), int(input()), input())
