## `oh-the-places-youll-go` -- desafío OSINT inspirado en "Geo Detective"
---

## Parte 1 (`DUOC{triangulacion_visual_urbana_78245}`)

Las primeras 11 imágenes muestran porciones de algunos de los monumentos más famosos del mundo, capturados por la cobertura oficial de Google Street View. La brújula en la parte superior de cada imagen indica la dirección general hacia el monumento. Utilizando la escala aparente de la estructura se puede estimar la distancia, y al inspeccionar las calles compatibles se identifica la ubicación exacta gracias a los elementos visuales presentes. Una vez localizados todos los puntos, se ensambla la palabra "CALL" y un número telefónico a partir del mapa para obtener la primera flag (`DUOC{triangulacion_visual_urbana_78245}`).

`map.jpg` - La pista sobre cómo ensamblar el mensaje oculto de cada imagen
![map](imgs/small_map_crop.png)

`img_0001.jpg` - Nueva York, mirando hacia Times Square -- "call" en "calling"
![image 1 "call"](imgs/small_orig_ny_call.jpg)
[Link to Google Maps](https://www.google.com/maps/@40.7576889,-73.9858065,3a,83.3y,29.16h,116.05t/data=!3m7!1e1!3m5!1suW_eUGvspzGFVjN_Vy2vfQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-26.047572807065833%26panoid%3DuW_eUGvspzGFVjN_Vy2vfQ%26yaw%3D29.157001408725435!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwOC4wIKXMDSoASAFQAw%3D%3D)

`img_0002.jpg` - Roma, mirando hacia el Coliseo -- "8" en "2018"
![image 2 "8"](imgs/small_orig_colle_8.jpg)
[Enlace a Google Maps](https://www.google.com/maps/place/S.+Gregorio/@41.8922026,12.4904373,3a,75y,184.95h,83.77t/data=!3m7!1e1!3m5!1swv8qEZM8bxd4nO7CORdgbQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D6.226083335339922%26panoid%3Dwv8qEZM8bxd4nO7CORdgbQ%26yaw%3D184.95013306142448!7i16384!8i8192!4m6!3m5!1s0x132f61b60285dc37:0x566e3a2693bd021d!8m2!3d41.8875048!4d12.4901711!16s%2Fg%2F12vsgzzml?entry=ttu&g_ep=EgoyMDI1MDQwNy4wIKXMDSoASAFQAw%3D%3D)

`img_0003.jpg` - París, mirando hacia la Torre Eiffel -- "0" en "30"
![image 3 "0"](imgs/small_orig_paris_0.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@48.856967,2.2919587,3a,75y,56.2h,73.53t/data=!3m7!1e1!3m5!1s7MNBZyPxAuHxLFDXgBJcPg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D16.466109134130335%26panoid%3D7MNBZyPxAuHxLFDXgBJcPg%26yaw%3D56.19639256096559!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwNy4wIKXMDSoASAFQAw%3D%3D)

`img_0004.jpg` - Londres, mirando hacia el Tower Bridge -- "1" en el número de serie del tractor
![image 4 "1"](imgs/small_orig_lon_1.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@51.5070572,-0.0757421,3a,75.4y,154.09h,104.47t/data=!3m7!1e1!3m5!1sUpvOHBL_dHPIaRf3Wmdo0Q!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-14.470301520502716%26panoid%3DUpvOHBL_dHPIaRf3Wmdo0Q%26yaw%3D154.0854114789515!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwOC4wIKXMDSoASAFQAw%3D%3D)

`img_0005.jpg` - Chichén Itzá, frente a un puesto en el camino norte/sur del mercado -- 9 en la camiseta
![image 5 "9"](imgs/small_orig_chich_9.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@20.6855829,-88.5681538,3a,75y,324.79h,70.23t/data=!3m7!1e1!3m5!1srjlSLJn8CmXSs_O63QLNfA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D19.77258179863219%26panoid%3DrjlSLJn8CmXSs_O63QLNfA%26yaw%3D324.785484721884!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDQwNi4wIKXMDSoASAFQAw%3D%3D)

`img_0006.jpg` - Necrópolis de Guiza, mirando hacia la Gran Esfinge -- "zero" en el cartel de Coke Zero
![image 6 "0"](imgs/small_orig_pyra_0.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@29.975454,31.1389447,2a,90y,272.66h,79.5t/data=!3m7!1e1!3m5!1s6ewxCJI3yR9TEFlSrKChrw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D10.497760982264126%26panoid%3D6ewxCJI3yR9TEFlSrKChrw%26yaw%3D272.65777164840256!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDQwNi4wIKXMDSoASAFQAw%3D%3D)

`img_0007.jpg` - San Francisco, Market Street mirando hacia el Ferry Building -- "one" en la señal "one way"
![image 7 "1"](imgs/small_orig_sf_1.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@37.7929636,-122.3968152,3a,74y,44.2h,92.6t/data=!3m7!1e1!3m5!1s8W6HqxG5dAhi4WWBNdYuPQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-2.6001081171146723%26panoid%3D8W6HqxG5dAhi4WWBNdYuPQ%26yaw%3D44.202151997949365!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwNi4wIKXMDSoASAFQAw%3D%3D)

`img_0008.jpg` - Dharmapuri, mirando hacia el Taj Mahal -- "O" en "NO ENTRY"
![image 8 "0"](imgs/small_orig_tajm_0.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@27.1744571,78.0422471,2a,45y,324.22h,92.15t/data=!3m7!1e1!3m5!1s-cCtXZDBsQ8dZPSi_jI2Aw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-2.1506750902047713%26panoid%3D-cCtXZDBsQ8dZPSi_jI2Aw%26yaw%3D324.2230564598831!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDQwNi4wIKXMDSoASAFQAw%3D%3D)

`img_0009.jpg` - Tokio, en el cruce peatonal de Shibuya -- 8 en "Ushi8"
![image 9 "8"](imgs/small_orig_toky_8.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@35.6594944,139.7007025,3a,66.8y,295.85h,107.88t/data=!3m7!1e1!3m5!1sRaNoutOgDdz7nABPid3adw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-17.882381664348273%26panoid%3DRaNoutOgDdz7nABPid3adw%26yaw%3D295.85088149921233!7i16384!8i8192!4m6!3m5!1s0x60188bcaeb0cd12b:0x20e563a2e0aec969!8m2!3d35.659482!4d139.7005596!16s%2Fg%2F11shy4scrj?entry=ttu&g_ep=EgoyMDI1MDQwOC4wIKXMDSoASAFQAw%3D%3D)

`img_0010.jpg` - Sídney, mirando hacia la Ópera de Sídney -- "3" en "3.6m"
![image 10 "3"](imgs/small_orig_syd_3.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@-33.8576952,151.2142861,2a,23.5y,77.86h,109.47t/data=!3m10!1e1!3m8!1smH57MBnD6z1VusFNzvrEoA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-19.46639854156443%26panoid%3DmH57MBnD6z1VusFNzvrEoA%26yaw%3D77.85527896648036!7i13312!8i6656!9m2!1b1!2i27?entry=ttu&g_ep=EgoyMDI1MDQwNy4wIKXMDSoASAFQAw%3D%3D)

`img_0011.jpg` - Las Vegas, mirando hacia el hotel The Flamingo -- "4" en "$5.49"
![image 11 "4"](imgs/small_orig_lv_4.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@36.1154347,-115.1727489,3a,75y,81.89h,96.8t/data=!3m7!1e1!3m5!1sOKVQSiS-NwCtb3Rq6Z6VHg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-6.795093560444371%26panoid%3DOKVQSiS-NwCtb3Rq6Z6VHg%26yaw%3D81.885777192817!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDQwOC4wIKXMDSoASAFQAw%3D%3D)

---

## Parte 2 (`DUOC{coordenadas_681742030869784848529051269297481582042587446976}`)

A diferencia de la parte 1, donde el objetivo era encontrar ubicaciones y descubrir información enmascarada en carteles, en la parte 2 basta con obtener las coordenadas geográficas de cada punto. Sin embargo, este segundo lote de imágenes no incluye monumentos mundialmente famosos. Se entrega un ejemplo de cómo construir la flag a partir de las coordenadas:

![example flag](imgs/small_example_pass.jpg)
Esta imagen muestra cómo ensamblar los dígitos: se toman los dos primeros dígitos después del punto decimal tanto de la latitud como de la longitud para producir 4 dígitos por cada ubicación.

La plantilla de la segunda flag muestra 12 imágenes en miniatura, lo que resulta en una cadena de 48 dígitos decimales (`DUOC{coordenadas_681742030869784848529051269297481582042587446976}`):
![flag 2 template](imgs/small_flag_2.jpg)

Cada una de estas ubicaciones puede determinarse sin ambigüedad utilizando indicadores específicos de cada país y metadatos visuales de Google Street View (como el vehículo de captura, matrículas, bolardos y señalética vial), apoyándose en recursos públicos de geolocalización como [Plonk It](https://www.plonkit.net/guide) o [GeoHints](https://geohints.com/).

## `img_1001.jpg` -- Portugal -- `@38.6895653,-9.1769822` -- **6817**

Indicadores del país:
- Matrícula europea blanca alargada con franja azul a la izquierda y amarilla a la derecha

La imagen muestra varias matrículas europeas con una franja vertical amarilla en el extremo derecho, característica exclusiva de Portugal. La brújula indica que nos encontramos sobre un puente colgante orientado de norte a sur: el Ponte 25 de Abril, al sur de Lisboa (también es visible el brazo izquierdo del monumento Cristo Rei en el extremo izquierdo). La posición exacta sobre el puente se determina alineando los tirantes y la motocicleta en el centro de la calzada.

![image 1](imgs/small_img_1001.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@38.6895653,-9.1769822,3a,75y,201.6h,87.9t/data=!3m7!1e1!3m5!1sxOe0UnuvKOVRm8CkmT8MWg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D2.102479664353396%26panoid%3DxOe0UnuvKOVRm8CkmT8MWg%26yaw%3D201.5965069220882!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1002.jpg` -- Kirguistán -- `@41.4273437,75.0332914` -- **4203**

Indicadores del país:
- Paisaje árido montañoso
- Vehículo de Google plateado con portaequipajes y espejos retrovisores visibles

La camioneta plateada con portaequipajes en un entorno árido identifica a Kirguistán. Buscando un puente pequeño orientado exactamente de norte a sur sobre el río Naryn en el centro del país, se confirma la ubicación por las barandas pintadas de azul y rojo.

![image 2](imgs/small_img_1002.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@41.4273437,75.0332914,3a,75y,7.09h,60.6t/data=!3m7!1e1!3m5!1s-7n4BkV4-iPWDSvv2-zQAw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D29.39953907190302%26panoid%3D-7n4BkV4-iPWDSvv2-zQAw%26yaw%3D7.086671441781004!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1003.jpg` -- Isla de Man -- `@54.0842611,-4.6959922` -- **0869**

Indicadores del país:
- Conducción por la izquierda
- Matrícula trasera amarilla con franja roja a la izquierda

La conducción por la izquierda con matrícula trasera amarilla y franja vertical roja a la izquierda identifica exclusivamente a la Isla de Man. Por la posición del mar en la brújula, el vehículo circula por la costa sur sobre la carretera A5.

![image 3](imgs/small_img_1003.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@54.0842611,-4.6959922,3a,75y,141.47h,77.47t/data=!3m7!1e1!3m5!1sZPzjy9pG3yxAkOsg9eE0uw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D12.52569889737542%26panoid%3DZPzjy9pG3yxAkOsg9eE0uw%26yaw%3D141.47210417915278!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1004.jpg` -- Islandia -- `@64.7883182,-14.4895161` -- **7848**

Indicadores del país:
- Bolardos viales amarillos con corte superior diagonal y reflector blanco

Los bolardos amarillos con corte inclinado son exclusivos de Islandia. La brújula indica un tramo curvo de la carretera Hringvegur que cruza el fiordo Berufjörður.

![image 4](imgs/small_img_1004.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@64.7883182,-14.4895161,3a,75y,39.61h,83.04t/data=!3m7!1e1!3m5!1sHF5TmiK8gmGtwUbuyAZbCg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D6.963626582018591%26panoid%3DHF5TmiK8gmGtwUbuyAZbCg%26yaw%3D39.61112281195068!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1005.jpg` -- Guatemala -- `@14.487069,-90.5260302` -- **4852**

Indicadores del país:
- Vehículo de Google con portaequipajes y espejos visibles
- Poste eléctrico verde con placa de ubicación ("M0" / "032")

El vehículo gris de Street View junto con el poste verde y la placa de identificación vial "M0 032" identifican el tramo exacto en Guatemala.

![image 5](imgs/small_img_1005.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@14.487069,-90.5260302,3a,75y,177.04h,61.95t/data=!3m7!1e1!3m5!1sxGq_MZ8__Wva53yCIRpfqg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D28.049310769779574%26panoid%3DxGq_MZ8__Wva53yCIRpfqg%26yaw%3D177.04157945948396!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1006.jpg` -- Malta -- `@35.9017928,14.516686` -- **9051**

Indicadores del país:
- Conducción por la izquierda con matrículas europeas blancas
- Edificios de piedra caliza y señal de parada de autobús de Malta

La arquitectura de piedra caliza con la cúpula de la Basílica de Nuestra Señora del Monte Carmelo al fondo ubica la escena en St. Elmo Place, La Valeta, Malta.

![image 6](imgs/small_img_1006.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@35.9017928,14.516686,3a,73.2y,259.08h,82.89t/data=!3m7!1e1!3m5!1szHGS_pqQ5-Yxsxxqo48z6Q!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D7.106785215160116%26panoid%3DzHGS_pqQ5-Yxsxxqo48z6Q%26yaw%3D259.08164220572974!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwOC4wIKXMDSoASAFQAw%3D%3D)

## `img_1007.jpg` -- Omán -- `@23.2648087,58.9252482` -- **2692**

Indicadores del país:
- Camioneta blanca de Google con barras negras atornilladas
- Matrícula trasera amarilla dorada y paisaje costero árido

Estos indicadores corresponden a la costa este de Omán, frente a la marina artificial de Qurayyat.

![image 7](imgs/small_img_1007.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@23.2648087,58.9252482,3a,90y,57.41h,74.85t/data=!3m7!1e1!3m5!1s1R5VRWHCrAcuYx61g_UF-w!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D15.150504005897744%26panoid%3D1R5VRWHCrAcuYx61g_UF-w%26yaw%3D57.40665071207248!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1008.jpg` -- San Marino -- `@43.9706272,12.4825187` -- **9748**

Indicadores del país:
- Idioma italiano y paso peatonal pintado en azul y blanco con señales colgantes

El estilo de paso peatonal azul y blanco junto con el comercio "MVPsport" sobre la Superstrada identifica la ubicación en San Marino.

![image 8](imgs/small_img_1008.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@43.9706272,12.4825187,3a,31.5y,348.06h,90.51t/data=!3m7!1e1!3m5!1slXrShcxLr4G4LUItMs-VeQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-0.5115744900562902%26panoid%3DlXrShcxLr4G4LUItMs-VeQ%26yaw%3D348.0551894805283!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1009.jpg` -- Senegal -- `@14.1527636,-16.8297142` -- **1582**

Indicadores del país:
- Matrículas azules alargadas y parte trasera de camioneta blanca de Google visible

El puente peatonal de madera que conecta tierra firme con la isla de conchas al sur de Joal-Fadiout identifica la ubicación en Senegal.

![image 9](imgs/small_img_1009.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@14.1527636,-16.8297142,3a,75y,149.18h,61.72t/data=!3m7!1e1!3m5!1sidj0dsaSYEv1D7sEIPkCbg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D28.283720467437085%26panoid%3Didj0dsaSYEv1D7sEIPkCbg%26yaw%3D149.17642871365416!7i16384!8i8192!4m6!3m5!1s0xe95028d30b8b5d3:0x837b0d2f2bc66f2!8m2!3d16.5110902!4d-15.8114879!16zL20vMDdieHBz?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1010.jpg` -- Colombia -- `@10.0453874,-75.2587667` -- **0425**

Indicadores del país:
- Cruz metálica en el reverso de la señal vial ("Colo cross") y mojón kilométrico verde vertical (Ruta 90, km 49)

Estos elementos identifican el kilómetro 49 de la Ruta Nacional 90 en Colombia.

![image 10](imgs/small_img_1010.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@10.0453874,-75.2587667,3a,63.7y,37.52h,82.57t/data=!3m7!1e1!3m5!1sMCjI0Ygw7I_wxnjdNI3WQQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D7.42825048863628%26panoid%3DMCjI0Ygw7I_wxnjdNI3WQQ%26yaw%3D37.524956273775786!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

## `img_1011.jpg` -- Reunión -- `@-20.8759326,55.4441705` -- **8744**

Indicadores del país:
- Matrículas europeas francesas en el hemisferio sur y barra de techo con cinta negra en la esquina trasera derecha

Estos indicadores identifican el puente sobre el Rivière Saint-Denis en la costa norte de la Isla de la Reunión.

![image 11](imgs/small_img_1011.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@-20.8759326,55.4441705,3a,90y,4.11h,57.64t/data=!3m7!1e1!3m5!1sXl-RfsWYysso5PZoirFmtw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D32.36296772423777%26panoid%3DXl-RfsWYysso5PZoirFmtw%26yaw%3D4.11245970240398!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDQwOC4wIKXMDSoASAFQAw%3D%3D)

## `img_1012.jpg` -- Santa Cruz (Islas Vírgenes de EE. UU.) -- `@17.6950798,-64.7635519` -- **6976**

Indicadores del país:
- Camioneta roja de Google con portaequipajes y matrícula corta azul brillante

La camioneta roja de Street View es característica de la isla de Santa Cruz (St. Croix) en las Islas Vírgenes de los Estados Unidos, ubicada en una rampa para botes en la costa sur.

![image 12](imgs/small_img_1012.jpg)
[Enlace a Google Maps](https://www.google.com/maps/@17.6950798,-64.7635519,3a,75y,190.12h,72.98t/data=!3m7!1e1!3m5!1sWHvMaVaizYt3z_ve7Fhh_w!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D17.017473946452427%26panoid%3DWHvMaVaizYt3z_ve7Fhh_w%26yaw%3D190.1235820308217!7i13312!8i6656!4m4!3m3!8m2!3d37.336663!4d-121.891094?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D)

---

Al concatenar los 48 dígitos obtenidos de las 12 ubicaciones en el formato estandarizado se obtiene la flag:
`DUOC{coordenadas_681742030869784848529051269297481582042587446976}`
![flag 2](imgs/true_flag_2.jpg)
