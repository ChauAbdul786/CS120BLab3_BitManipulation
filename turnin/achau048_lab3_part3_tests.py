# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'PINA: 0x00 => PORTC:0x40 (Fuel Level 0 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 5 } ],
	'expected': [('PORTC',0x40)],
	},
	{'description': 'PINA: 0x01 => PORTC: 0x60 (Fuel Level 1 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x01),('PINB',0x00)], 'iterations': 5 } ],
	'expected': [('PORTC',0x60)],
	},
	{'description': 'PINA: 0x02 => PORTC: 0x60 (Fuel Level 2 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x02)], 'iterations': 5 } ],
	'expected': [('PORTC',0x60)],
	},
	{'description': 'PINA: 0x03 => PORTC: 0x70 (Fuel Level 3 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x03)], 'iterations': 5 } ],
	'expected': [('PORTC',0x70)],
	},
	{'description': 'PINA: 0x04 => PORTC: 0x70 (Fuel Level 4 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x04)], 'iterations': 5 } ],
	'expected': [('PORTC',0x70)],
	},
	{'description': 'PINA: 0x05 => PORTC: 0x38 (Fuel Level 5 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x05)], 'iterations': 5 } ],
	'expected': [('PORTC',0x38)],
	},
	{'description': 'PINA: 0x06 => PORTC: 0x38 (Fuel Level 6 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x06)], 'iterations': 5 } ],
	'expected': [('PORTC',0x38)],
	},
	{'description': 'PINA: 0x07 => PORTC: 0x3C (Fuel Level 7 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x07)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3C)],
	},
	{'description': 'PINA: 0x08 => PORTC: 0x3C (Fuel Level 8 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x08)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3C)],
	},
	{'description': 'PINA: 0x09 => PORTC: 0x3C (Fuel Level 9 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x09)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3C)],
	},
	{'description': 'PINA: 0x0A => PORTC: 0x3E (Fuel Level 10 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x0A)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3E)],
	},
	{'description': 'PINA: 0x0B => PORTC: 0x3E (Fuel Level 11 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x0B)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3E)],
	},
	{'description': 'PINA: 0x0C => PORTC: 0x3E (Fuel Level 12 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x0C)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3E)],
	},
	{'description': 'PINA: 0x0D => PORTC: 0x3F (Fuel Level 13 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x0D)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3F)],
	},
	{'description': 'PINA: 0x0E => PORTC: 0x3F (Fuel Level 14 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x0E)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3F)],
	},
	{'description': 'PINA: 0x0F => PORTC: 0x3F (Fuel Level 15 No Fasten Seatbelt Light)',
	'steps': [ {'inputs': [('PINA',0x0F)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3F)],
	},
	{'description': 'PINA: 0x10 => PORTC: 0x40 (Only Ignition No Gas)',
	'steps': [ {'inputs': [('PINA',0x10)], 'iterations': 5 } ],
	'expected': [('PORTC',0x40)],
	},
	{'description': 'PINA: 0x1A => PORTC: 0x3E (Only Ignition With Gas)',
	'steps': [ {'inputs': [('PINA',0x1A)], 'iterations': 5 } ],
	'expected': [('PORTC',0x3E)],
	},
	{'description': 'PINA: 0x3F => PORTC: 0xBF (Fasten Seatbelt)',
	'steps': [ {'inputs': [('PINA',0x3F)], 'iterations': 5 } ],
	'expected': [('PORTC',0xBF)],
	},
	]
#watch = ['PORTB']

