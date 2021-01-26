temperature = \
    [30.75, 30.25, 29.75, 30.00, 29.00, 28.50, 29.75, 30.25,
     29.25, 28.75, 28.50, 29.25, 28.75, 28.50, 29.00, 29.25,
     27.25, 27.50, 27.75, 28.25, 28.25, 28.00, 28.50, 29.00,
     28.25, 28.25, 28.25, 28.25, 28.25, 28.75, 28.50, 28.00,
     27.00, 27.75, 27.75, 28.00, 28.50, 28.75, 28.50, 27.75,
     27.25, 28.00, 27.25, 28.00, 27.75, 27.50, 27.00, 29.50,
     26.75, 27.00, 26.75, 27.00, 27.50, 26.75, 27.50, 28.00,
     26.75, 26.75, 26.50, 25.50, 26.75, 26.75, 26.25, 29.25,
     ]

import numpy
import cv2
class VEVER_TTEPLOVIZOR:

    def convert(self, temperature):
        array = []
        temp = []
        id = 0
        for count, i in enumerate(temperature):
            if id == 8:
                array.append(temp)
                temp = []
                id = 0
            else:
                id = id + 1
                temp.append(i)
        return numpy.array(array)

    def show(self, temperature, DEBUG=False):

        heatmap = self.convert(temperature)
        heatmap = cv2.resize(heatmap, (500, 500))

        heatmapshow = None
        heatmapshow = cv2.normalize(heatmap, heatmapshow, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        heatmapshow = cv2.applyColorMap(heatmapshow, cv2.COLORMAP_JET)
        if DEBUG:
            cv2.imshow("Heatmap", heatmapshow)
            cv2.waitKey(0)
            cv2.waitKey()
        return heatmapshow

if __name__ == '__main__':

    temperature = \
        [30.75, 30.25, 29.75, 30.00, 29.00, 28.50, 29.75, 30.25,
         29.25, 28.75, 28.50, 29.25, 28.75, 28.50, 29.00, 29.25,
         27.25, 27.50, 27.75, 28.25, 28.25, 28.00, 28.50, 29.00,
         28.25, 28.25, 28.25, 28.25, 28.25, 28.75, 28.50, 28.00,
         27.00, 27.75, 27.75, 28.00, 28.50, 28.75, 28.50, 27.75,
         27.25, 28.00, 27.25, 28.00, 27.75, 27.50, 27.00, 29.50,
         26.75, 27.00, 26.75, 27.00, 27.50, 26.75, 27.50, 28.00,
         26.75, 26.75, 26.50, 25.50, 26.75, 26.75, 26.25, 29.25,
         ]
    test = VEVER_TTEPLOVIZOR()
    test.show(temperature)