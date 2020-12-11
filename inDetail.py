import numpy as np
def reasons(tags):
    print(len(tags))
    (smps1,\
    smps2,\
    smps3,\
    plc_power,\
    vfd_Connection,\
    vfd_RunMode,\
    vfd_ConnectionFaulted,\
    vfd_Status,\
    vfd_TorqueDisabled,\
    vfd_Safety,\
    vfd_ResetRequired,\
    vfd_Command,\
    vfd_SafeTorqueOff,\
    vfd_Reset,\
    vfd_Power,\
    conveyorAxis,\
    ent_DigitalOutput,\
    ent_DataModeIO,\
    ent_DataValidity,\
    ent_diag1_IO1,\
    ent_diag1_IO2,\
    ent_diag1_IO3,\
    ent_diag1_IO4,\
    ent_diag1_IO4,\
    ent_diag1_IO4,\
    ent_diag1_IO1,\
    ent_diag2_IO2,\
    ent_diag2_IO3,\
    ent_PowerSupply,\
    ent_IO_DeviceError,\
    ent_IO_DeviceWarning,\
    ent_IO_DeviceNotification,\
    int_DigitalOutput,\
    int_DataModeIO,\
    int_DataValid,\
    int_diag1_IO1,\
    int_diag1_IO2,\
    int_diag1_IO3,\
    int_diag1_IO4,\
    int_diag1_IO5,\
    int_diag1_IO6,\
    int_diag2_IO1,\
    int_diag2_IO2,\
    int_diag2_IO3,\
    int_PowerSupply,\
    int_IO_DeviceError,\
    int_IO_DeviceWarning,\
    int_IO_DeviceNotification,\
    redLight,\
    yellowLight,\
    greenLight,\
    buzzer,\
    auto,\
    manual,\
    executeOrder,\
    extra) = tags

    powerSystem = smps1 and smps2 and smps3

    fault_reasons = [not smps1,\
    not smps2,\
    not smps3,\
    not plc_power,\
    not vfd_Power and (not vfd_Connection),\
    not vfd_Power and (not vfd_Safety),\
    not vfd_Power,\
    not ent_DataModeIO,\
    powerSystem and ent_diag1_IO1,\
    powerSystem and ent_diag1_IO2,\
    powerSystem and ent_diag1_IO3,\
    powerSystem and ent_diag1_IO4,\
    powerSystem and ent_diag1_IO5,\
    powerSystem and ent_diag1_IO6,\
    powerSystem and ent_Power,\
    powerSystem and ent_IOLinkDeviceError,\
    powerSystem and ent_IOLinkDeviceWarn,\
    powerSystem and not int_DataModeIO,\
    powerSystem and int_diag1_IO1,\
    powerSystem and int_diag1_IO2,\
    powerSystem and int_diag1_IO3,\
    powerSystem and int_diag1_IO4,\
    powerSystem and int_diag1_IO5,\
    powerSystem and int_diag1_IO5,\
    powerSystem and int_Power,\
    powerSystem and int_IOLinkDeviceError,\
    powerSystem and int_IOLinkDeviceWarn]

    status = np.array([])

    faults = np.array(['SMPS-1',\
    'SMPS-2',\
    'SMPS-3',\

    'Power to PLC',\

    'VFD Connections',\
    'VFD Safety Requirements',\
    'VFD Power Connection',\

    'Entry Sensor: not in IO Link Connection Mode',\
    'Entry Sensor: Low Voltage at Sensor Power Supply',\
    'Entry Sensor: Low Voltage at AUX Power Supply'\
    'Entry Sensor: Short Circuit',\
    'Entry Sensor: Short Circuit at Actuator Channel A',\
    'Entry Sensor: Short Circuit at Actuator Channel B',\
    'Entry Sensor: IO Link not verified',\
    'Entry Sensor: Connected to wrong device or No device found connected to IO Link'\
    'Entry Sensor: IO Link Device Warning',\
    'Entry Sensor: Power Supply Issues',\
    'Entry Sensor: Device Error',\
    'Entry Sensor: Device Warning',\

    'Intermediate Sensor: not in IO Link Connection Mode',\
    'Intermediate Sensor: Low Voltage at Sensor Power Supply',\
    'Intermediate Sensor: Low Voltage at AUX Power Supply'\
    'Intermediate Sensor: Short Circuit',\
    'Intermediate Sensor: Short Circuit at Actuator Channel A',\
    'Intermediate Sensor: Short Circuit at Actuator Channel B',\
    'Intermediate Sensor: IO Link not verified',\
    'Intermediate Sensor: Connected to wrong device or No device found connected to IO Link'\
    'Intermediate Sensor: IO Link Device Warning',\
    'Intermediate Sensor: Power Supply Issues',\
    'Intermediate Sensor: Device Error',\
    'Intermediate Sensor: Device Warning'])

    print('Reason for fault: ',faults[fault_reasons])

