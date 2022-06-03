import microbit

lista_zaswiecania = [(0,0), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4), (0,3), (0,2), (0,1)]
index = 0
aktualney = 0
aktualnex = 0
while True:
    microbit.display.set_pixel(aktualnex,aktualney, 0)
    (aktualnex, aktualney) = lista_zaswiecania[index]

    microbit.display.set_pixel(aktualnex,aktualney, 5)

    index += 1
    if index == len(lista_zaswiecania):
        index = 0
    microbit.sleep(300)