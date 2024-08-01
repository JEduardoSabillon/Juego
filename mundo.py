import Constantes

class Mundo():
    def __init__(self):
        self.map_tiles = []

    def process_data(self, data, tile_list):
        self.level_length = len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image = tile_list[tile]
                image_rect = image.get_rect()
                image_x = x *Constantes.TILE_SIZE
                image_y = y *Constantes.TILE_SIZE
                image_rect.center = (image_x, image_y)
                tile_data = [image, image_rect, image_x, image_y]
                self.map_tiles.append(tile_data)

    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0], tile[1])