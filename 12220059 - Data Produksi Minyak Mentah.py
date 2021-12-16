''' Refydo Muhammad Farhan 12220059
Project Aplikasi Produksi Minyak Mentah
UAS Pemrograman Komputer Semester Ganjil 2021/2022'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import streamlit as st
import json

############### open resource ###############
#Change to Data Frame
file = pd.read_csv("produksi_minyak_mentah.csv")
df_f = pd.DataFrame(file, columns= ['kode_negara','tahun','produksi','nama','region','sub_region'])
file2= open('kode_negara_lengkap.json')
data=json.load(file2)
df_duplicateC = df_f.drop_duplicates(subset=['nama'])
df_duplicateY = df_f.drop_duplicates(subset=['tahun'])
############### open resource ###############

############### title ###############
st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called
st.title("Data Produksi Minyak Mentah")
############### title ###############)

############### sidebar ###############
st.sidebar.title("Pengaturan")
left_col, right_col = st.columns(2)

#Convert years and name into list
years=df_duplicateY['tahun'].values.tolist()
country=df_duplicateC['nama'].values.tolist()

############### sidebar ###############

############### upper left column ###############
list_years=st.sidebar.selectbox("Pilih Tahun", years)
list_country=st.sidebar.selectbox("Pilih Negara", country)
negara_tampil = st.sidebar.number_input("Jumlah Negara yang Ditampilkan", min_value=1, max_value=None, value=10)
left_col.subheader(f"Grafik Jumlah Produksi Minyak {list_country} Setiap Tahun")
#Change to Data Frame
df = pd.DataFrame(file, columns= ['kode_negara','tahun','produksi','nama','region','sub_region'])
filter_negara=(df.loc[df['nama']==list_country])
#Showing the plot
fig, ax = plt.subplots()
cmap = cm.get_cmap('tab10')
colors = cmap.colors
ax.set_title(f"Grafik Produksi Minyak Negara {list_country} Setiap Tahun",fontsize=8)
ax.set_xlabel("Tahun")
ax.set_ylabel("Produksi")
ax.plot(filter_negara['tahun'], filter_negara['produksi'])
plt.locator_params(axis='x', nbins=45)
plt.xticks(rotation=90,fontsize = 6)
plt.xlim(1971,2015)
plt.tight_layout()
left_col.pyplot(fig)
############### upper left column ###############

############### upper right column ###############
right_col.subheader(f"Grafik {negara_tampil} Besar Negara Penghasil Minyak Tahun {list_years}")
#Soal B
#Change to Data Frame
df2 = pd.DataFrame(file, columns= ['kode_negara','tahun','produksi','nama','region','sub_region'])
filter_tahun=(df2.loc[df2['tahun']==list_years])
filter_tahun.drop(['produksi'],axis=1)
filter_tahun.sort_values(by=['produksi'], inplace=True, ascending=False)
filter_tahun_new = filter_tahun.head(negara_tampil)
#Showing the plot
fig, ax = plt.subplots()
cmap = cm.get_cmap('tab10')
colors = cmap.colors
ax.set_title(f"Grafik {negara_tampil} Besar Negara Penghasil Minyak Tahun {list_years}",fontsize=8)
ax.set_xlabel("Negara")
ax.set_ylabel("Produksi")
ax.bar(filter_tahun_new['kode_negara'], filter_tahun_new['produksi'],color=colors)
plt.locator_params(axis='x')
plt.xticks(rotation=90,fontsize = 6)
plt.tight_layout()
right_col.pyplot(fig)
############### upper right column ###############

############### middle left column ###############
left_col.subheader(f"Grafik {negara_tampil} Besar Negara Penghasil Minyak Kumulatif")
#Soal C
#Change to Data Frame
df3 = pd.DataFrame(file, columns= ['kode_negara','produksi'])
df3['total_produksi']=df3.groupby(['kode_negara'])['produksi'].transform('sum')
df4=df3.drop_duplicates(subset=['kode_negara'])
df4.sort_values(by=['total_produksi'], inplace=True, ascending=False)
df4_new=df4.head(negara_tampil)
#Showing the plot
fig, ax = plt.subplots()
cmap = cm.get_cmap('tab10')
colors = cmap.colors
ax.set_title(f"Grafik {negara_tampil} Besar Negara Penghasil Minyak Kumulatif",fontsize=8)
ax.set_xlabel("Negara")
ax.set_ylabel("Produksi")
ax.bar(df4_new['kode_negara'], df4_new['total_produksi'],color=colors)
plt.xticks(rotation=90,fontsize = 6)
plt.tight_layout()
left_col.pyplot(fig)
############### middle left column ###############

############### middle right column ###############
right_col.subheader("Summary")
#Soal D
#Open File
file = pd.read_csv("produksi_minyak_mentah.csv")
#Change to Data Frame
df5 = pd.DataFrame(file, columns= ['kode_negara','tahun','produksi','nama','region','sub_region'])
df5['total_produksi_tahun']=df5.groupby(['tahun'])['produksi'].transform('max')
df6=df5.loc[df5['tahun']==list_years]
df6.sort_values(by=['produksi'],inplace=True,ascending=False)
df9=df6.mask(df6['produksi']==0).ffill()
terbesar_produksi=df6.iloc[0]['produksi']
terbesar_negara=df6.iloc[0]['kode_negara']
terbesar_n=df6.iloc[0]['nama']
terbesar_nr=df6.iloc[0]['region']
terbesar_nsr=df6.iloc[0]['sub_region']
terkecil_produksi=df9.iloc[-1]['produksi']
terkecil_negara=df9.iloc[-1]['kode_negara']
terkecil_n=df9.iloc[-1]['nama']
terkecil_nr=df9.iloc[-1]['region']
terkecil_nsr=df9.iloc[-1]['sub_region']
df['total_produksi_all'] = df.groupby(['kode_negara'])['produksi'].transform('sum')
df7 = df.drop_duplicates(subset=['kode_negara'])
df7.sort_values(by=['total_produksi_all'],inplace=True,ascending=False)
terbesar_all_negara=df7.iloc[0]['kode_negara']
terbesar_all_n=df7.iloc[0]['nama']
terbesar_all_negara_r=df7.iloc[0]['region']
terbesar_all_negara_sr=df7.iloc[0]['sub_region']
terbesar_all_produksi=df7.iloc[0]['total_produksi_all']
df8=df7.mask(df7['produksi']==0).ffill()
terkecil_all_n=df8.iloc[-1]['nama']
terkecil_all_negara_r=df8.iloc[-1]['region']
terkecil_all_negara_sr=df8.iloc[-1]['sub_region']
terkecil_all_negara=df8.iloc[-1]['kode_negara']
terkecil_all_produksi=df8.iloc[-1]['total_produksi_all']
right_col.markdown(f"**Negara dengan Produksi Minyak Terbanyak Tahun {list_years}: ** \n Nama Negara: {terbesar_n} \n Code Negara : {terbesar_negara} \n Region: {terbesar_nr} \n Sub-Region: {terbesar_nsr} dengan jumlah produksi {terbesar_produksi}")
right_col.markdown(f"**Negara dengan Produksi Minyak Kumulatif Terbesar: ** \n  Nama Negara: {terbesar_all_n} \n Code Negara : {terbesar_all_negara} \n Region: {terbesar_all_negara_r} \n Sub-Region: {terbesar_all_negara_sr} dengan jumlah produksi {terbesar_all_produksi}")
right_col.markdown(f"**Negara dengan Produksi Minyak Terkecil Tahun {list_years}: ** \n  Nama Negara: {terkecil_n} Code Negara : {terkecil_negara} \n Region: {terkecil_nr} \n Sub-Region: {terkecil_nsr} dengan jumlah produksi {terkecil_produksi}")
right_col.markdown(f"**Negara dengan Produksi Minyak Kumulatif Terkecil: ** \n Nama Negara: {terkecil_all_n} \n Code Negara : {terkecil_all_negara} \n Region: {terkecil_all_negara_r} \n Sub-Region: {terkecil_all_negara_sr} dengan jumlah produksi {terkecil_all_produksi}")
############### middle right column ###############

############### lower left column ###############
#Soal D Produksi Negara = 0
#Open File
#Change to Data Frame
df11 = pd.DataFrame(file, columns= ['kode_negara','tahun','produksi','nama','region','sub_region'])
df11['total_produksi'] = df11.groupby(['kode_negara'])['produksi'].transform('sum')
df12 = df.drop_duplicates(subset=['kode_negara'])
df12=df12.drop('tahun',axis=1)
nilai=0
filter_nol=df11.loc[(df11['produksi']==nilai) & (df11['tahun']==list_years)]
filter_nol_new=filter_nol.drop('total_produksi',axis=1)
filter_all_0=df12.loc[(df12['total_produksi_all']==nilai)]
filter_all_0_new=filter_all_0.drop('produksi',axis=1)
############### lower left column ###############

############### lower right column ###############
left_col.markdown(f"**Negara dengan Produksi 0 Tahun {list_years}**")
left_col.dataframe(filter_nol_new.reset_index())
right_col.markdown(f"**Negara dengan Produksi 0 Kumulatif**")
right_col.dataframe(filter_all_0_new.reset_index())
############### lower right column ###############