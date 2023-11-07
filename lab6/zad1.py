import math

from sklearn import preprocessing
import numpy as np
siatka = np.array([[23, 75, 176, 1],
                  [25, 67, 180, 1],
                  [28, 120, 175, 0],
                  [22, 65, 165, 1],
                  [46, 70, 187, 1],
                  [50, 68, 180, 0],
                  [48, 97, 178, 0]])

normalized_siatka = preprocessing.normalize([siatka])
print(normalized_siatka)

def forward_pass(wiek, waga, wzrost):
    hidden1 = wiek * (-0.46122) + waga * 0.97314 + wzrost * (-0.39203) + 0.80109
    hidden1_po_aktywacji = 1/(1+math.e**hidden1)
    hidden2 = wiek * 0.78548 + waga * 2.10584 + wzrost * (-0.57847) + 0.43529
    hidden2_po_aktywacji = 1/(1+math.e**hidden2)
    output = (hidden1_po_aktywacji * (-0.81546) + hidden2_po_aktywacji * 1.03775) + (-0.2368)
    return output


print(forward_pass(23, 75, 176))
