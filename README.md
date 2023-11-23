<p align="center">
  <img width="180" src="./resources/logo/MUSE_LOGO2.png" alt="MUSE_LOGO">
  <h1 align="center">MUSE: Multi-engine Urban Expansion Simulator</h1>
</p>

# Paper Link:
<a href="https://doi.org/10.1080/136588197242329">Jianxin Yang, Wenwu Tang, Jian Gong, Rui Shi, Minrui Zheng, Yunzhe Dai,Simulating urban expansion using cellular automata model with spatiotemporally explicit representation of urban demand,Landscape and Urban Planning</a>

<a href="http://dx.doi.org/10.2139/ssrn.4171720">Yang, Jianxin and Yang, Shengbing and Li, Jingjing and Gong, Jian and Li, Jingye and Yuan, Man and Dai, Yunzhe, A Distance-Driven Urban Simulation Model (DISUSIM): Accounting For Urban Morphology At Multiple Landscape Levels</a>

<a href="https://doi.org/10.1080/136588197242329">CHRISTOPHER J. BROOKES (1997) A parameterized region-growing programme for site allocation on raster suitability maps, International Journal of Geographical Information Science</a>

# 1. Introduction
The **MUSE (Multi-engine Urban Expansion Simulator)** is a sophisticated cellular automata-based model meticulously designed for simulating urban growth. It integrates three distinct patch size generators and employs four diverse patch generation techniques. The primary objective of MUSE is to accurately replicate the intricate patterns and procedures inherent in urban land expansion. The four patch-generating algorithms at the core of MUSE are:

- **Distance-Constrained Patch Shape (Dis-PGE)**
- **Neighborhood-Constrained Patch Shape (Nei-PGE)**
- **Spatially-Constrained Patch Shape (SPGE)**
- **Parameterized Patch-Growing Engine with Tradeoff between Maximized Cell Suitability and Optimized Patch Shape (PPGE)**

Furthermore, MUSE offers three patch size controllers to facilitate precise patch size determination:

- **Lognormal Distribution:** This Patch Size Controller operates under the assumption that patch areas follow a log-normal distribution (refer to Equation (4)).
- **Power Distribution:** The Patch Size Controller assumes that patch areas follow a power-law distribution (refer to Equation (5)).
- **History:** The third Patch Size Controller utilizes historical patch area sizes from previous periods.

With MUSE, users gain the capability to create diverse spatial patterns for urban land structures. They can construct patches of varying sizes and forms using different algorithms and generators, effectively mimicking the dynamic process of urban expansion. This versatile model holds immense potential for applications in decision support, land resource management, urban planning, and land use planning. Whether you are a researcher, urban planner, or decision-maker, MUSE empowers you to explore and understand the complexities of urban growth, contributing valuable insights to the fiel

# 2. Data Preparation

To set up MUSE, navigate to the installation directory, where the example files are stored. This directory contains 9 essential files, including 4 CSV files and 5 TIFF files, crucial for MUSE's operation. Data preparation techniques using these sample files are detailed in the documentation.

## 2.1 CSV Documents

### 2.1.1 Stepwise Demand of Urban Development

- **File**: [\_04_StepwiseIncrement.csv](_TEST_FILES/_04_StepwiseIncreasment.csv)
- **Description**: Records yearly rise in the number of urban land grid cells and the proportion of organic patches from 2005 to 2015.

### 2.1.2 History Patch Size Controller Data

- **File**: [\_09_History_CellSize.csv](_TEST_FILES/_09_History_CellSize.csv)
- **Description**: Records 5000 patch sizes in historical periods.

### 2.1.3 Gaussian Correction Parameter Data

- **File**: [\_08_GaussianParams.csv](_TEST_FILES/_08_GaussianParams.csv)
- **Description**: Documents mean parameter 'b' and standard deviation parameter 'c' for Gaussian correction from 2005 to 2015.

### 2.1.4 Stepwise Percent of Organic Growth Data

- **File**: [\_03_StepwiseOrganic.csv](_TEST_FILES/_03_StepwiseOrganic.csv)
- **Description**: Documents area ratios of newly added organic patches from 2005 to 2015.

Feel free to refer to the documentation for detailed information on data preparation and utilization in MUSE.

# 3. Data Preparation

To ensure the proper operation of the MUSE program, users are required to provide 5 TIF files containing specific spatial data crucial for model execution. These files cover essential information such as the distribution of urban construction land at the base and model validation simulation sites, probability of urban construction appropriateness, urban development construction constraints, and urban center point data. It is imperative that these files maintain rigorous consistency in spatial features, including the same number of rows and columns, projection coordinates, and spatial resolution. Refer to Figure 3-6 for an example file.

