from machine import Pin, ADC, I2C
from time import sleep_ms, ticks_ms
from math import pi, sin
from ssd1306 import SSD1306_I2C
from screens import load_screen, interface_screen
import framebuf


pot_A = ADC(26)
pot_F = ADC(27)

class Functions():
    def sin(t: float ,amplitude: float, frequency: float, phase: float):
        w = 2 * pi * frequency
        return amplitude * sin(w * (t * 1e-3) + phase)
    
    def tan(amplitude: float, frequency: float, phase: float):
        pass


class Configs():
    # pins
    deep_swich_pins: list
    voltage_pot_pin: int
    frequency_pot_pin: int
    noise_button_pin: int
    sda_oled_pin: int
    scl_oled_pin: int
    
    # consts
    function_list: list
    max_voltage: float
    min_voltage: float
    max_frequency: float
    min_frequency: float
    oled_height: int
    oled_width: int
    
    def __init__(self) -> None:
        pass
    
    
    def default(self) -> None:
        self.deep_swich_pins = [5, 4, 3, 2]
        self.voltage_pot_pin = 26
        self.frequency_pot_pin = 27
        self.sda_oled_pin = 0
        self.scl_oled_pin = 1
        self.oled_height = 32
        self.oled_width = 128
        
        self.function_list = [
            Functions.sin,
            Functions.tan
        ]
        
        self.max_voltage = 3.3
        self.min_voltage = 0
        self.max_frequency = 0.1
        self.min_frequency = 1 / 0.018


class Machine():
    ## options
    configs: Configs
    
    ## calculated
    mv: float
    mf: float
    
    ## states
    frequency: float
    voltage: float
    option: int
    active_function: any
    
    ## pins
    deep_swich: list
    voltage_pot: Pin
    frequency_pot: Pin
    noise_button: Pin
    
    ## objects
    oled: SSD1306_I2C
    
    ## screens
    load_arr: list = load_screen
    interface_arr: list = interface_screen
    
    ## init
    def __init__(self, configs: Configs, setup: any, loop: any) -> None:
        # options
        self.configs = configs
        
        # pins
        self.deep_swich = []
        for swich_pin in configs.deep_swich_pins:
            self.deep_swich.append(
                Pin(swich_pin, Pin.IN, Pin.PULL_UP)              
            )
        
        # calculated
        self.mv = (configs.max_voltage - configs.min_voltage) / 2**16
        self.mf = (configs.max_frequency - configs.min_frequency) / 2**16
        
        ##
        self.setup = setup
        self.loop = loop
        
        i2c = I2C(sda = configs.sda_oled_pin, scl = configs.scl_oled_pin)
        
        self.oled = SSD1306_I2C(128, 32, i2c)
        
    # getters
    def getVoltage(self) -> float:
        return self.mv * self.voltage_pot.value() + self.min_voltage
    
    def getFrequency(self) -> float:
        return self.mf * self.frequency_pot.value() + self.min_frequency
    
    
    def getOption(self) -> float:
        bits = '0b'
        
        for swich in self.deep_swich:
            bits += str(swich.value())
            
        return int(bits, 2)
    
    
    ## events
    def optionChanged(self) -> bool:
        return op != self.getOption()
    
    # hooks
    def start(self) -> None:
        self.begin()
        self.setup(self)
        while True:
            self.step()
            self.loop(self)
    
    
    def begin(self) -> None:
        self.op = self.getOption()
    
    
    def step(self) -> None: 
        if self.otionChanged():
            pass
            
    
    def newOption(self) -> None:
        pass

    ## program 
    def setup(self) -> None:
        pass

    def loop(self) -> None:
        pass
    
    ## hooks
        
        
        
