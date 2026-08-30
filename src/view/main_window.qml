import view
import QtQuick
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow{
    id: root

    width: 500; height: 400;
    visible: true
    title: qsTr("Visualizer")
    font.family: "Times New Roman"

    color: Colors.window.background

    property string country: ""
    property string category: ""


    ColumnLayout{
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        anchors.verticalCenterOffset: 0
        spacing: 20

        Repeater{
            model: [
                {
                    label: "Select a country",
                    objName: "countryOptionButton",
                    options: ["Austria", "Belgium",
                         "Bulgaria", "Croatia",
                         "Cyprus", "Czechia",
                         "Denmark", "Estonia",
                         "Finland", "France",
                         "Germany", "Greece",
                         "Hungary", "Ireland",
                         "Italy", "Latvia",
                         "Lithuania", "Luxembourg",
                         "Malta", "Netherlands",
                         "Poland", "Portugal",
                         "Romania", "Slovakia",
                         "Slovenia", "Spain",
                         "Sweden", "All"]
                },
                {
                    label: "Select a category",
                    objName: "categoryOptionButton",
                    options: ["Petrol prices", "Diesel prices"]
                }
            ]

            delegate: Rectangle{
                width: 250
                height: 35
                Layout.alignment: Qt.AlignHCenter
                color: Colors.window.background
                border.color: Colors.window.border
                border.width: 2

                OptionButton{
                    id: optionButton
                    anchors.verticalCenter: parent.verticalCenter
                    options: modelData.options

                    onSelectedTextChanged: {
                        if(modelData.objName === "countryOptionButton")
                            root.country = selectedText

                        else if (modelData.objName === "categoryOptionButton")
                            root.category = selectedText
                    }
                }

                Text{
                    text: optionButton.selectedText === ""
                        ? modelData.label
                        : optionButton.selectedText

                    font.pixelSize: 18
                    anchors.centerIn: parent
                }
            }
        }

        ColumnLayout{
            Layout.alignment: Qt.AlignHCenter
            spacing: 10

            ButtonGroup{ id: graphGroup }

            Text{
                text: "Visualize"
                font.pixelSize: 18
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                horizontalAlignment: Text.AlignHCenter
            }

            ColumnLayout{

                spacing: 5

                Repeater{
                    model: ["Scatter plot", "Box plot", "Bar plot", "Linear regression"]

                    delegate: RadioButton{
                        text: modelData
                        ButtonGroup.group: graphGroup
                    }
                }

            }
        }

        RowLayout{
            spacing: 4

            Repeater{
                model: [
                    { text: "Show", action: "create" },
                    { text: "Update prices", action: "update" }
                ]

                delegate: FunctionButton{
                    text: modelData.text

                    onClicked:{
                        if (modelData.action === "update") {
                            updatePrices.get_values()

                        }else if (modelData.action === "create") {
                            var plotType = graphGroup.checkedButton
                                ? graphGroup.checkedButton.text
                                : ""

                            createPlot.visualize_data(root.country, root.category, plotType)
                        }
                    }
                }
            }
        }
    }
}