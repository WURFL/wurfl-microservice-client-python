from wmclient import *

try:
    client = WmClient.create("http", "localhost", 8080, "")

    info = client.get_info()
    print("Printing WM server information")
    print("WURFL API version: " + info.wurfl_api_version)
    print("WM server version:  " + info.wm_version)
    print("Wurfl file info: " + info.wurfl_info)

    ua = "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) " \
         "Chrome/56.0.2924.87 Mobile Safari/537.36 "

    client.set_requested_static_capabilities(["brand_name", "model_name"])
    client.set_requested_virtual_capabilities(["is_smartphone", "form_factor"])
    print()
    print("Detecting device for user-agent: " + ua);

    # Perform a device detection calling WM server API
    device = client.lookup_useragent(ua)

    if device.error is not None and len(device.error) > 0:
        print("An error occurred: " + device.error)
    else:
        # Let's get the device capabilities and print some of them
        capabilities = device.capabilities
        print("Detected device WURFL ID: " + capabilities["wurfl_id"])
        print("Device brand & model: " + capabilities["brand_name"] + " " + capabilities["model_name"])
        print("Detected device form factor: " + capabilities["form_factor"])
        if capabilities["is_smartphone"] == "true":
            print("This is a smartphone")
            # Iterate over all the device capabilities and print them
            print("All received capabilities");
            for k in capabilities:
                print(k + ": " + capabilities[k])

            # Get all the device manufacturers, and print the first twenty
            print()
            limit = 20
            deviceMakes = client.get_all_device_makes()
            print("Print the first {} Brand of {} retrieved from server\n".format(limit, len(deviceMakes)))

            # Sort the device manufacturer names
            list.sort(deviceMakes)
            for i in range(limit):
                print(" - {}\n".format(deviceMakes[i]))

            # Now call the WM server to get all device model and marketing names produced by Apple
            print("Print all Model for the Apple Brand")
            devNames = client.get_all_devices_for_make("Apple")

            for model_mkt_name in devNames:
                print(" - {} {}\n".format(model_mkt_name.brand_name, model_mkt_name.model_name))

            # Now call the WM server to get all operative system names
            print("Print the list of OSes")
            oses = client.get_all_OSes()
            # Sort and print all OS names
            list.sort(oses)
            for os in oses:
                print(" - {}\n".format(os))

            # Let's call the WM server to get all version of the Android OS
            print("Print all versions for the Android OS")
            osVersions = client.get_all_versions_for_OS("Android")
            # Sort all Android version numbers and print them.
            list.sort(osVersions)
            for ver in osVersions:
                print(" - {}\n".format(ver))

except WmClientError as wme:
    # problems such as network errors  or internal server problems
    print("An error has occurred: " + wme.message)