![Figure 2-1: Model Input Data Files](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/2-1%20Model%20Input%20Data%20Files.png)

## 2.2 TIF Files Overview

### 2.2.1. Base Period Urban Construction Land Data
- **Function**: Describes the spatial distribution of urban construction land during the baseline period. 
- **Format**: Values are denoted by 0 and 1, where 0 signifies undeveloped land and 1 represents developed urban areas.
- **File Name**: [_01_UrbanLand2005_Changsha.tif](_TEST_FILES/_01_UrbanLand2005_Changsha.tif)

### 2.2.2. Model Validation Simulation Urban Construction Land Data
- **Function**: Reflects the urban construction land distribution at the validation simulation point.
- **Format**: Similar to the base period data, values range from 0 to 1, representing undeveloped and developed land.
- **File Name**: [_06_UrbanLand2015_Changsha.tif](_TEST_FILES/_06_UrbanLand2015_Changsha.tif)

### 2.2.3. Urban Construction Suitability Probability File
- **Function**: Represents the probability of urban construction suitability based on diverse driving factor data.
- **Format**: Values range from 0 to 1, where higher values indicate higher suitability for urban development.
- **File Name**: [_05_UrbanSuitability2005.tif](_TEST_FILES/_05_UrbanSuitability2005.tif)

### 2.2.4. Urban Development Construction Restriction File
- **Function**: Provides information on spatial constraints for urban development, such as water bodies, protected farmland, historical and cultural conservation areas, etc.
- **Format**: Values are expressed as 0 for open development areas and 1 for restricted development areas.
- **File Name**: [_02_Constraints_Water.tif](_TEST_FILES/_02_Constraints_Water.tif)

### 2.2.5. Urban Center Point Data
- **Function**: Specifies the locations of urban center points, typically situated in areas like central business districts (CBD), government institutions, or key city hubs.
- **Format**: Values vary between 0 and 1, with 0 representing non-center grid cells and 1 denoting center grid cells.
- **File Name**: [_07_CityCenter.tif](_TEST_FILES/_07_CityCenter.tif)

Feel free to refer to Table 1 for a quick reference to each model input data file, including data sources, value ranges, and corresponding example files.

# Table 1: List of Model Input Data Files

| File Names                                                  | Data Sources                               | Values Range                                         | Corresponding Example File                     |
|-------------------------------------------------------------|--------------------------------------------|------------------------------------------------------|------------------------------------------------|
| Simulated Base-Year Urban Construction Land Spatial Distribution Data | Remote Sensing Data, Land Survey Data, etc. | 0 (Undeveloped Land), 1 (Developed Land)             | [_01_UrbanLand2005_Changsha.tif](_TEST_FILES/_01_UrbanLand2005_Changsha.tif)   |
| Model Validation Urban Construction Land Spatial Distribution Data | Remote Sensing Data, Land Survey Data, etc. | 0 (Undeveloped Land), 1 (Developed Land)             | [_06_UrbanLand2015_Changsha.tif](_TEST_FILES/_06_UrbanLand2015_Changsha.tif)   |
| Urban Construction Suitability Probability File              | Evaluated based on Driver Factor Data     | 0-1 (Urban Construction Suitability Probability)     | [_05_UrbanSuitability2005.tif](_TEST_FILES/_05_UrbanSuitability2005.tif)     |
| Urban Development and Construction Restriction File         | Set based on Real Conditions and Simulated Scenario Requirements | 0 (Developable Area), 1 (Restricted Development Area) | [_02_Constraints_Water.tif](_TEST_FILES/_02_Constraints_Water.tif)      |
| Urban Center Point Data                                      | Set based on Real Conditions and Simulated Scenario Requirements | 0 (Non-Center Point), 1 (Center Point)               | [_07_CityCenter.tif](_TEST_FILES/_07_CityCenter.tif)              |


# 3. User Guide

