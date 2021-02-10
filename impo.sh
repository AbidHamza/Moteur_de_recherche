champs="Ageod Allegorithmic Ankama_Games ARG_Informatique Asobo_Studio Attitude_Studio Bigben_Interactive Bleu-ciel_informatique Bulkypix Canal+_Multimedia Cobra_soft Coktel_Vision Creative_Patterns  Cyanide_(entreprise) DK-Games_Duran_Duboi Ère_informatique Étranges_Libellules Eversim Galiléa Infomedia Innelec_Multimedia Int13 Jeutel Koalabs Lankhor Lexis_Numérique Loriciel LSP_Games Magic_Pockets (entreprise) "
for champ in $champs
do
    echo importation de $champ
    curl "https://fr.wikipedia.org/w/index.php?title=${champ}&action=raw" > PAGES/$champ
done
