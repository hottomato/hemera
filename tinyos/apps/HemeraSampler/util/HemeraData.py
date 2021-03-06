#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'HemeraData'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 9

# The Active Message type associated with this message.
AM_TYPE = -1

class HemeraData(tinyos.message.Message.Message):
    # Create a new HemeraData of size 9.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=9):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <HemeraData> \n"
        try:
            s += "  [temperature=0x%x]\n" % (self.get_temperature())
        except:
            pass
        try:
            s += "  [humidity=0x%x]\n" % (self.get_humidity())
        except:
            pass
        try:
            s += "  [light=0x%x]\n" % (self.get_light())
        except:
            pass
        try:
            s += "  [motion=0x%x]\n" % (self.get_motion())
        except:
            pass
        try:
            s += "  [battery=0x%x]\n" % (self.get_battery())
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: temperature
    #   Field type: int
    #   Offset (bits): 0
    #   Size (bits): 16
    #

    #
    # Return whether the field 'temperature' is signed (False).
    #
    def isSigned_temperature(self):
        return False
    
    #
    # Return whether the field 'temperature' is an array (False).
    #
    def isArray_temperature(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'temperature'
    #
    def offset_temperature(self):
        return (0 / 8)
    
    #
    # Return the offset (in bits) of the field 'temperature'
    #
    def offsetBits_temperature(self):
        return 0
    
    #
    # Return the value (as a int) of the field 'temperature'
    #
    def get_temperature(self):
        return self.getUIntElement(self.offsetBits_temperature(), 16, 1)
    
    #
    # Set the value of the field 'temperature'
    #
    def set_temperature(self, value):
        self.setUIntElement(self.offsetBits_temperature(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'temperature'
    #
    def size_temperature(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'temperature'
    #
    def sizeBits_temperature(self):
        return 16
    
    #
    # Accessor methods for field: humidity
    #   Field type: int
    #   Offset (bits): 16
    #   Size (bits): 16
    #

    #
    # Return whether the field 'humidity' is signed (False).
    #
    def isSigned_humidity(self):
        return False
    
    #
    # Return whether the field 'humidity' is an array (False).
    #
    def isArray_humidity(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'humidity'
    #
    def offset_humidity(self):
        return (16 / 8)
    
    #
    # Return the offset (in bits) of the field 'humidity'
    #
    def offsetBits_humidity(self):
        return 16
    
    #
    # Return the value (as a int) of the field 'humidity'
    #
    def get_humidity(self):
        return self.getUIntElement(self.offsetBits_humidity(), 16, 1)
    
    #
    # Set the value of the field 'humidity'
    #
    def set_humidity(self, value):
        self.setUIntElement(self.offsetBits_humidity(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'humidity'
    #
    def size_humidity(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'humidity'
    #
    def sizeBits_humidity(self):
        return 16
    
    #
    # Accessor methods for field: light
    #   Field type: int
    #   Offset (bits): 32
    #   Size (bits): 16
    #

    #
    # Return whether the field 'light' is signed (False).
    #
    def isSigned_light(self):
        return False
    
    #
    # Return whether the field 'light' is an array (False).
    #
    def isArray_light(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'light'
    #
    def offset_light(self):
        return (32 / 8)
    
    #
    # Return the offset (in bits) of the field 'light'
    #
    def offsetBits_light(self):
        return 32
    
    #
    # Return the value (as a int) of the field 'light'
    #
    def get_light(self):
        return self.getUIntElement(self.offsetBits_light(), 16, 1)
    
    #
    # Set the value of the field 'light'
    #
    def set_light(self, value):
        self.setUIntElement(self.offsetBits_light(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'light'
    #
    def size_light(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'light'
    #
    def sizeBits_light(self):
        return 16
    
    #
    # Accessor methods for field: motion
    #   Field type: short
    #   Offset (bits): 48
    #   Size (bits): 8
    #

    #
    # Return whether the field 'motion' is signed (False).
    #
    def isSigned_motion(self):
        return False
    
    #
    # Return whether the field 'motion' is an array (False).
    #
    def isArray_motion(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'motion'
    #
    def offset_motion(self):
        return (48 / 8)
    
    #
    # Return the offset (in bits) of the field 'motion'
    #
    def offsetBits_motion(self):
        return 48
    
    #
    # Return the value (as a short) of the field 'motion'
    #
    def get_motion(self):
        return self.getUIntElement(self.offsetBits_motion(), 8, 1)
    
    #
    # Set the value of the field 'motion'
    #
    def set_motion(self, value):
        self.setUIntElement(self.offsetBits_motion(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'motion'
    #
    def size_motion(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'motion'
    #
    def sizeBits_motion(self):
        return 8
    
    #
    # Accessor methods for field: battery
    #   Field type: int
    #   Offset (bits): 56
    #   Size (bits): 16
    #

    #
    # Return whether the field 'battery' is signed (False).
    #
    def isSigned_battery(self):
        return False
    
    #
    # Return whether the field 'battery' is an array (False).
    #
    def isArray_battery(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'battery'
    #
    def offset_battery(self):
        return (56 / 8)
    
    #
    # Return the offset (in bits) of the field 'battery'
    #
    def offsetBits_battery(self):
        return 56
    
    #
    # Return the value (as a int) of the field 'battery'
    #
    def get_battery(self):
        return self.getUIntElement(self.offsetBits_battery(), 16, 1)
    
    #
    # Set the value of the field 'battery'
    #
    def set_battery(self, value):
        self.setUIntElement(self.offsetBits_battery(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'battery'
    #
    def size_battery(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'battery'
    #
    def sizeBits_battery(self):
        return 16
    
