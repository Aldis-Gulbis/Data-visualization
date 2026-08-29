import pandas
import matplotlib.pyplot as plt

def visualize_data():
    fails = pandas.read_csv("../Prices.csv", delimiter =";")

    create_scatterplot(fails)
    create_boxplot(fails)
    create_barplot(fails)
    #create_linear_regression(fails)

def create_scatterplot(fails):
    fails["Datums"] = pandas.to_datetime(fails["Datums"], format = "%d %b %y")

    fails.plot.scatter(
        x = "Datums",
        y = "Benzīna cena (€/L)"
    )

    plt.title('Benzīna cena Eiropā')
    plt.xlabel('Datums')
    plt.ylabel('Cena (€/L)')
    plt.show()

def create_boxplot(fails):
    fails.boxplot(
        column = "Benzīna cena (€/L)",
        by = "Valsts nosaukums",
        figsize = (12, 7),
        grid = False)

    plt.title('Benzīna cena valstī pēdējo 10 nedēļu laikā')
    plt.xlabel('Valsts')
    plt.ylabel('Cena (€/L)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def create_barplot(fails):
    fails.plot.bar(
        x = "Valsts nosaukums",
        y = "Benzīna cena (€/L)"
    )

    plt.title('Benzīna cena valstī pēdējo 10 nedēļu laikā')
    plt.xlabel('Valsts')
    plt.ylabel('Cena (€/L)')
    plt.show()

#def create_linear_regression(fails):