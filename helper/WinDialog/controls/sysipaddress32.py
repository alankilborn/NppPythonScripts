""" Dialog SYSIPADDRESS32 control implementation """
from dataclasses import dataclass
from .__control_template import Control

@dataclass
class IPAddress(Control):
    window_class: str = 'SysIPAddress32'