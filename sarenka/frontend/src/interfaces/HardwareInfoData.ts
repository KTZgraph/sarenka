interface HardwareInfoData {
  bios: {
    name: string;
    version: string;
  };
  computer_information: {
    name: string;
    system_type: string;
    computer_serial_number: string;
    total_physical_memory: string;
    mac_address: string;
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
  motherboard_information: {
    product: string;
    manufacturer: string;
    version: string;
    serialnumber: string;
  };
  hard_drive_info: {
    NTFS: {
      freespace: string;
      systemname: string;
      filesystem: string;
      size: string;
      volumeserialnumber: string;
    };
  };
}

export default HardwareInfoData;
