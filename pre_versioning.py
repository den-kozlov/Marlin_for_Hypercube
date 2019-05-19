Import("env")
from datetime import datetime

env.ProcessFlags("-DUSE_AUTOMATIC_VERSIONING=1")
env.Append(CPPDEFINES=[
  ("USE_AUTOMATIC_VERSIONING", "1")
])

custom_version_file = open('Marlin/src/inc/_Version.h', 'w')
custom_version_file.write('#define SHORT_BUILD_VERSION "2.0 for SKR v1.3"\n')
custom_version_file.write('#define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION " (Github)"\n')
custom_version_file.write('#define REQUIRED_CONFIGURATION_H_VERSION 020000\n')
custom_version_file.write('#define REQUIRED_CONFIGURATION_ADV_H_VERSION 020000\n')
custom_version_file.write('#define PROTOCOL_VERSION "1.0"\n')
custom_version_file.write('#define MACHINE_NAME "3D Printer"\n')
custom_version_file.write('#define SOURCE_CODE_URL "https://github.com/MarlinFirmware/Marlin"\n')
custom_version_file.write('#define DEFAULT_MACHINE_UUID "cede2a2f-41a2-4748-9b12-c55c62f367ff"\n')
custom_version_file.write('#define WEBSITE_URL "http://marlinfw.org"\n')

now = datetime.now()
custom_version_file.write('#define STRING_DISTRIBUTION_DATE "{0}"\n'.format(now.strftime("%Y-%m-%d")))

custom_version_file.close()

