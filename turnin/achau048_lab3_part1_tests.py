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
tests = [ {'description': 'PINA: 0x00, PINB: 0x00 => PORTC:0x00 (Zero)',
	'steps': [ {'inputs': [('PINA',0x00),('PINB',0x00)], 'iterations': 5 } ],
	'expected': [('PORTC',0x00)],
	},
	{'description': 'PINA: 0x01, PINB: 0x00 => PORTC: 0x01 (One)',
	'steps': [ {'inputs': [('PINA',0x01),('PINB',0x00)], 'iterations': 5 } ],
	'expected': [('PORTC',0x01)],
	},
	{'description': 'PINA: 0x01, PINB: 0x01 => PORTC: 0x02 (Two)',
	'steps': [ {'inputs': [('PINA',0x01),('PINB',0x01)], 'iterations': 5 } ],
	'expected': [('PORTC',0x02)],
	},
	{'description': 'PINA: 0xF0, PINB: 0x0C => PORTC: 0x06 (Six)',
	'steps': [ {'inputs': [('PINA',0xF0),('PINB',0x0C)], 'iterations': 5 } ],
	'expected': [('PORTC',0x06)],
	},
	{'description': 'PINA: 0xFF, PINB: 0xFF => PORTC: 0x10 (Full)',
	'steps': [ {'inputs': [('PINA',0xFF),('PINB',0xFF)], 'iterations': 5 } ],
	'expected': [('PORTC',0x10)],
	},
	{'description': 'PINA: 0xFF, PINB: 0x00 => PORTC: 0x08 (A Full, B Empty)',
	'steps': [ {'inputs': [('PINA',0xFF),('PINB',0x00)], 'iterations': 5 } ],
	'expected': [('PORTC',0x08)],
	},
	{'description': 'PINA: 0x00, PINB: 0xFF => PORTC: 0x08 (A Empty, B Full)',
	'steps': [ {'inputs': [('PINA',0x00),('PINB',0xFF)], 'iterations': 5 } ],
	'expected': [('PORTC',0x08)],
	},
	{'description': 'PINA: 0xAA, PINB: 0x55 => PORTC: 0x08',
	'steps': [ {'inputs': [('PINA',0xAA),('PINB',0x55)], 'iterations': 5 } ],
	'expected': [('PORTC',0x08)],
	},
	{'description': 'PINA: 0xCC, PINB: 0xCC => PORTC: 0x08',
	'steps': [ {'inputs': [('PINA',0xCC),('PINB',0xCC)], 'iterations': 5 } ],
	'expected': [('PORTC',0x08)],
	},
	]
#watch = ['PORTB']

