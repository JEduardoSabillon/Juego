import Constantes
import items

obstaculos = [0, 1, 2, 3, 4, 5, 6, 42, 11, 21, 31, 55, 56, 6, 16, 26, 36, 84, 96, 95, 50, 60]

class Mundo():
    def __init__(self):
        self.map_tiles = []
        self.obstaculos_tiles = []
        self.exit_tile = None
        self.lista_item = []

    def process_data(self, data, tile_list, item_imagenes):
        self.level_length = len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image = tile_list[tile]
                image_rect = image.get_rect()
                image_x = x *Constantes.TILE_SIZE
                image_y = y *Constantes.TILE_SIZE
                image_rect.center = (image_x, image_y)
                tile_data = [image, image_rect, image_x, image_y]
                #AGREGAR TILES A OBSTACULOS
                if tile in obstaculos:
                    self.obstaculos_tiles.append(tile_data)
                    #TILE DE SALIDA
                elif tile == 84:
                    self.exit_tile = tile_data

                elif tile == 86:
                    moneda = items.Item(image_x, image_y, 0, item_imagenes[0])
                    self.lista_item.append(moneda)
                    tile_data[0] = tile_list[32]

                elif tile == 88:
                    posion = items.Item(image_x, image_y, 1, item_imagenes[1])
                    self.lista_item.append(posion)
                    tile_data[0] = tile_list[32]

                self.map_tiles.append(tile_data)

    def update(self, posicion_pantalla):
        for tile in self.map_tiles:
            tile[2] += posicion_pantalla[0]
            tile[3] += posicion_pantalla[1]
            tile[1].center = (tile[2], tile[3])

    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0], tile[1])
