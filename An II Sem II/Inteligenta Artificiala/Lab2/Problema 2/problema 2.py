#Se dau mai multe imagini (salvate in folder-ul "data/images"). Se cere:

#sa se vizualizeze una din imagini
#daca imaginile nu aceeasi dimensiune, sa se redimensioneze toate la 128 x 128 pixeli si sa se vizualizeze imaginile intr-un cadru tabelar.
#sa se transforme imaginile in format gray-levels si sa se vizualizeze
#sa se blureze o imagine si sa se afiseze in format "before-after"
#sa se identifice muchiile ontr-o imagine si sa se afiseze in format "before-after"
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
import os

image_folder = "images"

# listam imaginile
    #os.listdir() -> se listeaza toate fisierele din folderul specificat
    #os.path.isfile() -> se selecteaza doar fisierele (nu directoarele)
    #rezultatul este o lista cu numele fisierelor de imagini din director
poze = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# alegem prima imagine + vizualizare
path_imagine = os.path.join(image_folder, poze[0])

poza_originala = Image.open(path_imagine)
poza_originala.show()

# Redimensionare la 128x128 pixeli + vizualizare in cadru tabelar
poze_resized = []
for poza in poze:
    image_path = os.path.join(image_folder, poza)
    image = Image.open(image_path)
    poza_resized = image.resize((128, 128))
    poze_resized.append(poza_resized)

fig, axes = plt.subplots(2, len(poze_resized) // 2, figsize=(12, 6)) #creem o figura plot

# cadru tabelar
for i, ax in enumerate(axes.flat):
    ax.imshow(poze_resized[i])
    ax.axis('off')
    ax.set_title(f'Imagine {i+1}')

plt.show()

# Transformare in format grayscale + vizualizare
poze_gri = [ImageOps.grayscale(image) for image in poze_resized]

for i, poza_gri in enumerate(poze_gri, start=1):
    poza_gri.show(title=f'Grayscale {i}')

# Blurring unei imagini + before-after
poza_blur = poze_resized[0].filter(ImageFilter.BLUR)

poza_originala.show(title='Original')
poza_blur.show(title='Blurrată')

# Identificarea muchiilor + afișare before-after
poza_muchii = poze_resized[0].filter(ImageFilter.FIND_EDGES)

poza_originala.show(title='Original')
poza_muchii.show(title='Muchii identificate')
