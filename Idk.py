import subprocess

def get_wifi_networks():
    try:
        output = subprocess.check_output(['nmcli', '-f', 'SSID', 'dev', 'wifi'])
        networks = output.decode().split('\n')[1:]
        return [network.strip() for network in networks if network.strip()]
    except subprocess.CalledProcessError:
        return []

def select_wifi_network():
    networks = get_wifi_networks()
    if not networks:
        print("No WiFi networks found.")
        return

    print("Available WiFi networks:")
    for i, network in enumerate(networks):
        print(f"{i+1}. {network}")

    while True:
        try:
            choice = int(input("Enter the number of the network you want to connect to: "))
            if 1 <= choice <= len(networks):
                return networks[choice-1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

selected_network = select_wifi_network()
print(f"Selected WiFi network: {selected_network}")