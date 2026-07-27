# %%


import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

dfs = pd.read_html(url, storage_options=headers)


# %%


ufs = dfs[1]


# %%

ufs.info()


# %%
# n = "164 122,2	"

def str_to_float(x):

    return float(x.replace(' ','').replace(',', '.').replace("\t",'').replace("\xa0",''))


# %%


ufs["Área (km²)"].apply(str_to_float)


# %%

ufs.info()
# %%


ufs["PIB per capita (R$) (2015)"] = ufs["PIB per capita (R$) (2015)"].apply(str_to_float)
ufs["População (Censo 2022)"] = ufs["População (Censo 2022)"].apply(str_to_float)
ufs["Área (km²)"] = ufs["Área (km²)"].apply(str_to_float)
ufs["PIB (2015)"] = ufs["PIB (2015)"].apply(str_to_float)
# %%

ufs
# %%

def str_to_int(n):
    return int(float(n.split(' ')[0].replace(',' , '.')))



# %%

ufs["Expectativa de vida (2016)"].apply(str_to_int)


# %%

def uf_to_regiao(uf):

    # tartar uf
    # uf = uf

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"



# %%


ufs["Unidade federativa"].apply(uf_to_regiao)


# %%
ufs["Regiao"] = ufs["Unidade federativa"].apply(uf_to_regiao)
# %%

ufs
# %%

def mortalidade_to_float(x):
    return float(x.replace(',', '.').replace('‰', ''))



# %%

ufs["Mortalidade infantil (/1000)"] = ufs["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
ufs

# %%

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and 
            linha["IDH (2010)"] > 700)


# %%

ufs.apply(classifica_bom, axis=1)
# %%