**Note:** The following installation steps apply only if you are using the downloaded [MUSE_Setup_1.0.exe](https://github.com/Mr-ShiRui/MUSE/releases/tag/v1.0.0). If the software environment is cloned, the installation steps are unnecessary.

## 3.1 Software Installation

## 3.1 Software Installation

### Step 1:
Double-click the software installation package [MUSE_Setup_1.0.exe](https://github.com/Mr-ShiRui/MUSE/releases/tag/v1.0.0) and select the installation mode. It is recommended to choose "Install for all users".

![Figure 3-1: MUSE Shortcut](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-1%20MUSE%20Shortcut.png)
![Figure 3-2: Installation Mode Selection](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-2%20Installation%20Mode%20Selection.png)

### Step 2:
Customize the installation directory (default or modified) and select the Start menu folder.

![Figure 3-3: Installation Directory Customization](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-3%20Installation%20Directory%20Customization.png)
![Figure 3-4: Start Menu Folder Selection](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-4%20Start%20Menu%20Folder%20Selection.png)

### Step 3:
Check the box for "Create desktop shortcut," then verify the installation information, and click on "Install" to proceed.

![Figure 3-5: Desktop Shortcut Creation Selection](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-5%20Desktop%20Shortcut%20Creation%20Selection.png)
![Figure 3-6: Installation Information Confirmation](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-6%20Installation%20Information%20Confirmation.png)

After the installation progress is complete, click Finish to complete the installation.

![Figure 3-7: Installation Progress](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-7%20Installation%20Progress.png)
![Figure 3-8: Installation Completed](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-8%20Installation%20Completed.png)

## 3.2 Running the Software

### 3.2.1 Model Validation

**Step 1:** Find the MUSE shortcut, double-click to run it, and access the main program interface as shown in Figure 4-9.

![Figure 4-9: The main interface of MUSE](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-9%20The%20main%20interface%20of%20MUSE.png)

**Step 2:** Enter the required data for the model in the input data area, inputting each dataset as per the corresponding relationship outlined in Table 2.

**Table 2: Overview of Input File Information**

| Parameters Name                    | File Types                                  | Example Files                                |
|-------------------------------------|---------------------------------------------|---------------------------------------------|
| Simulated Initial Urban Land        | Base-year Urban Construction Land Data      | _01_UrbanLand2005_Changsha.tif              |
| Simulated Final Urban Land          | Target-year Urban Construction Land Data    | _06_UrbanLand2015_Changsha.tif              |
| Development Restriction Factors     | Urban Development Restriction File           | _02_Constraints_Water.tif                   |
| Urban Construction Suitability      | Urban Construction Suitability Probability File | _05_UrbanSuitability2005.tif             |
| New Urban Land Area                  | Urban Construction Land Increment           | _04_StepwiseIncreasment.csv                 |
| Stepwise percent of organic growth   | Patch Organic Growth Category Ratio Data    | _03_StepwiseOrganic.csv                     |

**Step 3:** Please indicate if you want to use the Urban Expansion Control Module. If you want to use this module, toggle the switch on the left side of the space to enable it. Enter data for urban center points, Gaussian correction parameters, and the weight showing the impact of the urban center on urban land development (value range: 0-1). If you do not want to use this functionality, simply turn it off. Table 3 shows the relationships for each dataset.

...
**Table 3: Overview of Input File Information for Expansion Degree Control Module**

| Parameters Name       | File Types                      | Example Files                  |
|------------------------|---------------------------------|-------------------------------|
| Urban Center           | City center raster data          | _07_CityCenter.tif            |
| Gaussian Parameters    | Parameters data based on Gaussian correction rule | _08_GaussianParams.tif     |

**Step 4:** It is critical to configure five vital parameters under the model's global parameter section. Specifically, during setup, the overall duration of the simulation period (simulation finish - simulation start) must comply with certain guidelines: its value must not exceed the timeframe indicated in the urban construction land increment data. To be more specific, this value is calculated by subtracting one from the total number of rows in the urban construction land increment data, which represents the duration. For example, if the urban development land increment data (including headers) contains 11 rows of information spanning the years 2006 to 2015, the aforementioned duration parameter would be 10 years. As a result, when defining the simulation period length, it should be less than or equal to 10 years. Essentially, the time difference between the simulation's finish and beginning should not be more than ten years. The table below details the definitions and acceptable value ranges for each parameter in the global parameter section.

**Table 4: Model Parameters**

| Parameter Name        | Parameter Description                                              | Value Range   |
|------------------------|---------------------------------------------------------------------|---------------|
| Starting time          | Starting step of the model simulation                               | 1~36767       |
| Ending time            | Ending step of the model simulation                                 | 1~36767       |
| Location uncertainty   | Proportion of non-randomly selected seeds in the seed selection process for patches | 0~1   |
| Pruning parameter      | The size of the patch seed unit library is equal to the total number of developable grid units sorted in descending order based on development probability, multiplied by a pruning coefficient | 0~1 |
| Type of neighborhood    | In the context of 4-neighborhood, it corresponds to the Von Neumann neighborhood, while in the case of 8-neighborhood, it corresponds to the Moore neighborhood | 4, 8          |

**Step 5:** Please select one of the three patch size generators. Among these options, "lognormal distribution" and "power law distribution" are predefined generation strategies integrated into the model. They assume that the sizes of newly generated patches adhere to either a lognormal or power law distribution, respectively. If you opt for the Historical Period Patch size, you'll be required to furnish a CSV file containing customized patch sizes formatted as described in section 3.1. The "lognormal distribution" strategy employs a random generator based on the lognormal distribution to regulate the sizes of generated patches. This procedure involves entering parameters such as the lognormal distribution's expectation and logarithmic standard deviation. Conversely, the "power law distribution" strategy utilizes a random generator based on the power law distribution to control patch area sizes. To govern the distribution of patch sizes, this approach requires the input of parameters such as the proportional constant and power.

**Step 6:** Choose the patch generation engine. MUSE provides four algorithms for patch generation engines. When you pick the Neighborhood Controlled Patch Generation Engine, the model will automatically set the patch position uncertainty parameter to 1 and the neighborhood type parameter to 8. This adjustment is due to the Neighborhood Controlled Patch Generation Engine's mechanism, which is based on a stochastic process and a repeating neighborhood mechanism. The following table details the parameters for each engine.

**Table 5: Explanation of Engine Control Parameters**

| Engine Name | Parameter Name   | Parameter Description  | Default Value | Value Range |
|-------------|-------------------|-------------------------|---------------|-------------|
| SPGE        | -                 | This engine does not require any input parameters. | -             | -           |
| PPGE        | N                 | N and D together influence the longest dimension of the plaque | 1             | Greater than 0 |
|             | D                 | -                       | 2             | Greater than 0 |
|             | A                 | the number of arms       | 2             | Not less than 0 |
|             | O                 | patch orientation        | 45            | Not less than 0 |
|             | suit_weight       | The weight of the patch shape during the generation process | 0.5           | 0-1         |
|             | shape_weight      | The weight of suitability during the generation process | 0.5           | 0-1         |
| Nei-PGE     | beta              | Whether neighborhood repetition based on seed units controls the compactness of the patch | 1.6           | Greater than 0 |
| Dis-PGE     | delta             | Control of patch shape based on a distance decay mechanism | 2             | Any real number |

**Step 7:** To initiate the model execution, click on the 'Start Simulation' button. The program will transition into the running state, and upon completion of the simulation, the 'Save Simulation Data' button will shift from being inactive to an active clickable state, as illustrated in 

![Figure 3-10: The interface after the execution has completed](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-10%20The%20interface%20after%20the%20execution%20has%20completed.png)

**Step 8:** To assess the simulation accuracy, MUSE offers three indices: Kappa, Operation Accuracy (OA), and Figure of Merit (FOM). These indices are utilized to characterize the model's simulation accuracy.

**Step 9:** If the model's simulation results meet the accuracy requirements, you can select 'Save Simulation Data.' After specifying the storage path and file name for the simulation results, you can save the model's output from the simulation.

### 3.2.2 Scenario Simulation

After completing model verification, users can access the scenario prediction mode by navigating to "Preferences" > "Mode" > "Scenario Prediction". The operational process within this mode mirrors that of the model verification mode. However, in the scenario prediction module, users are not required to input urban land data at the simulation's conclusion, and the model does not display relevant accuracy indicators. Refer to Figure 3-11 for the interface of the scenario prediction module.

When the program enters the scenario prediction mode, it uses the urban land data observed at the end of the simulation verification stage (observation data, not simulation results) as the initial urban land data for the prediction stage. Similarly, the simulation time period within the model parameters automatically moves from past to future time points.

The necessary inputs for users in scenario prediction include data on development limitation factors, new urban land areas, and urban construction suitability. Users should adjust these inputs based on their forecasts and expectations concerning future urban development. Users also have the option to modify other parameters to simulate various scenarios or retain parameters utilized during the model validation phase.

Once these preparations are finalized, users simply need to click on the "Run" button to commence the simulation for scenario prediction. After the simulation process is completed, users can save the predicted results at a specified location by clicking on "Save Simulation Data".

![Figure 4-11: Scenario Simulation Interface](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-11%20Scenario%20Simulation%20Interface.png)

### 3.3. Saving and Opening Parameter Files

Users have the option to save the configured input files and various parameters by using the 'File - Save' function, creating a .mud file for convenient access in subsequent operations. This method eliminates the necessity to reset parameters individually. The saved parameter file can be accessed and loaded via the 'File - Open' function.

### 3.4. Explanation of Simulation Results

Upon reviewing the completed simulation results, you'll notice that the pixel values range from 0 to 'n'. In the symbol system of ArcGIS software, unique values are displayed sequentially, presenting pixel values as 0, 1, i...n. Here, 'i' represents the initial value set at the beginning of the simulation plus 1, while 'n' represents the value set at the end of the simulation. This setup provides a clear insight into the spatial arrangement of newly added urban construction land at each time step.

![Figure 4-12: Simulation results of urban construction land in Changsha from 2005 to 2015](https://github.com/LandInsightLab/MUSE/blob/master/resources/doc/3-12%20Simulation%20results%20of%20urban%20construction%20land%20in%20Changsha%20from%202005%20to%202015.png)



