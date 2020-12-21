import React from 'react';
import { storiesOf } from '@storybook/react';
import StoryRouter from 'storybook-react-router';
import InstalledSoftware from './InstalledSoftware';

const dummyData = {
  key:
    'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
  softwares: [
    {
      name: '7-Zip 19.00 (x64)',
      location: 'C:\\Program Files\\7-Zip\\',
      version: '19.00',
      date: null,
      vendor: 'Igor Pavlov',
    },
    {
      name: 'Android Studio',
      location: null,
      version: '3.6',
      date: null,
      vendor: 'Google LLC',
    },
    {
      name: 'AutoHotkey 1.1.32.00',
      location: null,
      version: '1.1.32.00',
      date: null,
      vendor: 'Lexikos',
    },
    {
      name: 'EPSON WF-7610 Series Printer Uninstall',
      location: null,
      version: null,
      date: null,
      vendor: 'SEIKO EPSON Corporation',
    },
    {
      name: 'Firefox Developer Edition 78.0 (x64 pl)',
      location: 'C:\\Program Files\\Firefox Developer Edition',
      version: '78.0',
      date: null,
      vendor: 'Mozilla',
    },
    {
      name: 'Git version 2.25.1',
      location: 'C:\\Program Files\\Git\\',
      version: '2.25.1',
      date: '20200325',
      vendor: 'The Git Development Community',
    },
    {
      name: 'Logitech Options',
      location: null,
      version: '8.10.84',
      date: null,
      vendor: 'Logitech',
    },
    {
      name: 'Mozilla Maintenance Service',
      location: null,
      version: '76.0',
      date: null,
      vendor: 'Mozilla',
    },
    {
      name: 'Microsoft Office 365 ProPlus - pl-pl',
      location: 'C:\\Program Files\\Microsoft Office',
      version: '16.0.12624.20442',
      date: null,
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'PostgreSQL 9.5 ',
      location: 'C:\\Program Files\\PostgreSQL\\9.5',
      version: '9.5',
      date: 1588790686,
      vendor: 'PostgreSQL Global Development Group',
    },
    {
      name: 'R for Windows 3.6.3',
      location: 'C:\\Program Files\\R\\R-3.6.3\\',
      version: '3.6.3',
      date: '20200328',
      vendor: 'R Core Team',
    },
    {
      name: 'VLC media player',
      location: 'C:\\Program Files\\VideoLAN\\VLC',
      version: '3.0.8',
      date: null,
      vendor: 'VideoLAN',
    },
    {
      name: 'WinMerge 2.16.4.0 x64',
      location: 'C:\\Program Files\\WinMerge\\',
      version: '2.16.4.0',
      date: '20200403',
      vendor: 'Thingamahoochie Software',
    },
    {
      name: 'Microsoft Visual C++ 2013 x64 Additional Runtime - 12.0.40664',
      location: '',
      version: '12.0.40664',
      date: '20200325',
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'DaVinci Resolve Keyboards',
      location: '',
      version: '1.0.0.0',
      date: '20200506',
      vendor: 'Blackmagic Design',
    },
    {
      name: 'VMware Workstation',
      location: '',
      version: '15.5.2',
      date: '20200607',
      vendor: 'VMware, Inc.',
    },
    {
      name: 'MSVCRT Redists',
      location: '',
      version: '1.0',
      date: '20200319',
      vendor: 'MAGIX Computer Products Intl. Co.',
    },
    {
      name: 'Dolby Atmos Windows API SDK',
      location: 'C:\\Program Files\\Dolby\\Dolby DAX3\\',
      version: '1.1.3.23',
      date: '20200303',
      vendor: 'Dolby Laboratories, Inc.',
    },
    {
      name: 'Microsoft Visual C++ 2019 X64 Additional Runtime - 14.20.27508',
      location: '',
      version: '14.20.27508',
      date: '20200526',
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'Microsoft Visual C++ 2013 x64 Minimum Runtime - 12.0.40664',
      location: '',
      version: '12.0.40664',
      date: '20200325',
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'Slack Machine-Wide',
      location: '',
      version: '4.4.2.0',
      date: '20200420',
      vendor: 'Slack Technologies',
    },
    {
      name: 'DaVinci Resolve Panels',
      location: '',
      version: '1.3.2.0',
      date: '20200506',
      vendor: 'Blackmagic Design',
    },
    {
      name: 'Java SE Development Kit 8 Update 211 (64-bit)',
      location: 'C:\\Program Files\\Java\\jdk1.8.0_211\\',
      version: '8.0.2110.12',
      date: '20200326',
      vendor: 'Oracle Corporation',
    },
    {
      name: 'Intel® Hardware Accelerated Execution Manager',
      location: '',
      version: '7.5.6',
      date: '20200326',
      vendor: 'Intel Corporation',
    },
    {
      name: 'DaVinci Resolve',
      location: '',
      version: '16.2.1017',
      date: '20200506',
      vendor: 'Blackmagic Design',
    },
    {
      name: 'Office 16 Click-to-Run Licensing Component',
      location: '',
      version: '16.0.12624.20442',
      date: '20200410',
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'Office 16 Click-to-Run Extensibility Component',
      location: '',
      version: '16.0.12624.20442',
      date: '20200410',
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'Office 16 Click-to-Run Localization Component',
      location: '',
      version: '16.0.12624.20442',
      date: '20200410',
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'Python 2.7.17 (64-bit)',
      location: '',
      version: '2.7.17150',
      date: '20200326',
      vendor: 'Python Software Foundation',
    },
    {
      name: 'Blackmagic RAW Common Components',
      location: '',
      version: '1.7',
      date: '20200506',
      vendor: 'Blackmagic Design',
    },
    {
      name: 'Node.js',
      location: '',
      version: '13.11.0',
      date: '20200326',
      vendor: 'Node.js Foundation',
    },
    {
      name: 'Lenovo Bluetooth with Enhanced Data Rate Software',
      location: 'C:\\Program Files\\Lenovo\\Bluetooth Software\\',
      version: '12.0.1.720',
      date: '20200303',
      vendor: 'Broadcom Corporation',
    },
    {
      name: 'Microsoft Visual Studio Code',
      location: 'C:\\Program Files\\Microsoft VS Code\\',
      version: '1.45.1',
      date: '20200520',
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.20.27508',
      location: '',
      version: '14.20.27508',
      date: '20200526',
      vendor: 'Microsoft Corporation',
    },
    {
      name: 'Backup and Sync from Google',
      location: '',
      version: '3.49.9800.0000',
      date: '20200416',
      vendor: 'Google, Inc.',
    },
  ],
};

storiesOf('Organisms/InstalledSoftware', module)
  .addDecorator(StoryRouter())
  .add('Normal', () => (
    <InstalledSoftware
      searchLocation={dummyData.key}
      softwares={dummyData.softwares}
    />
  ));
