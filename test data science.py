import pandas as pd 
df = pd.read_excel("JUNGLE BIKE BBB.xlsx")


df.rename(columns={"Unnamed: 1":"contenance", "Unnamed: 2":"gamme"}, inplace=True)#on renomme les colonnes pour plus de lisibilité


del df["Unnamed: 7"] #on supprime la colonne inutile


"""On essaye d'extraire les types de produits"""
df_produit = df[(df["Unnamed: 4"].isna()==True) & (df["Unnamed: 5"].isna()==True) & (df["Unnamed: 6"].isna()==True)]
df["produits"] = df_produit["contenance"][df_produit["contenance"].isna()==False]



"""On essaye d'extraire les modèles et les contenances"""
df_modele_contenance = df[(df["Unnamed: 4"].isna()==False) & (df["Unnamed: 5"].isna()==False) & (df["Unnamed: 6"].isna()==False)]
df["Modèle"] = df_modele_contenance["TARIF PROFESSIONNEL BBB: COLLECTION 2021"]
df["Contenance"] = df_modele_contenance["contenance"]



li =  list(df["gamme"].unique())#on regarde toutes les informations de la colonne "gamme"
couleurs = ['Noir', 'Noir Mat', 'Carbone Brillant ', 'noir', 'noir brillant','black','transparent','carbon', 'Transparent','argent','Blanc / Bleu','Blanc / Gris','bleu', 'or', 'vert','dark blue', 'light blue','gris/gris','gris', 'gris/nickel', 'nickel/nickel', 'nickel ','grey','grey/nickel', 'nickel', 'Noir Argent', 'Noir Gris','Noir / Gris', 'Noir/Gris','noir mat','carbone','matt black','Noir/Noir', 'Gris', 'rouge', 'noir/argent', 'NOIR MAT','Jaune Fluo','blanc','noir/bleu/rouge/vert ']
dimensions = ['Ø 10 - 80', 'S 143mm', 'M 208mm', 'L 302mm', '10 x 1800mm', '5 x 1200mm', '10mmx10mmx1000m ', '250mm x 170mm', '8mm x150cm', '12mm x 150cm ', '12mm x 100cm ', '6mm x 150cm ', '10mm x 150cm ', '10mm x 100cm ', '12mmx180cm', '15mmx180cm', '12mmx100cm', '18mmx100cm', '5mm x 1000mm', ' 4.8x1500mm', '3 X 1200mm', '8 X 1500mm', '8mm x 2000mm', '8mm x 1200mm', '4,5mm x 1000mm ', '46mmØx68mm', '46mmØx68/73mm', '42Ø x 68/73mm', '41mmØ x86,5mm ', '41mmx89,5 - 92mm', '41mmØx86/92mm', 'BB86/92 41mmx86/92', '1.37x24T x 68/73mm', '37x25x6', 'C46 x 68/73mm', '46Ø x 68/73mm', 'C42 x 68/73mm', '42 x ID 30 x 7mm', 'C40 x ID 29 x 6.8mm', '37 x ID 24 x 7mm', '36 x ID 30 x 0.5mm ', '36 x ID 30 x 1.0mm', '36 x ID 30 x 2.5mm', '30 x ID 24 x 0,5mm', '30 x ID 24 x 1,0mm', '30 x ID 24 x 2,5mm','260x50 ', ' 500mmX50mm', '500mmx70mm','25x4', '140mm', '160mm', '180mm', '203mm', '0,3mm','(1,1x2000mm)','1.1 x 2350mm', '4x2500mm', '1.5x2350mm', '(1,5x2350mm)', '(1.5x2000mm)', '(1,5x2000mm)', '1.5 x 2350mm', '5x2500mm', '1.1x2000mm ', '1.1x2350mm ', '1.1x2350mm', '1.1x2000mm', '1.5x1100mm  ', '1.5mmx1700mm  ', '1.5mmx2350mm  ', '1.5mmx900mm  ', '1.5mmx2000mm ', '1.5mmx2000mm', '5mmX 50 mtr.', '(5mmx50 mtr)', '(4mmx50 mtr)', '(4mmX50 mtr)', '(5mmX50 mtr)','50 mtr.','2,1mm','20" & 22"', '24" - 26" - 28"', '35/800mm','38-40-42-44', '22.2-31.8mm', '31.8mm', '130mm', '92mm 130mm', '45°x45°', ' 45°x45°', ' 36°x45°', '80 X 55 X 200', '20 x 9.5 x 8.5cm', '20 x 16 x 11cm', '8Ø x 15cm', '15 x 15 x 4cm  0.75L', 'S 130 x 40 x 80mm', 'M 130 x 50 x 80mm', 'L 130 x 85 x 80mm','20 x 11x5.5cm', '30 x 14 x 14cm - 4L', '124X64X10mm', '155x75x10mm', '158X80X10mm', '160X110', '202X269','29x2.40/2.80','18mm x\xa0 4m', '22mm x\xa0 4m ', '25mm x\xa0 4m','28/31/34 x 4.5M','18mm x\xa0 10m', '22mm x\xa0 10m', '25mm x\xa0 10m', '28mm x 10M', '31mm x 10M', '34mm x 10M', '48 mm', '80mm', '450ml', '630ml', 'T25/4mm/5mm','5mm', '8mm']
tailles = ['S 143mm', 'M 208mm', 'L 302mm','M', 'L', 'S', 'XL', 'XXL', 'Enfant', 'Uni taille','39T/42T', '46/50/52/53', '44T/130', '46T/130', '50/52/53', '39T/130', '30T/130', '39/42', '46/48/50/52/53', '34/36', '34/36/38', '36T/110', '34/36/38/39/42', '46/50/52', '38/40', '30/32/34/36', '38/40/42', '24T/64', '26/28', '30/32/34', '34/26/28', '12T-14T','10L', '15 x 15 x 4cm  0.75L', 'S 130 x 40 x 80mm', 'M 130 x 50 x 80mm', 'L 130 x 85 x 80mm', '27.2/30,9/31,6', '47-62-203', '47-57-305', '47/57-355', '23-451', '47-57-406', '32-37-438-451', '47-57-507', '32-40-540-541', '18/23-571 ', '40-47-559-584', '45-61-559', '32-40-584-590', '52/58-584', '20-28-622-630', '30/43-622/630','50/56-622','2/2/3/4/5/6/8/10T25', 'T25 / T30', 'T40', '32-35 / 36-40', 'Uni-Taille']



