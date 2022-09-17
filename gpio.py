try:
    import RPi.GPIO as GPIO
except RuntimeError:
    from types import SimpleNamespace
    print(f'Not running on Raspberry PI, proceeding with GPIO mock...')
    GPIO = SimpleNamespace(
        OUT=None,
        LOW=None,
        HIGH=None,
        BOARD=None,
        BCM=None,
        setup=lambda channel, direction: None,
        cleanup=lambda: None,
        output=lambda channel, state: None,
        setmode=lambda mode: None,
        PWM=lambda channel, frequency: SimpleNamespace(
            ChangeFrequency=lambda _: None,
            start=lambda duty_cycle: None,
            stop=lambda: None
        )
    )
