# ASD-Graph-Analysis

## Project omschrijving
Analyse van Autisme Spectrum Stoornis (ASS) of, in het Engels *Autism Spectrum Disorder* (ASD), gebruik makend van datasets ter beschikking gesteld door de organisatie ABIDE.
ABIDE staat voor Autism Brain Imaging Data Exchange. Hieronder volgt een vertaling van de introductie op de [ABIDE website](https://fcon_1000.projects.nitrc.org/indi/abide/).

>Autisme Spectrum Stoornis wordt gekenmerkt door kwalitatieve beperkingen in sociale omgang en door repetitief, beperkt en stereotiep bedrag/interesses. Voorheen werd ASS als zeldzaam beschouwd, maar wordt nu erkend bij meer dan 1% van de kinderen. Ondanks de voortdurende vooruitgang in het onderzoek, hebben het tempo en de klinische impact ervan, geen gelijke tred gehouden met de dringende noodzaak om manieren te vinden waarmee de diagnose op jongere leeftijd kan worden gesteld, optimale behandelingen kunnen worden geseleceerd en uitkomsten kunnen worden voorspeld. Voor het grootste deel is dit te wijten aan de complexiteit en heterogeniteit van ASS. Om deze uitdagingen aan te gaan, zijn grootschalige monsters essentieel, maar afzonderlijke laboratoria kunnen geen voldoende grote datasets verkrijgen om de hersenmechanismen die ten grondslag liggen aan ASS te onthullen. In reactie hierop heeft het Autism Brain Imaging Data Exchange (ABIDE) initiatief functionele en structurele beeldvormingsgegevens van de hersenen verzameld van laboratoria over de hele wereld om ons begrip van de neurale basis van autisme te versnellen. Met het uiteindelijke doel om ontdekkingswetenschap en vergelijkingen tussen verschillende monsters te vergemakkelijken, omvat het ABIDE-initiatief nu twee grootschalige collecties: ABIDE I en ABIDE II. Elke collectie is tot stand gekomen door het samenvoegen van datasets die onafhanelijk van elkaar zijn verzameld in meer dan 24 internationale laboratoria voor hersenbeeldvorming en worden beschikbaar gesteld aan onderzoekers over de hele wereld, in overeenstemming met de principes van open science, zoals die centraal staan in het International Neuroimaging Data-sharing Initiative.

## Projectstructuur
- **docs/**: begeleidende documenten uit websites, boeken, ...
- **notebooks/**: Jupyter Notebooks voor data cleaning, analyse en machine learning
- **src/**: Python scripts voor ondersteunende doeleinden
- **results/**: grafieken, visualisaties,...

## Data
### ABIDE dataset
De ABIDE dataset kan vrij gedownload worden. In de docs directory staat een README markdown file met toelichting hoe de dataset kan gedownload worden, en welke parameters kunnen meegegeven worden. Voor verdere details verwijs ik graag naar deze tekst, maar alvast al een beknopte toelichting bij de gekozen parameters:
> - ***pipeline*** = 'cpac' (*Configurable Pipeline for the Analysis of Connectomes*). C-PAC is een populaire methode om MRI-scans te verwerken tot data, wereldwijd gebruikt en bijgevolg beter vergelijkbaar in wetenschappelijke literatuur. Bovendien zijn meerdere handleidingen, voorbeelden en andere resources beschikbaar om te werken met data die verwerkt zijn volgens de C-PAC principes.
>- ***Derivative*** = 'rois_cc200'. ROI staat voor Region of Interest, een regio (synaps of zone) in de hersenen. Zo zijn er 200 gedefinieerd die weergegeven worden in de bestanden uit de ADIBE dataset. Meer gedetailleerde toelichting volgt in een afzonderlijk document.
>- ***Strategy*** = 'filt_noglobal'. Wereldwijd worden verschillende toestellen gebruikt voor het maken van de MRI-scans. Daardoor kunnen minieme verschillen bestaan in de beeldvorming. Deze "noises" zijn gefilterd door de setting filt_noglobal.
>- ***diagnosis*** = 'both'. Dit betekent dat zowel ASS als niet ASS personen in de database aanwezig zijn. Dit laat toe vergelijkingen te maken.

In de notebooks/Data_Collection sectie van deze repository staat een script *download_abide_preprocessed_dataset.ipynb*. Dit script wordt ter beschikking gesteld door ABIDE en kan gebruikt worden voor het instellen van de hierboven beschreven parameters. De download geeft, met deze parameters, een totaal van 884 bestanden van het type .1D. Dit zijn de numerieke weergaven van 884 MRI-scans. 

De gegevens over deze personen zijn samengebracht in een csv-bestand met de naam *Phenotypic_V1_0b_preprocessed1.csv*. Dit bestand geeft ons een idee over welke personen een MRI-scan ondergingen. Concreet vinden we hier informatie zoals geslacht, leeftijd, plaats van de scan (bijv. New York, Leuven) terug. Uiteraard wordt dit bestand meer in detail bekeken gedurende de concrete data-analyse.

Nog dit: ik voegde ook een csv-bestand toe met de 200 hersenregio's (ROI's) die gebruikt worden bij de weergave van de .1D bestanden. Een Python script werd gemaakt om deze regio's visueel weer te geven. Hierbij heb ik gebruik gemaakt van Streamlit. Om deze Streamlit app toegankelijk te maken, werd het bestand CC200.nii.gz expliciet wél toegevoegd aan de data folder, Streamlit kan immers niet deployen vanuit lokale data. Via deze link kan u een ROI naar keuze selecteren en visualiseren: [ROI in Streamlit](https://qrt69-asd-graph-analysis-notebooksrois-in-streamlit-i1qfvl.streamlit.app).

## Gebruikte Tools

- **Python** als programmeertaal voor de verwerking van alle data
- **Neo4j** als graph database voor opslaan en visualiseren van de .1D bestanden. Bovendien is een vlotte interactie mogelijk tussen Python 
en Neo4j. Binnen deze database zijn de nodes de 200 ROI's in de hersenen, terwijl de edges de connecties zijn die gelegd worden tussen deze
verschillende regio's.


