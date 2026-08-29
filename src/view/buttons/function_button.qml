import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import view

TabButton{
    id: functionButton

    Layout.preferredWidth: 200
    Layout.preferredHeight: 40

    contentItem: Item{
        anchors.fill: parent

        Text{
            anchors.centerIn: parent
            font.pixelSize: 18
            text: functionButton.text

            color: Colors.customButton.text
        }
    }

    background: Rectangle{
        color: functionButton.pressed
            ? Colors.customButton.pressed.background
            : functionButton.hovered
                ? Colors.customButton.hover.background
                : Colors.customButton.idle.background

        border.color: functionButton.pressed
            ? Colors.customButton.pressed.border
            : functionButton.hovered
                ? Colors.customButton.hover.border
                : Colors.customButton.idle.border

        border.width: 2
    }

    HoverHandler {
        acceptedDevices: PointerDevice.Mouse | PointerDevice.TouchPad
        cursorShape: Qt.PointingHandCursor
    }
}