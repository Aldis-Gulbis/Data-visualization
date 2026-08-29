pragma Singleton
import QtQuick

QtObject{
    id: colors

    readonly property QtObject window: QtObject{
        readonly property color background: "#ffffff"
        readonly property color border: "#c3c3c3"
        readonly property color text: "#000000"
    }

    readonly property QtObject customButton: QtObject{
        readonly property color text: "#000000"

        readonly property QtObject idle: QtObject{
            readonly property color background: "#ffffff"
            readonly property color border: "#c3c3c3"

        }

        readonly property QtObject hover: QtObject{
            readonly property color background: "#c3c3c3"
            readonly property color border: "#c3c3c3"
        }

        readonly property QtObject pressed: QtObject{
            readonly property color background: "#c3c3c3"
            readonly property color border: "#7f7f7f"
        }
    }
}