<div align="center">
<a href="https://github.com/Paloschi/CyMP"><img alt="CyMP" src="https://img.shields.io/badge/CyMP-Crop--yield%20Modeling%20Platform-3F6212?style=for-the-badge&labelColor=1A2E05"></a>
<h1>CyMP</h1>
<p><strong>Plataforma de modelagem espacial de produtividade agrícola — balanço hídrico FAO sobre séries raster.</strong></p>
<p>
<img alt="INPI" src="https://img.shields.io/badge/INPI-BR%2051%202017%20000623--7-3F6212?style=flat-square">
<a href="https://www.unioeste.br"><img alt="UNIOESTE" src="https://img.shields.io/badge/UNIOESTE-LEA-1A2E05?style=flat-square"></a>
<a href="https://tede.unioeste.br/handle/tede/2726"><img alt="Dissertação" src="https://img.shields.io/badge/disserta%C3%A7%C3%A3o-2016-3F6212?style=flat-square"></a>
<img alt="Python" src="https://img.shields.io/badge/python-2.7-3776AB?style=flat-square&logo=python&logoColor=white">
</p>
<p>
<img alt="PyQt4" src="https://img.shields.io/badge/GUI-PyQt4-41CD52?style=flat-square">
<img alt="NumPy" src="https://img.shields.io/badge/NumPy-arrays-013243?style=flat-square&logo=numpy&logoColor=white">
<img alt="rasterio" src="https://img.shields.io/badge/rasterio-GeoTIFF-1B5E20?style=flat-square">
<img alt="FAO" src="https://img.shields.io/badge/modelo-FAO%20water%20balance-3F6212?style=flat-square">
<img alt="MODIS" src="https://img.shields.io/badge/sensor-MODIS-0D47A1?style=flat-square">
</p>
<p>
<a href="#autores-e-registro-inpi">Autores</a> ·
<a href="#pré-requisitos">Pré-requisitos</a> ·
<a href="#início-rápido">Início rápido</a> ·
<a href="#módulos">Módulos</a> ·
<a href="#arquitetura">Arquitetura</a> ·
<a href="#publicação">Publicação</a>
</p>
</div>

---

