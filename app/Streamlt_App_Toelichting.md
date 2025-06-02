# 🧠 Interactieve CC200 ROI Streamlit App
## Toelichting
Deze Streamlit app laat gebruikers toe de 200 *"Regions of interest"* te visualiseren volgens de x, y en z as. 
De term CC200 verwijst naar de CC200 atlas, een brein atlas ontworpen door Cameron Craddock, zelf een machine learning
engineer, gefascineerd door het menselijk brein. Voor meer info verwijs ik graag naar zijn LinkedIn pagina:
[Cameron Craddock](https://www.linkedin.com/in/cameron-craddock/).

## Gebruik
Voer het nummer van de ROI in, waarna de App volgende informatie zal geven. Nummers kunnen ingegeven worden, doorlopen
van de nummers kan door op + en - te klikken.
>-  ***Harvard-Oxford Label***: de formele anatomische benaming van de hersenzone, indien een formele benaming bestaat.
>-  ***Center of Mass***: de x, y en z coördinaten van de ROI. Een tekening werd toegevoegd om coördinaat (0, 0, 0) aan
> te geven. De x-as vertrekt aan het achterhoofd (negatief) naar het voorhoofd (positief). De y-coördinaat vertrekt rechts
> (negatief) naar links (positief). De z-as tenslotte vertrekt onderaan(negatief) naar boven (positief). 
> Het coördinatensysteem wordt het MNI systeem genoemd, verwijzend naar het Montreal Neurological Institute. Dit systeem
> werd ingevoerd om een universele methodologie te kunnen hanteren bij het interpreteren van MRI-scans. De coördinaten worden
> expliciet in millimeters gemeten, dus een x-coördinaat van -30 betekent dat het centrum van de ROI zich 3cm achter het
> nulpunt bevindt.
>-  ***Volume(voxels)***: geeft de grootte weer van een ROI. 1 voxel is een kleine kubus van 3mm x 3mm x 3mm.

Onder deze informatie wordt een visualisatie getoond van de 3 dwarsdoorsneden van de hersenen met aanduiding van de ROI
in het rood.
Voor de duidelijkheid is er ook een tekening toegevoegd die nogmaals aanduidt hoe de x, y en z-coördinaten te interpreteren.

## Technisch

### Gebruikte libraries
>- ***streamlit***: library gebruikt voor het genereren van de web-app. Streamlit laat toe online visualisaties te genereren op
> een vrij eenvoudige manier.
>- ***pathlib***: library die toelaat op een dynamische manier paths en verwijzingen naar bestanden aan te geven, ook
> indien deze applicatie gerund wordt vanuit Github
>- ***nilearn***: nilearn maakt toegankelijke en veelzijdige analyses van hersenvolumes mogelijk. Het biedt statistische
> en machine learning tools, met instructieve documentatie en een open community. [nilearn](https://nilearn.github.io/stable/index.html).
>- ***numpy en pandas***: worden gebruikt voor o.a. het inlezen van het csv-bestand met de ROI informatie. Ook nilearn
> maakt indirect gebruik van numpy en pandas
>- ***matplotlib***: wordt gebruikt voor visualisaties, ook aangeroepen door nilearn.








