import QtQuick
import QtQuick.Controls
import view

RadioButton{
    id: radioButton

    property color idleColor: Colors.customButton.idle.border
    property color checkedColor: Colors.customButton.hover.border
    property real indicatorSize: 18

    indicator: Rectangle{
        implicitWidth: radioButton.indicatorSize
        implicitHeight: radioButton.indicatorSize
        radius: width / 2
        x: radioButton.leftPadding
        y: parent.height / 2 - height / 2

        color: "transparent"
        border.width: 2
        border.color: radioButton.checked
            ? radioButton.checkedColor
            : radioButton.idleColor

        Rectangle{
            anchors.centerIn: parent
            width: parent.width - 8
            height: width
            radius: width / 2
            color: radioButton.checkedColor
            visible: radioButton.checked
        }
    }

    contentItem: Text{
        text: radioButton.text
        font.pixelSize: 14
        color: Colors.window.text
        verticalAlignment: Text.AlignVCenter
        leftPadding: radioButton.indicator.width + radioButton.spacing
    }

    HoverHandler{
        acceptedDevices: PointerDevice.Mouse | PointerDevice.TouchPad
        cursorShape: Qt.PointingHandCursor
    }
}