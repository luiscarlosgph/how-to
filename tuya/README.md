How to setup Tuya lights with local control in Home Assistant
-------------------------------------------------------------

1. Get the device ID from the Tuya mobile phone app, in the app is called `Virtual ID`.
   
2. Get the local key from the Tuya developer website:

   2.1. Go to [https://iot.tuya.com](https://iot.tuya.com)
   
   2.2. If not created already, create a `Cloud Project` (use the Central Europe datacenter, it has to be the same the Tuya app uses in the phone)
      and then go to `Cloud Project` -> `Devices` -> `Link App Account` and link the cloud project to the Tuya app in the phone. 
   
   2.3. Click on `Cloud` -> `API Explorer` -> `Device Management` -> `Query Device Details`.
   
   2.4. Write the device ID and obtain the `Local Key` for the Tuya device.

3. Launch the following Python script to obtain the :
   
```python

TODO

```