**Crop-yield Modeling Platform (CyMP)** — software de estimativa espacial de
produtividade agrícola desenvolvido no
[Laboratório de Estatística Aplicada (LEA)](https://www.unioeste.br),
[UNIOESTE](https://www.unioeste.br) — campus Cascavel.

Aplica o **balanço hídrico FAO** sobre séries temporais georreferenciadas
(índices de vegetação MODIS, clima ECMWF interpolado à resolução do sensor).
Foi testado para soja no Paraná na safra 2011/2012: suavização de ruído
(Savitzky–Golay), datas do ciclo da cultura, estresse hídrico (Ks),
evapotranspiração real e produtividades potencial bruta (PPB/Yx) e
atingível (Ya).

Não é software oficial da FAO. A dissertação que documenta a versão 1.0.1
está no repositório da UNIOESTE
([tede/2726](https://tede.unioeste.br/handle/tede/2726)).

| Camada        | Stack                                              |
| ------------- | -------------------------------------------------- |
| Linguagem     | **Python 2.7**                                     |
| Interface     | **PyQt4** (`CyMP.py` → `Visao/TelaPrincipal.py`)   |
| Rasters       | **rasterio** / GDAL · GeoTIFF                      |
| Arrays        | **NumPy**                                          |
| Padrão        | Funções polimórficas (`Modelo/Funcoes/AbstractFunction.py`) |
| Instituição   | **UNIOESTE** · LEA · CAPES                         |
| Registro      | **INPI** `BR 51 2017 000623-7`                     |

---

## Autores e registro INPI

Software institucional da **Universidade Estadual do Oeste do Paraná
(UNIOESTE)**. Programa de computador registrado no
[INPI](https://www.gov.br/inpi/pt-br) (Lei nº 9.609/1998).

| Papel | Nome | Instituição |
| ----- | ---- | ----------- |
| Autor e desenvolvedor | **Me. Rennan Andres Paloschi** | UNIOESTE / LEA |
| Orientação | **Dr. Jerry Adriani Johann** | UNIOESTE |
| Coorientação | **Dr. Adair Santa Catarina** | UNIOESTE |
| Titular | **UNIOESTE** | Universidade Estadual do Oeste do Paraná |

| Campo | Valor |
| ----- | ----- |
| Nome do programa | Crop-yield Modeling Platform — **CyMP** |
| Registro INPI | **BR 51 2017 000623-7** (concedido) |
| Laboratório | Laboratório de Estatística Aplicada (LEA) |
| Campus | Cascavel — PR |
| Fomento | [CAPES](https://www.gov.br/capes) |
| Versão documentada | 1.0.1 (dissertação, 2016) |
| Versão neste repositório | 1.0.10 beta (`workspace.properties`) |
| Contato (desenvolvimento) | rennan_paloschi@yahoo.com |

A autoria é dos três nomes acima, no âmbito do mestrado em Engenharia
Agrícola da UNIOESTE. O registro no INPI comprova a titularidade do
programa de computador; não é patente de invenção.

---

## Pré-requisitos

Ambiente de **2015–2016** (desktop Windows):

- **Python 2.7**
- **PyQt4**
- **NumPy**
- **rasterio** (e GDAL nas variáveis de ambiente)
- Eclipse / PyDev (projeto original: `Gafanhoto_1.0`)

Este código **não** roda em Python 3 sem port. PyQt4 e `ConfigParser` /
`QString` são da era Python 2.

---

## Início rápido

```bash
git clone https://github.com/Paloschi/CyMP.git
cd CyMP
python CyMP.py
```

O launcher lê `workspace.properties` (empresa **Unioeste-LEA**, pasta
padrão `Dados\\`, ícone, modo debug) e abre a janela
*Crop-yield Modeling Platform*.

---

## Módulos

Menu principal (`Visao/TelaPrincipal.py`):

| Menu | Ferramentas |
| ---- | ----------- |
| Balanço hídrico | ETc/ETa, TAW/RAW, esgotamento Dr, Ks |
| Estimativa de produtividade (FAO) | PPB (Yx), Ya |
| Interpoladores | Raster → raster (IDW); ECMWF shape → raster (desligado) |
| Carregar dado | Lista de dados, dado tabelado |
| Tratamento de dados | Datas da cultura, distribuidor de índice, decendial → diário, Savitzky–Golay |
| Estatísticas | Estatísticas descritivas do perfil espectral |

### Cadeia FAO (soja)

```text
IV (MODIS) + clima (ECMWF)
        ↓  Savitzky–Golay / interpolação
  datas do ciclo  →  Kc, TAW/RAW
        ↓
       Dr  →  Ks  →  ETc / ETa
        ↓
     PPB (Yx)  →  Ya
```

---

## Estrutura do projeto

```text
CyMP/
├── CyMP.py                 # entrada: QApplication + TelaPrincipal
├── workspace.properties    # versão, ícone, workspace
├── Controle/               # controllers PyQt (um por diálogo)
├── Visao/                  # UI gerada / TelaPrincipal, diálogos
├── InterfacesQT/           # arquivos .ui
├── Modelo/
│   ├── beans/              # Raster, Vector, Table, SerialFile
│   ├── Funcoes/            # operações (herdam Function)
│   │   ├── BalancoHidrico/BHFAO/   # TAW, Dr, Ks, ETc, PPR, Ya
│   │   ├── Filtros/
│   │   ├── Interpoladores/
│   │   ├── Estatisticos/
│   │   ├── RasterTools/
│   │   └── IndicesVegetativos/
│   └── GeneralTools/
└── images/                 # ícones, logos UNIOESTE / CAPES / LEA
```

### Onde olhar primeiro

| Assunto | Arquivo |
| ------- | ------- |
| Sobre / créditos | `Visao/TelaPrincipal.py` (`retranslateUi`) |
| Contrato das operações | `Modelo/Funcoes/AbstractFunction.py` |
| Raster GeoTIFF | `Modelo/beans/RasterData.py` |
| Balanço FAO | `Modelo/Funcoes/BalancoHidrico/BHFAO/` |
| Produtividade atingível | `Modelo/Funcoes/BalancoHidrico/BHFAO/Ya.py` |
| Controllers | `Controle/Con*.py` |

---

## Arquitetura

```text
CyMP.py
   ↓
TelaPrincipal  (menus PyQt4)
   ↓
Controle/Con*  (diálogo + thread)
   ↓
Modelo/Funcoes/*  (Function: descriptionIN/OUT → exec)
   ↓
beans  (RasterFile, SerialFile, TableData)
   ↓
rasterio / NumPy  →  GeoTIFF de saída
```

- Toda operação herda `Function`: declara metadados de entrada/saída e
  carrega parâmetros no dicionário `paramentrosIN_carregados`.
- Controllers (`AbstractController`) disparam a função em thread com
  barra de progresso para não travar a UI.
- Tipos de dado (`ABData`) unificam raster, vetor, tabela e série
  temporal — o mesmo molde serve para incluir um modelo novo.

---

## Publicação

Paloschi, R. A. *Software aplicado a modelos de estimativa de
produtividade agrícola*. 2016. 99 f. Dissertação (Mestrado em Engenharia
Agrícola) — Universidade Estadual do Oeste do Paraná, Cascavel, 2016.

- Repositório: [tede.unioeste.br/handle/tede/2726](https://tede.unioeste.br/handle/tede/2726)
- Orientador: Jerry Adriani Johann
- Coorientador: Adair Santa Catarina
- Banca: Jansle Vieira Rocha · Erivelto Mercante
- Licença da dissertação: [CC BY-NC-ND 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/)

---

## Titularidade

Programa de computador **CyMP**, registro **INPI BR 51 2017 000623-7**,
titular **UNIOESTE**. Autores: Rennan Andres Paloschi, Jerry Adriani
Johann e Adair Santa Catarina.
