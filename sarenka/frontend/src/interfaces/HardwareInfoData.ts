interface HardwareInfoData {
  bios: {
    name: string;
    version: string;
  };
  computer_name: {
    name: string;
    system_type: string;
  };
  commputer_information: {
    commputer_serial_number: string;
    total_physical_memory: string;
    'mac_address???': string;
    computer_manufacturer: string;
  };
  operation_system: {
    name: string;
    version: string;
    manufacturer: string;
    configuration: string;
    build_type: string;
    os_architecture: string;
  };
  baseboard_information: {
    product: string;
    manufacturer: string;
    version: string;
    serialnumber: string;
  };
}

export default HardwareInfoData;
