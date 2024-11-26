import kernel
import matplotlib.pyplot as plt
import numpy as np
import skimage as ski
from skimage import io

#wczytanie obrazu z dysku w skali szarości
image_array=ski.io.imread('building.jpg', True)


#MODYFIKATORY
#nowa wielkość obrazu. program wykonuje tylko resizing dla liczb naturalnych oraz obrazów kwadratowych
l=5 #rozmiar jądra uśredniającego
step=1/2 #ilość kroków tzn. ile razy obraz ma zostać zresizowany (dodatnie - zmniejszenie, ujemne - powiększenie)
k=int(len(image_array)/step)



#tablica do wykorzystania jako jądro uśredniające
averaging_array=np.zeros((l,l))
#tablica do której zostanie zapisany obraz
resized_array=np.zeros((k,k))

#warunek, decydujący czy obraz będzie zwiększany, czy zmniejszany
if k < len(image_array):

    # zmienne potrzebne do obsługi pętli
    starting_point = [0, 0]
    current_point = [0, 0]
    x_point = 0
    y_point = 0

    while starting_point[0]<len(image_array): #poruszanie się po wymiarze 0 oryginalnego obrazu

        starting_point[1]=0

        while starting_point[1]<len(image_array): #poruszanie się po wymiarze 1 oryginalnego obrazu
            temp_array = averaging_array.copy()

            for i in range(len(averaging_array)):
                for j in range(len(averaging_array)): #poruszanie się po jądrze uśredniającym
                        temp_array[i,j]=image_array[current_point[0]][current_point[1]]
                        current_point[0] = starting_point[0] + 1

                current_point[0] = starting_point[0]
                current_point[1] = starting_point[1] + 1

            average = (np.sum(temp_array)) / (len(temp_array) * len(temp_array)) #oblliczanie średniej z jądra uśredniającego
            resized_array[x_point,y_point] = average #zapisanie uzyskanej wartości do tablicy z przeskalowanym obrazem

            #ustalanie markerów do kolejnego przejścia pętli
            current_point[1] = 0 #]
            x_point=int(starting_point[0]/step)
            y_point=int(starting_point[1]/step)
            starting_point[1] += step
        starting_point[0] += step

    # pokazanie obrazu
    plt.imshow(resized_array)
    plt.show()

elif k > len(image_array):
    index_array = np.arange(0,len(image_array)-1,1)
    temp_array=resized_array.copy()

    for i in range(k):
        resized_array[i,:] = kernel.h1(index_array,temp_array[i,:],image_array[i,:],)
        print('Row Done!')

    mod_index_array = np.arange(0,k,1)
    temp_array=resized_array.copy()

    for j in range(k):
        resized_array[:,j] = kernel.h1(mod_index_array,temp_array[:,j],resized_array[:,j])
        print('Column Done!')

    plt.imshow(resized_array)
    plt.show()


else:
    #warunek graniczny, kiedy użytkownik wybierze rescaling obrazu o 1
    plt.imshow(image_array)
    plt.show()





