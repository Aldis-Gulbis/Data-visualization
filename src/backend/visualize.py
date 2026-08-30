import pandas
import matplotlib.pyplot as plt
from PySide6.QtCore import QObject, Slot

class Create(QObject):
    @Slot(str, str, str)
    def visualize_data(self, country, category, plot_type):
        fails = pandas.read_csv("../Prices.csv", delimiter =";")

        if category == "Petrol prices":
            category = "Benzīna cena (€/L)"

        elif category == "Diesel prices":
            category = "Dīzeļdegvielas cena (€/L)"


        if plot_type == "Scatter plot":
            Create.create_scatterplot(fails, country, category)

        elif plot_type == "Box plot":
            Create.create_boxplot(fails, country, category)

        elif plot_type == "Bar plot":
            Create.create_barplot(fails, country, category)

        '''elif plot_type == "Linear regression":
            Create.create_linear_regression(fails, country, category)'''



    def create_scatterplot(fails, country, category):
        fails["Datums"] = pandas.to_datetime(fails["Datums"], format = "%d %b %y")

        if country == "All":
            fails.plot.scatter(
                x = "Datums",
                y = category
            )

            plt.title('Benzīna cena Eiropā')

        else:
            fails = fails[fails["Valsts nosaukums"] == country]

            fails.plot.scatter(
                x= "Datums",
                y= category
            )

            plt.title(f'Benzīna cena {country}')

        plt.xlabel('Datums')
        plt.ylabel('Cena (€/L)')
        plt.show()

    def create_boxplot(fails, country, category):

        if country == "All":
            fails.boxplot(
                column = category,
                by = "Valsts nosaukums",
                figsize = (12, 7),
                grid = False)

            plt.title('Benzīna cena Eiropā pēdējo 10 nedēļu laikā')
            plt.xlabel('Valsts')

        else:
            fails = fails[fails["Valsts nosaukums"] == country]

            fails.boxplot(
                column=category,
                by="Valsts nosaukums",
                figsize=(12, 7),
                grid=False)

            plt.title('Benzīna cena valstī pēdējo 10 nedēļu laikā')
            plt.xlabel('Valsts')


        plt.ylabel('Cena (€/L)')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    def create_barplot(fails, country, category):

        if country == "All":
            fails.plot.bar(
                x = "Valsts nosaukums",
                y = "Benzīna cena (€/L)"
            )

            plt.title('Benzīna cena Eiropā pēdējo 10 nedēļu laikā')
            plt.xlabel('Valsts')

        else:
            fails = fails[fails["Valsts nosaukums"] == country]

            fails.plot.bar(
                x="Datums",
                y="Benzīna cena (€/L)"
            )

            plt.title('Benzīna cena valstī pēdējo 10 nedēļu laikā')
            plt.xlabel('Valsts')


        plt.ylabel('Cena (€/L)')
        plt.show()

    #def create_linear_regression(fails):