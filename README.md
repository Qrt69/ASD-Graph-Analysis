# ASD-Graph-Analysis

## Project omschrijving
Aalyse van Autisme Spectrum Stoornis (ASS) of, in het Engels *Autism Spectrum Disorder* (ASD), gebruik makend van datasets ter beschikking gesteld door de organisatie ABIDE.
ABIDE staat voor Autism Brain Imaging Data Exchange. Hieronder volgt een vertaling van de introductie op de [ABIDE website](https://fcon_1000.projects.nitrc.org/indi/abide/).

>Autisme Spectrum Stoornis wordt gekenmerkt door kwalitatieve beperkingen in sociale wederkerigheid en door repetitief, beperkt en stereotiep bedrag/interesses. Voorheen werd ASS als >zeldzaam bechouwd, maar nu wordt erkend bij meer dan 1% van de kinderen voorkomt. Ondanks de voortdurende vooruitgang in het onderzoek hebben het tempo en de klinische impact ervan >geen gelijke tred gehouden met de dringende noodzaak om manieren te vinden waarmee de diagnose op jongere leeftijd kan worden gesteld, optimale behandelingen kunnen worden >geseleceerd en uitkomsten kunnen worden voorspeld. Voor het grootste deel is dit te wijten aan de complexiteit en heterogeniteit van ASS. Om deze uitdagingen aan te gaan, zijn >grootschalige monsters essentieel, maar afzonderlijke laboratoria kunnen geen voldoende grote datasets verkrijgen om de hersenmechanismen die ten grondslag liggen aan ASS te >onthullen. In reactie hierop heeft het Autism Brain Imaging Data Exchange (ABIDE) initiatief functionele en structurele beeldvormingsgegevens van de hersenen verzameld van >laboratoria over de hele wereld om ons begrip van de neurale basis van autisme te versnellen. Met het uiteindelijke doel om ontdekkingswetenschap en vergelijkingen tussen >verschillende monsters te vergemakkelijken, omvat het ABIDE-initiatief nu twee grootschalige collecties: ABIDE I en ABIDE II. Elke collectie is tot stand gekomen doo rhet samen >voegen van dtasets die onafhanelij van elkaar zijn verzameld in meer dan 24 internationale laboratoria voor hersenbeeldvorming en worden beschikbaar gesteld aan onderzoekers over de >hele wereld, in overeenstemming met de principes van open science, zoals die centraal staan in het International Neuroimaging Data-sharing Initiative.

## Projectstructuur
- **docs/**: begeleidende documenten uit websites, boeken, ...
- **notebooks/**: Jupyter Notebooks voor data cleaning, analyse en machine learning
- **src/**: Python scripts voor ondersteunende doeleinden

## Data
De ABIDE dataset kan vrij gedownload worden. In de docs directory staat een README markdown file met toelichting hoe de dataset kan gedownload worden, en welke parameters kunnen meegegeven worden. Voor verdere details verwijs ik graag naar deze tekst, maar alvast al een beknopte toelichting bij de gekozen parameters:
> - ***pipeline*** = 'cpac' (*Configurable Pipeline for the Analysis of Connectomes*). C-PAC is een populaire methode om MRI-scans te verwerken tot data, wereldwijd gebruikt en >>bijgevolg beter vergelijkbaar in wetenschappelijke literatuur. Bovendien zijn meerdere handleidingen, voorbeelden en andere resources beschikbaar om te werken met C-PAC verwerkte >>data.
>- ***Derivative*** = 'rois_cc200'. ROI staat voor Region of Interest, een regio (synaps of zone) in de hersenen. Zo zijn er 200 gedefinieerd die weergegeven worden in de bestanden >>uit de ADIBE dataset.
