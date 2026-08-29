import QtQuick
import QtQuick.Controls
import view

Button{
    id: optionButton

    property string selectedText: ""
    property var options: []

    height: 25
    width: 25

    background: Rectangle{
        color: "transparent"
    }

    contentItem: Image{
        source: {
            if(optionButton.hovered) return "../logos/option_hover.svg"
            return "../logos/option_idle.svg"
        }

        fillMode: Image.PreserveAspectFit
    }

    HoverHandler{
        acceptedDevices: PointerDevice.Mouse | PointerDevice.TouchPad
        cursorShape: Qt.PointingHandCursor
    }

    display: AbstractButton.IconOnly

    onClicked: menu.open()

    Menu{
        id: menu

        Instantiator{
            model: optionButton.options

            MenuItem{
                text: modelData
                onTriggered: { optionButton.selectedText = modelData }
            }

            onObjectAdded: (index, object) => menu.insertItem(index, object)
        }
    }
}