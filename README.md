<p align="center">
  <img width="180" src="./resources/MUSE_LOGO2.svg" alt="MUSE_LOGO">
  <h1 align="center">MUSE: Multi-engine Urban Expansion Simulator</h1>
</p>

# Paper Link:
<a href="https://doi.org/10.1080/136588197242329">Jianxin Yang, Wenwu Tang, Jian Gong, Rui Shi, Minrui Zheng, Yunzhe Dai,Simulating urban expansion using cellular automata model with spatiotemporally explicit representation of urban demand,Landscape and Urban Planning</a>

<a href="http://dx.doi.org/10.2139/ssrn.4171720">Yang, Jianxin and Yang, Shengbing and Li, Jingjing and Gong, Jian and Li, Jingye and Yuan, Man and Dai, Yunzhe, A Distance-Driven Urban Simulation Model (DISUSIM): Accounting For Urban Morphology At Multiple Landscape Levels</a>

<a href="https://doi.org/10.1080/136588197242329">CHRISTOPHER J. BROOKES (1997) A parameterized region-growing programme for site allocation on raster suitability maps, International Journal of Geographical Information Science</a>

# 1. Introduction

The **MUSE (Multi-engine Urban Expansion Simulator)** is a sophisticated cellular automata-based model meticulously designed for simulating urban growth. It integrates three distinct patch size generators and employs four diverse patch generation engines. The primary objective of MUSE is to accurately replicate the intricate patterns and procedures inherent in urban land expansion. The four patch-generating engines at the core of MUSE are:

- **Distance-Constrained Patch Shape (Dis-PGE)**
- **Neighborhood-Constrained Patch Shape (Nei-PGE)**
- **Spatially-Constrained Patch Shape (SPGE)**
- **Parameterized Patch-Growing Engine with Tradeoff between Maximized Cell Suitability and Optimized Patch Shape (PPGE)**

Furthermore, MUSE offers three patch size controllers to facilitate precise patch size determination:

- **Lognormal Distribution:** This Patch Size Controller operates under the assumption that patch areas follow a log-normal distribution (refer to Equation (4)).
- **Power Distribution:** The Patch Size Controller assumes that patch areas follow a power-law distribution (refer to Equation (5)).
- **History:** The third Patch Size Controller utilizes historical patch area sizes from previous periods.

With MUSE, users gain the capability to create diverse spatial patterns for urban land structures. They can construct patches of varying sizes and forms using different algorithms and generators, effectively mimicking the dynamic process of urban expansion. This versatile model holds immense potential for applications in decision support, land resource management, urban planning, and land use planning. Whether you are a researcher, urban planner, or decision-maker, MUSE empowers you to explore and understand the complexities of urban growth, contributing valuable insights to the field.

# 2. Installation
## Quick Installation

If you want to quickly use the software, you can download the release package from the following link: [Installation Link](xxx).

## Build Steps

If you prefer to build the project from the source, please follow these steps:

1. **Clone the Project:**
   ```bash
   git clone git@github.com:LandInsightLab/MUSE.git
2. **Install Python 3.11: Create a new environment named MUSE_ENV using Conda:**
   ```bash
   conda create -n MUSE_ENV python=3.11
3. **Activate the Environment: Switch to the MUSE_ENV environment:**
   ```bash
   conda activate MUSE_ENV
4. **Install Required Packages: Install the necessary packages listed in requirements.txt:**
   ```bash
   pip install -r requirements.txt
5. **Run the Application: Finally, run the application using the following command:**
   ```bash
   python.exe main.py