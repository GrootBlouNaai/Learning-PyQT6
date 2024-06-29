import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QRadioButton,
    QButtonGroup, QFormLayout, QGroupBox
)

class AP2ConfigWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AP 2 Configuration")
        self.setGeometry(100, 100, 600, 450)

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Top bar with back, forward buttons and URL
        self.setup_top_bar(main_layout)

        # Basic Configuration Group Box
        self.setup_basic_config(main_layout)

        # Wireless and Wired Subforms
        self.setup_subforms(main_layout)

        # Security Configuration Group Box
        self.setup_security_config(main_layout)

        # Bottom buttons
        self.setup_bottom_buttons(main_layout)

    def setup_top_bar(self, main_layout):
        top_bar_layout = QHBoxLayout()
        self.back_button = QPushButton("Back")
        self.forward_button = QPushButton("Forward")
        self.url_label = QLabel("https://ap2.setup.do")
        top_bar_layout.addWidget(self.back_button)
        top_bar_layout.addWidget(self.forward_button)
        top_bar_layout.addWidget(self.url_label)
        main_layout.addLayout(top_bar_layout)
        
    def setup_basic_config(self, main_layout):
        basic_config_group = QGroupBox("Basic Configuration")
        basic_config_layout = QFormLayout()

        self.ap_name_label = QLabel("Access Point Name")
        self.ap_name_entry = QLineEdit("AP2")
        self.ap_name_entry.setReadOnly(True)

        self.ip_address_label = QLabel("IP Address")
        self.ip_address_entry = QLineEdit()
        #self.ip_address_entry.setFixedWidth(150)  # Adjust the width as needed

        self.subnet_label = QLabel("/")
        self.subnet_entry = QLineEdit()
        self.subnet_entry.setFixedWidth(50)  # Smaller entry box for subnet

        self.gateway_label = QLabel("Gateway")
        self.gateway_entry = QLineEdit("192.168.1.1")
        self.gateway_entry.setReadOnly(True)

        self.ssid_label = QLabel("SSID")
        self.ssid_entry = QLineEdit()

        self.ssid_broadcast_label = QLabel("SSID Broadcast")
        self.ssid_broadcast_group = QButtonGroup()
        self.ssid_broadcast_yes = QRadioButton("Yes")
        self.ssid_broadcast_no = QRadioButton("No")
        self.ssid_broadcast_group.addButton(self.ssid_broadcast_yes)
        self.ssid_broadcast_group.addButton(self.ssid_broadcast_no)

        basic_config_layout.addRow(self.ap_name_label, self.ap_name_entry)

        # Combine ip_address_entry and subnet_entry into a single layout
        ip_subnet_layout = QHBoxLayout()
        ip_subnet_layout.addWidget(self.ip_address_entry)
        ip_subnet_layout.addWidget(self.subnet_label)
        ip_subnet_layout.addWidget(self.subnet_entry)
        basic_config_layout.addRow(self.ip_address_label, ip_subnet_layout)

        basic_config_layout.addRow(self.gateway_label, self.gateway_entry)
        basic_config_layout.addRow(self.ssid_label, self.ssid_entry)

        ssid_broadcast_layout = QHBoxLayout()
        ssid_broadcast_layout.addWidget(self.ssid_broadcast_yes)
        ssid_broadcast_layout.addWidget(self.ssid_broadcast_no)
        basic_config_layout.addRow(self.ssid_broadcast_label, ssid_broadcast_layout)

        basic_config_group.setLayout(basic_config_layout)
        main_layout.addWidget(basic_config_group)
        
    def setup_subforms(self, main_layout):
        subforms_layout = QHBoxLayout()

        # Wireless Group
        wireless_group = QGroupBox("Wireless")
        wireless_layout = QFormLayout()
        self.mode_label = QLabel("Mode")
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["B", "G"])
        self.channel_label = QLabel("Channel")
        self.channel_combo = QComboBox()
        self.channel_combo.addItems([str(i) for i in range(1, 12)])
        wireless_layout.addRow(self.mode_label, self.mode_combo)
        wireless_layout.addRow(self.channel_label, self.channel_combo)
        wireless_group.setLayout(wireless_layout)
        subforms_layout.addWidget(wireless_group)

        # Wired Group
        wired_group = QGroupBox("Wired")
        wired_layout = QFormLayout()
        self.speed_label = QLabel("Speed")
        self.speed_group = QButtonGroup()
        self.auto_speed = QRadioButton("Auto")
        self.speed_100 = QRadioButton("100")
        self.speed_1000 = QRadioButton("1000")
        self.speed_group.addButton(self.auto_speed)
        self.speed_group.addButton(self.speed_100)
        self.speed_group.addButton(self.speed_1000)
        self.duplex_label = QLabel("Duplex")
        self.duplex_group = QButtonGroup()
        self.auto_duplex = QRadioButton("Auto")
        self.half_duplex = QRadioButton("Half")
        self.full_duplex = QRadioButton("Full")
        self.duplex_group.addButton(self.auto_duplex)
        self.duplex_group.addButton(self.half_duplex)
        self.duplex_group.addButton(self.full_duplex)

        speed_layout = QHBoxLayout()
        speed_layout.addWidget(self.auto_speed)
        speed_layout.addWidget(self.speed_100)
        speed_layout.addWidget(self.speed_1000)
        wired_layout.addRow(self.speed_label, speed_layout)

        duplex_layout = QHBoxLayout()
        duplex_layout.addWidget(self.auto_duplex)
        duplex_layout.addWidget(self.half_duplex)
        duplex_layout.addWidget(self.full_duplex)
        wired_layout.addRow(self.duplex_label, duplex_layout)

        wired_group.setLayout(wired_layout)
        subforms_layout.addWidget(wired_group)
        main_layout.addLayout(subforms_layout)

    def setup_security_config(self, main_layout):
        security_group = QGroupBox("Security Configuration")
        security_layout = QFormLayout()
        self.security_label = QLabel("Security Settings")
        self.security_group = QButtonGroup()
        self.none_radio = QRadioButton("None")
        self.wep_radio = QRadioButton("WEP")
        self.wpa_radio = QRadioButton("WPA")
        self.wpa2_radio = QRadioButton("WPA2")
        self.wpa2_enterprise_radio = QRadioButton("WPA2 Enterprise")
        self.security_group.addButton(self.none_radio)
        self.security_group.addButton(self.wep_radio)
        self.security_group.addButton(self.wpa_radio)
        self.security_group.addButton(self.wpa2_radio)
        self.security_group.addButton(self.wpa2_enterprise_radio)
        self.key_label = QLabel("Key/Passphrase")
        self.key_entry = QLineEdit()

        security_radio_layout = QHBoxLayout()
        security_radio_layout.addWidget(self.none_radio)
        security_radio_layout.addWidget(self.wep_radio)
        security_radio_layout.addWidget(self.wpa_radio)
        security_radio_layout.addWidget(self.wpa2_radio)
        security_radio_layout.addWidget(self.wpa2_enterprise_radio)
        security_layout.addRow(self.security_label, security_radio_layout)

        security_layout.addRow(self.key_label, self.key_entry)
        security_group.setLayout(security_layout)
        main_layout.addWidget(security_group)

    def setup_bottom_buttons(self, main_layout):
        bottom_layout = QHBoxLayout()
        self.reset_button = QPushButton("Reset to Default")
        self.save_button = QPushButton("Save/Close")
        bottom_layout.addWidget(self.reset_button)
        bottom_layout.addWidget(self.save_button)
        main_layout.addLayout(bottom_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AP2ConfigWindow()
    window.show()
    sys.exit(app.exec())
