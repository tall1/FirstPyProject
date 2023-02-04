class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = int((self._red + self._green + self._blue) / 3)
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        not_zero_color = ""
        if self._red == 0 and self._green == 0 and self._blue > 50:
            not_zero_color = "Blue"
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            not_zero_color = "Green"
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            not_zero_color = "Green"

        print("X: " + str(self._x) + ", Y: " + str(self._y) + ", Color: (" + str(self._red) + ", " + str(
            self._green) + ", " + str(
            self._blue) + ") " + not_zero_color)


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


main()
