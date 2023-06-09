# Spiderfoot-local-data-module

This module allows Spiderfoot to search local databases. This might be useful, when you want to include databases of leaks and breaches.

You can find the original Spiderfoot project here: https://github.com/smicallef/spiderfoot.
They are amazing <3!

It is not included in Spiderfoots standard installation, because it is not how Spiderfoot was designed to work.
But because I have developed this module, since I think it is useful, I wanted to make it available to others.

To use it, just copy the [sfp_local_data.py](https://github.com/her0marodeur/Spiderfoot-local-data-module/blob/main/sfp_local_data.py) to the modules directory of your Spiderfoot installation

If you want to read more about it, you can check out my blog: 

### Usage

Datasets have to be stored on the local machine. If you want to make them available for Spiderfoot, you have to include their full path in the settings of the module. Multiple files can be specified in a comma separated list. Below the path configuration you can select what kinds of data the module should listen for. So, if that kind of data is found during your scan, the module will automatically start searching for it in your local files. Do not forget to click “Save Changes”.

<img width="861" alt="sfp_settings" src="https://github.com/her0marodeur/Spiderfoot-local-data-module/assets/101996103/1a3e0c7a-4bad-41bf-bc13-96f4385004f0">


Afterwards you can select the module in the scan settings in the “By Module” tab.

![spf_local_screen](https://github.com/her0marodeur/Spiderfoot-local-data-module/assets/101996103/0e318c1e-c9b5-4dad-b6a4-ad8050314fc1)


If the scan finds anything in your local dataset, it will report the filename, line and content back as “Raw Data from RiRs/APIs”.

![sfp_result](https://github.com/her0marodeur/Spiderfoot-local-data-module/assets/101996103/81e7a604-3d87-4282-8f8e-2088ecb6f4f8)


This implementation was able to search a 30GB file in 3 minutes, which will slow the search process down, if a lot of data is present. Possible speed improvements could be done by implementing ripgrep, but this would require additional libraries. If you have any improvements, I am looking forward to your Pull Requests on Github.
