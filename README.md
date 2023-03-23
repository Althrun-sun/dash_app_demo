# Used car maket
This is a visualization app showing used cars

[Hosted on Render](https://used-car-maket.onrender.com/)

- Author: Althrun SUn


This is where you can view and visualize recent used car trade offers and performance data.

You can learn more about it by looking at the proposal.

The following is the basic information and functions of the used car app, please feel free to browse: 

* [Description of App](#description)
* [Usage and Installation](#usage-and-installation)
* [Contribution](#Contribution)
* [Contact](#contact)
* [License](#license)
* [Data Reference](#data-reference)

## Description

The visualization application includes a visualization panel that displays recent transaction data for used cars. The visualized used car transaction data is arranged according to the performance of the car, and users can use the filter box to understand detailed vehicle information.

The purpose of this visualization is to display the performance indicators and price trends of electric vehicles and fuel vehicles, and at the same time show the characteristics of different brands of manufacturers according to the visualization.


### Interaction components:

- There is a drop-down option box for vehicle type at the bottom left, you can select 'ALL', 'Electric', 'Fuel' to select the energy type.

- Just below is the range bar of 0-60 MPH Time, you can choose a model with a specific performance range.

- At the bottom right is the drop-down box of Car Model, the user can select a specific car model for visualization according to the Model.

### Plots

- Line chart: Show the relationship between vehicle performance and Price according to the filter below

- Pie chart: Shows the proportion of each brand in the current used car transaction data.

## Usage and Installation

You can use my APP, follow the bu'zhou below:

1. download the code:

```
https://github.com/Althrun-sun/used_car_market.git
```

2. prepare for the env:

```{r}
conda env create -f usedcar_env.yaml

```

3. last but not least run locally: 

- Open the folder with your familiar IDE, select the above environment as the interpreter, and start the app.

- Then open the URL: http://127.0.0.1:8050/:


## Contribution

I welcome anyone interested in contributing to the app for Kobe's career stats. The project is open-source, which means that anyone can view and contribute to the code on this GitHub repository.

If you are interested in getting involved, check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## Contact

If you have any new ideas or comments, please contact me in time: althrunsun@gmail.com

## License

Licensed under the terms of the [MIT license](LICENSE).

## Data Reference

The data used to visualize is extracted from https://www.kaggle.com/datasets/rkiattisak/sports-car-prices-dataset.If you are interested in the details of the dataset, please visit this URL.