"""On essaye d'extraire les couleurs"""
df_couleurs = df[(df["gamme"].isin(couleurs)==True)]#Si l'élément de l colonne "gamme" est dans la liste de couleurs...
df_couleurs["gamme"].fillna("0")
df["colors"] = df_couleurs["gamme"]#... on ajoute au dataframe initiale la colonne avec les couleurs
#df["colors"] = df["colors"].fillna("Pas de couleurs")




"""On essaye d'extraire les dimensions """
df_dimensions = df[(df["gamme"].isin(dimensions)==True)]#Si l'élément de l colonne "gamme" est dans la liste de dimensions...
df["dimensions"] = df_dimensions["gamme"]#... on ajoute au dataframe initiale la colonne avec les dimensions
#df["dimensions"] = df["dimensions"].fillna("Pas de dimensions")




"""On essaye d'extraire les tailles"""
df_tailles = df[(df["gamme"].isin(tailles)==True)]#Si l'élément de l colonne "gamme" est dans la liste de tailles...
df["tailles"] = df_tailles["gamme"]#... on ajoute au dataframe initiale la colonne avec les tailles
#df["tailles"] = df["tailles"].fillna("Pas de tailles")


"""Faisons un nouveau fichier dans lequel les données seront nettoyées """
df_clean = df.copy()
del df_clean["TARIF PROFESSIONNEL BBB: COLLECTION 2021"]
del df_clean["contenance"]
del df_clean["gamme"]
del df_clean["Unnamed: 3"]
del df_clean["Unnamed: 4"]
del df_clean["Unnamed: 5"]
del df_clean["Unnamed: 6"]


df_clean.to_csv("test clean.csv")